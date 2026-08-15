import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:file_picker/file_picker.dart';
import 'package:provider/provider.dart';
import '../services/auth_service.dart';
import '../services/api_service.dart';
import '../services/activity_service.dart';
import '../providers/app_provider.dart';
import '../models/repository.dart';
import '../widgets/file_icon.dart';
import '../theme/app_theme.dart';

class UploadScreen extends StatefulWidget {
  final String? initialRepoOwner;
  final String? initialRepoName;
  final String? initialFolder;

  const UploadScreen({
    super.key,
    this.initialRepoOwner,
    this.initialRepoName,
    this.initialFolder,
  });

  @override
  State<UploadScreen> createState() => _UploadScreenState();
}

class _UploadScreenState extends State<UploadScreen> {
  Repository? _selectedRepo;
  late TextEditingController _folderPathController;
  late TextEditingController _commitMsgController;
  String _selectedBranch = "main";
  List<PlatformFile> _selectedFiles = [];
  bool _isUploading = false;
  double _uploadProgress = 0.0;
  String? _statusMessage;
  String? _errorMessage;

  @override
  void initState() {
    super.initState();
    _folderPathController = TextEditingController(text: widget.initialFolder ?? "");
    _commitMsgController = TextEditingController(text: "Add files via Mobile Git Workspace");

    WidgetsBinding.instance.addPostFrameCallback((_) {
      final appProv = Provider.of<AppProvider>(context, listen: false);
      if (widget.initialRepoOwner != null && widget.initialRepoName != null) {
        final match = appProv.repositories.where(
          (r) => r.owner == widget.initialRepoOwner && r.name == widget.initialRepoName,
        );
        if (match.isNotEmpty) {
          setState(() {
            _selectedRepo = match.first;
            _selectedBranch = _selectedRepo!.defaultBranch;
          });
        }
      } else if (appProv.selectedRepo != null) {
        setState(() {
          _selectedRepo = appProv.selectedRepo;
          _selectedBranch = _selectedRepo!.defaultBranch;
        });
      } else if (appProv.repositories.isNotEmpty) {
        setState(() {
          _selectedRepo = appProv.repositories.first;
          _selectedBranch = _selectedRepo!.defaultBranch;
        });
      }
    });
  }

  @override
  void dispose() {
    _folderPathController.dispose();
    _commitMsgController.dispose();
    super.dispose();
  }

  Future<void> _pickFiles() async {
    try {
      final result = await FilePicker.platform.pickFiles(
        allowMultiple: true,
        withData: true,
      );
      if (result != null && result.files.isNotEmpty) {
        setState(() {
          _selectedFiles = result.files;
          if (_selectedFiles.length == 1) {
            _commitMsgController.text = "Add ${_selectedFiles.first.name} via Mobile Git Workspace";
          } else {
            _commitMsgController.text = "Add ${_selectedFiles.length} files via Mobile Git Workspace";
          }
          _errorMessage = null;
        });
      }
    } catch (e) {
      setState(() {
        _errorMessage = "Failed to pick files: $e";
      });
    }
  }

