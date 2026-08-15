import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_markdown/flutter_markdown.dart';
import 'package:flutter_highlight/flutter_highlight.dart';
import 'package:flutter_highlight/theme_map.dart';
import 'package:provider/provider.dart';
import '../services/auth_service.dart';
import '../services/api_service.dart';
import '../services/activity_service.dart';
import '../providers/app_provider.dart';
import '../models/file_detail.dart';
import '../widgets/pre_commit_dialog.dart';
import '../theme/app_theme.dart';

class CodeEditorScreen extends StatefulWidget {
  final String repoOwner;
  final String repoName;
  final String? filePath;
  final String initialBranch;
  final String? fileSha;
  final String? initialFolder;
  final bool isNewFile;

  const CodeEditorScreen({
    super.key,
    required this.repoOwner,
    required this.repoName,
    this.filePath,
    required this.initialBranch,
    this.fileSha,
    this.initialFolder,
    this.isNewFile = false,
  });

  @override
  State<CodeEditorScreen> createState() => _CodeEditorScreenState();
}

class _CodeEditorScreenState extends State<CodeEditorScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  late TextEditingController _fileNameController;
  late TextEditingController _codeController;
  late TextEditingController _searchController;

  bool _isLoading = false;
  String? _errorMsg;
  FileDetail? _fileDetail;
  String _currentBranch = "main";
  bool _isSearchVisible = false;
  String _searchQuery = "";

  @override
  void initState() {
    super.initState();
    _currentBranch = widget.initialBranch;
    _tabController = TabController(length: 2, vsync: this);
    
    final path = widget.filePath ?? "";
    final filename = path.contains('/') ? path.split('/').last : path;
    _fileNameController = TextEditingController(text: filename);
    _codeController = TextEditingController();
    _searchController = TextEditingController();

    if (!widget.isNewFile && widget.filePath != null) {
      _loadFileContent();
    }
  }

  @override
  void dispose() {
    _tabController.dispose();
    _fileNameController.dispose();
    _codeController.dispose();
    _searchController.dispose();
    super.dispose();
  }

  Future<void> _loadFileContent() async {
    final auth = Provider.of<AuthService>(context, listen: false);
    if (auth.token == null || widget.filePath == null) return;

    setState(() {
      _isLoading = true;
      _errorMsg = null;
    });

    try {
      final detail = await ApiService.fetchFileDetail(
        auth.token!,
        widget.repoOwner,
        widget.repoName,
        widget.filePath!,
        branch: _currentBranch,
      );

      setState(() {
        _fileDetail = detail;
        _codeController.text = detail.decodedText;
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _isLoading = false;
        _errorMsg = e.toString().replaceAll("Exception: ", "");
      });
    }
  }

  String _detectLanguage(String path) {
    final ext = path.contains('.') ? path.split('.').last.toLowerCase() : '';
    switch (ext) {
      case 'py': return 'python';
      case 'js':
      case 'jsx': return 'javascript';
      case 'ts':
      case 'tsx': return 'typescript';
      case 'html': return 'html';
      case 'css': return 'css';
      case 'md': return 'markdown';
      case 'json': return 'json';
      case 'yaml':
      case 'yml': return 'yaml';
      case 'xml': return 'xml';
      case 'sh':
      case 'bash': return 'bash';
      case 'dart': return 'dart';
      default: return 'plaintext';
    }
  }

  bool _isImageFile(String path) {
    final ext = path.contains('.') ? path.split('.').last.toLowerCase() : '';
    return ['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp'].contains(ext);
  }

  Future<void> _handleSaveAndCommit() async {
    final fileName = _fileNameController.text.trim();
    if (fileName.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text("Please enter a valid file name.")));
      return;
    }

    final auth = Provider.of<AuthService>(context, listen: false);
    if (auth.token == null) return;

    final folder = widget.initialFolder?.trim().replaceAll(RegExp(r'^/|/$'), '') ?? '';
    final fullPath = widget.isNewFile
        ? (folder.isNotEmpty ? "$folder/$fileName" : fileName)
        : (widget.filePath ?? fileName);

    final rawContent = _codeController.text;
    final b64Content = base64Encode(utf8.encode(rawContent));

    final initialMsg = widget.isNewFile
        ? "Create $fileName via Mobile Git Workspace"
        : "Update $fileName via Mobile Git Workspace";

    PreCommitDialog.show(
      context,
      repoName: widget.repoName,
      branch: _currentBranch,
      changedFiles: [widget.isNewFile ? "CREATE: $fullPath" : "MODIFY: $fullPath"],
      initialCommitMessage: initialMsg,
      onCommit: (commitMsg) async {
        final sha = await ApiService.commitFile(
          token: auth.token!,
          owner: widget.repoOwner,
          repo: widget.repoName,
          path: fullPath,
          message: commitMsg,
          contentB64: b64Content,
          branch: _currentBranch,
          sha: widget.fileSha,
        );

        final activity = Provider.of<ActivityService>(context, listen: false);
        activity.logActivity(
          actionType: widget.isNewFile ? "created" : "updated",
          repoName: widget.repoName,
          filePath: fullPath,
          commitMessage: commitMsg,
          branch: _currentBranch,
        );

        final appProv = Provider.of<AppProvider>(context, listen: false);
        if (appProv.selectedRepo?.name == widget.repoName) {
          await appProv.refreshDirectoryContents(auth.token!);
        }

        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(backgroundColor: AppTheme.successGreen, content: Text("Successfully committed to $_currentBranch!")),
          );
          Navigator.pop(context);
        }
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final currentPath = widget.filePath ?? _fileNameController.text;
    final lang = _detectLanguage(currentPath);
    final isMarkdown = lang == 'markdown';
    final isImage = _isImageFile(currentPath);

    return Scaffold(
      backgroundColor: AppTheme.darkBg,
      appBar: AppBar(
        title: widget.isNewFile
            ? TextField(
                controller: _fileNameController,
                style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
                decoration: const InputDecoration(
                  hintText: "Filename (e.g. main.py)",
                  border: InputBorder.none,
                ),
              )
            : Text(
                _fileNameController.text.isNotEmpty ? _fileNameController.text : "File Editor",
                style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 16),
              ),
        bottom: (isMarkdown || isImage)
            ? TabBar(
                controller: _tabController,
                indicatorColor: AppTheme.primaryCyan,
                labelColor: AppTheme.primaryCyan,
                unselectedLabelColor: AppTheme.textSecondary,
                tabs: const [
                  Tab(text: "Editor"),
                  Tab(text: "Preview"),
                ],
              )
            : null,
        actions: [
          IconButton(
            icon: Icon(_isSearchVisible ? Icons.search_off_rounded : Icons.search_rounded, color: AppTheme.primaryCyan),
            onPressed: () {
              setState(() {
                _isSearchVisible = !_isSearchVisible;
              });
            },
          ),
          Padding(
            padding: const EdgeInsets.only(right: 12),
            child: ElevatedButton.icon(
              onPressed: _handleSaveAndCommit,
              icon: const Icon(Icons.check_rounded, size: 18, color: Colors.black),
              label: Text("Commit", style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold)),
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
              ),
            ),
          ),
        ],
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator(color: AppTheme.primaryCyan))
          : _errorMsg != null
              ? Center(
                  child: Padding(
                    padding: const EdgeInsets.all(20),
                    child: Text(_errorMsg!, style: GoogleFonts.inter(color: AppTheme.dangerRed)),
                  ),
                )
              : Column(
                  children: [
                    // Search Bar if toggled
                    if (_isSearchVisible)
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                        color: AppTheme.surfaceBg,
                        child: TextField(
                          controller: _searchController,
                          onChanged: (q) => setState(() => _searchQuery = q.toLowerCase()),
                          style: GoogleFonts.inter(color: AppTheme.textPrimary, fontSize: 14),
                          decoration: const InputDecoration(
                            hintText: "Search in file...",
                            prefixIcon: Icon(Icons.search_rounded, color: AppTheme.primaryCyan),
                          ),
                        ),
                      ),

                    // Main View Editor / Preview Tab Switch
                    Expanded(
                      child: (isMarkdown || isImage)
                          ? TabBarView(
                              controller: _tabController,
                              children: [
                                _buildCodeEditorWidget(lang),
                                isMarkdown
                                    ? _buildMarkdownPreview()
                                    : _buildImagePreview(),
                              ],
                            )
                          : _buildCodeEditorWidget(lang),
                    ),
                  ],
                ),
    );
  }

  Widget _buildCodeEditorWidget(String lang) {
    final lines = _codeController.text.split('\n');

    return Container(
      color: const Color(0xFF0D1117),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Line Numbers Gutter
          Container(
            width: 42,
            padding: const EdgeInsets.only(top: 12),
            color: const Color(0xFF161B22),
            child: ListView.builder(
              itemCount: lines.length > 0 ? lines.length : 1,
              itemBuilder: (ctx, idx) {
                return Padding(
                  padding: const EdgeInsets.symmetric(vertical: 2),
                  child: Text(
                    "${idx + 1}",
                    style: GoogleFonts.jetBrainsMono(
                      fontSize: 12,
                      color: AppTheme.textSecondary,
                    ),
                    textAlign: TextAlign.center,
                  ),
                );
              },
            ),
          ),
          const VerticalDivider(width: 1, color: AppTheme.borderDark),

          // Code Input Editor Box
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(12),
              child: TextField(
                controller: _codeController,
                maxLines: null,
                keyboardType: TextInputType.multiline,
                style: GoogleFonts.jetBrainsMono(
                  fontSize: 13,
                  color: AppTheme.textPrimary,
                  height: 1.4,
                ),
                decoration: const InputDecoration(
                  border: InputBorder.none,
                  enabledBorder: InputBorder.none,
                  focusedBorder: InputBorder.none,
                  fillColor: Colors.transparent,
                  hintText: "Write or paste code here...",
                ),
                onChanged: (_) => setState(() {}),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildMarkdownPreview() {
    return Container(
      color: AppTheme.darkBg,
      padding: const EdgeInsets.all(16),
      child: Markdown(
        data: _codeController.text.isNotEmpty ? _codeController.text : "*No content to preview*",
        styleSheet: MarkdownStyleSheet.fromTheme(Theme.of(context)).copyWith(
          p: GoogleFonts.inter(color: AppTheme.textPrimary, fontSize: 14),
          h1: GoogleFonts.inter(color: AppTheme.primaryCyan, fontSize: 22, fontWeight: FontWeight.bold),
          h2: GoogleFonts.inter(color: AppTheme.secondaryTeal, fontSize: 18, fontWeight: FontWeight.bold),
          code: GoogleFonts.jetBrainsMono(backgroundColor: AppTheme.surfaceBg, color: AppTheme.primaryCyan),
        ),
      ),
    );
  }

  Widget _buildImagePreview() {
    if (_fileDetail?.contentB64 != null && _fileDetail!.contentB64!.isNotEmpty) {
      try {
        final bytes = base64Decode(_fileDetail!.contentB64!.replaceAll(RegExp(r'\s+'), ''));
        return Center(
          child: InteractiveViewer(
            child: Image.memory(bytes),
          ),
        );
      } catch (e) {
        return Center(child: Text("Error rendering image: $e"));
      }
    }
    return Center(child: Text("No image preview available.", style: GoogleFonts.inter(color: AppTheme.textSecondary)));
  }
}