  Future<void> _executeUploadAndCommit() async {
    if (_selectedRepo == null) {
      setState(() => _errorMessage = "Please select a destination repository.");
      return;
    }
    if (_selectedFiles.isEmpty) {
      setState(() => _errorMessage = "Please select at least one file from phone storage.");
      return;
    }

    final commitMsg = _commitMsgController.text.trim();
    if (commitMsg.isEmpty) {
      setState(() => _errorMessage = "Please enter a commit message.");
      return;
    }

    final auth = Provider.of<AuthService>(context, listen: false);
    if (auth.token == null) return;

    setState(() {
      _isUploading = true;
      _uploadProgress = 0.0;
      _statusMessage = "Preparing files for upload...";
      _errorMessage = null;
    });

    final total = _selectedFiles.length;
    int completed = 0;
    List<String> uploadedPaths = [];

    try {
      for (var i = 0; i < total; i++) {
        final f = _selectedFiles[i];
        if (f.bytes == null) continue;

        setState(() {
          _statusMessage = "Committing ${f.name} (${i + 1}/$total)...";
          _uploadProgress = (i + 0.5) / total;
        });

        final commitMessagePerFile = total == 1 ? commitMsg : "$commitMsg (${f.name})";

        final sha = await ApiService.uploadPhoneFile(
          token: auth.token!,
          owner: _selectedRepo!.owner,
          repo: _selectedRepo!.name,
          folderPath: _folderPathController.text,
          filename: f.name,
          bytes: f.bytes!,
          message: commitMessagePerFile,
          branch: _selectedBranch,
        );

        final cleanFolder = _folderPathController.text.trim().replaceAll(RegExp(r'^/|/$'), '');
        final targetPath = cleanFolder.isNotEmpty ? "$cleanFolder/${f.name}" : f.name;
        uploadedPaths.add(targetPath);

        completed++;
        setState(() {
          _uploadProgress = completed / total;
        });
      }

      // Log activity
      final activity = Provider.of<ActivityService>(context, listen: false);
      activity.logActivity(
        actionType: "uploaded",
        repoName: _selectedRepo!.name,
        filePath: uploadedPaths.join(", "),
        commitMessage: commitMsg,
        branch: _selectedBranch,
      );

      // Refresh provider directory contents if target repo is currently selected
      final appProv = Provider.of<AppProvider>(context, listen: false);
      if (appProv.selectedRepo?.fullName == _selectedRepo!.fullName) {
        await appProv.refreshDirectoryContents(auth.token!);
      }

      setState(() {
        _isUploading = false;
        _statusMessage = "Successfully uploaded and committed $completed files!";
      });

      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            backgroundColor: AppTheme.successGreen,
            content: Row(
              children: [
                const Icon(Icons.check_circle_rounded, color: Colors.white),
                const SizedBox(width: 10),
                Expanded(child: Text("Files committed directly to GitHub!")),
              ],
            ),
          ),
        );
        Navigator.pop(context);
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _isUploading = false;
          _errorMessage = e.toString().replaceAll("Exception: ", "");
        });
      }
    }
  }

  String _formatBytes(int bytes) {
    if (bytes < 1024) return "$bytes B";
    if (bytes < 1024 * 1024) return "${(bytes / 1024).toStringAsFixed(1)} KB";
    return "${(bytes / (1024 * 1024)).toStringAsFixed(1)} MB";
  }

  @override
  Widget build(BuildContext context) {
    final appProv = Provider.of<AppProvider>(context);

    return Scaffold(
      backgroundColor: AppTheme.darkBg,
      appBar: AppBar(
        title: Text("Upload Files From Phone", style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Target Repository Picker
            Text(
              "Destination Repository",
              style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
            ),
            const SizedBox(height: 8),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 14),
              decoration: BoxDecoration(
                color: AppTheme.surfaceBg,
                borderRadius: BorderRadius.circular(10),
                border: Border.all(color: AppTheme.borderDark),
              ),
              child: DropdownButtonHideUnderline(
                child: DropdownButton<Repository>(
                  value: _selectedRepo,
                  isExpanded: true,
                  dropdownColor: AppTheme.cardBg,
                  icon: const Icon(Icons.keyboard_arrow_down_rounded, color: AppTheme.primaryCyan),
                  items: appProv.repositories.map((r) {
                    return DropdownMenuItem<Repository>(
                      value: r,
                      child: Text(r.fullName, style: GoogleFonts.inter(color: AppTheme.textPrimary, fontSize: 14)),
                    );
                  }).toList(),
                  onChanged: (r) {
                    setState(() {
                      _selectedRepo = r;
                      if (r != null) _selectedBranch = r.defaultBranch;
                    });
                  },
                ),
              ),
            ),
            const SizedBox(height: 16),

            // Target Folder Path & Target Branch
            Row(
              children: [
                Expanded(
                  flex: 2,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text("Folder / Path", style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
                      const SizedBox(height: 6),
                      TextField(
                        controller: _folderPathController,
                        style: GoogleFonts.jetBrainsMono(fontSize: 13, color: AppTheme.textPrimary),
                        decoration: const InputDecoration(
                          hintText: "docs/ or src/",
                          prefixIcon: Icon(Icons.folder_outlined, color: AppTheme.primaryCyan, size: 20),
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  flex: 1,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text("Branch", style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
                      const SizedBox(height: 6),
                      Container(
                        height: 48,
                        padding: const EdgeInsets.symmetric(horizontal: 10),
                        decoration: BoxDecoration(
                          color: AppTheme.surfaceBg,
                          borderRadius: BorderRadius.circular(10),
                          border: Border.all(color: AppTheme.borderDark),
                        ),
                        child: Center(
                          child: Text(
                            _selectedBranch,
                            style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.primaryCyan),
                            overflow: TextOverflow.ellipsis,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 20),

            // Select Files Box
            Text("Select Files", style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
            const SizedBox(height: 8),
            InkWell(
              onTap: _isUploading ? null : _pickFiles,
              borderRadius: BorderRadius.circular(12),
              child: Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(vertical: 24, horizontal: 16),
                decoration: BoxDecoration(
                  color: AppTheme.cardBg,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: AppTheme.primaryCyan.withOpacity(0.5), width: 1.5),
                ),
                child: Column(
                  children: [
                    Container(
                      padding: const EdgeInsets.all(12),
                      decoration: BoxDecoration(
                        color: AppTheme.primaryCyan.withOpacity(0.15),
                        shape: BoxShape.circle,
                      ),
                      child: const Icon(Icons.file_upload_outlined, color: AppTheme.primaryCyan, size: 32),
                    ),
                    const SizedBox(height: 10),
                    Text(
                      _selectedFiles.isEmpty ? "Tap to select files from phone storage" : "Tap to change selected files",
                      style: GoogleFonts.inter(fontSize: 14, fontWeight: FontWeight.bold, color: AppTheme.primaryCyan),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      "Supports documents, images, code, laboratory coursework, PDFs",
                      style: GoogleFonts.inter(fontSize: 11, color: AppTheme.textSecondary),
                      textAlign: TextAlign.center,
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),

            // Selected Files List Preview
            if (_selectedFiles.isNotEmpty) ...[
              Text("Selected Files (${_selectedFiles.length}):", style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
              const SizedBox(height: 8),
              Container(
                decoration: BoxDecoration(
                  color: AppTheme.surfaceBg,
                  borderRadius: BorderRadius.circular(10),
                  border: Border.all(color: AppTheme.borderDark),
                ),
                child: ListView.separated(
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  itemCount: _selectedFiles.length,
                  separatorBuilder: (_, __) => const Divider(color: AppTheme.borderDark, height: 1),
                  itemBuilder: (ctx, idx) {
                    final f = _selectedFiles[idx];
                    return ListTile(
                      dense: true,
                      leading: FileTypeIcon(fileName: f.name, isDirectory: false),
                      title: Text(f.name, style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.w600, color: AppTheme.textPrimary)),
                      subtitle: Text(_formatBytes(f.size), style: GoogleFonts.inter(fontSize: 11, color: AppTheme.textSecondary)),
                      trailing: IconButton(
                        icon: const Icon(Icons.close_rounded, size: 18, color: AppTheme.dangerRed),
                        onPressed: () {
                          setState(() {
                            _selectedFiles.removeAt(idx);
                          });
                        },
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(height: 20),
            ],

            // Commit Message Input
            Text("Commit Message", style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
            const SizedBox(height: 8),
            TextField(
              controller: _commitMsgController,
              maxLines: 2,
              style: GoogleFonts.inter(fontSize: 14, color: AppTheme.textPrimary),
              decoration: const InputDecoration(
                hintText: "Add laboratory coursework",
              ),
            ),
            const SizedBox(height: 16),

            // Progress & Errors
            if (_isUploading) ...[
              LinearProgressIndicator(
                value: _uploadProgress,
                backgroundColor: AppTheme.surfaceBg,
                color: AppTheme.primaryCyan,
              ),
              const SizedBox(height: 8),
              if (_statusMessage != null)
                Text(_statusMessage!, style: GoogleFonts.inter(fontSize: 12, color: AppTheme.primaryCyan)),
              const SizedBox(height: 16),
            ],

            if (_errorMessage != null) ...[
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: AppTheme.dangerRed.withOpacity(0.15),
                  borderRadius: BorderRadius.circular(8),
                  border: Border.all(color: AppTheme.dangerRed),
                ),
                child: Row(
                  children: [
                    const Icon(Icons.error_outline, color: AppTheme.dangerRed, size: 18),
                    const SizedBox(width: 8),
                    Expanded(child: Text(_errorMessage!, style: GoogleFonts.inter(color: AppTheme.dangerRed, fontSize: 12))),
                  ],
                ),
              ),
              const SizedBox(height: 16),
            ],

            // Primary Upload & Commit Button
            SizedBox(
              width: double.infinity,
              height: 52,
              child: ElevatedButton.icon(
                onPressed: _isUploading ? null : _executeUploadAndCommit,
                icon: const Icon(Icons.cloud_upload_rounded, color: Colors.black),
                label: Text(
                  "Upload & Commit",
                  style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.bold),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
