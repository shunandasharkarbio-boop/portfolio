import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../theme/app_theme.dart';

class PreCommitDialog extends StatefulWidget {
  final String repoName;
  final String branch;
  final List<String> changedFiles;
  final String initialCommitMessage;
  final Future<void> Function(String commitMessage) onCommit;

  const PreCommitDialog({
    super.key,
    required this.repoName,
    required this.branch,
    required this.changedFiles,
    required this.initialCommitMessage,
    required this.onCommit,
  });

  static Future<bool?> show(
    BuildContext context, {
    required String repoName,
    required String branch,
    required List<String> changedFiles,
    required String initialCommitMessage,
    required Future<void> Function(String commitMessage) onCommit,
  }) {
    return showModalBottomSheet<bool>(
      context: context,
      isScrollControlled: true,
      backgroundColor: AppTheme.cardBg,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      builder: (ctx) => Padding(
        padding: EdgeInsets.only(
          bottom: MediaQuery.of(ctx).viewInsets.bottom,
        ),
        child: PreCommitDialog(
          repoName: repoName,
          branch: branch,
          changedFiles: changedFiles,
          initialCommitMessage: initialCommitMessage,
          onCommit: onCommit,
        ),
      ),
    );
  }

  @override
  State<PreCommitDialog> createState() => _PreCommitDialogState();
}

class _PreCommitDialogState extends State<PreCommitDialog> {
  late TextEditingController _controller;
  bool _isCommitting = false;
  String? _errorMessage;

  @override
  void initState() {
    super.initState();
    _controller = TextEditingController(text: widget.initialCommitMessage);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  Future<void> _handleCommit() async {
    final msg = _controller.text.trim();
    if (msg.isEmpty) {
      setState(() {
        _errorMessage = "Commit message cannot be empty.";
      });
      return;
    }

    setState(() {
      _isCommitting = true;
      _errorMessage = null;
    });

    try {
      await widget.onCommit(msg);
      if (mounted) {
        Navigator.of(context).pop(true);
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _isCommitting = false;
          _errorMessage = e.toString().replaceAll("Exception: ", "");
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Header Drag Handle
          Center(
            child: Container(
              width: 40,
              height: 4,
              decoration: BoxDecoration(
                color: AppTheme.borderDark,
                borderRadius: BorderRadius.circular(2),
              ),
            ),
          ),
          const SizedBox(height: 16),

          Row(
            children: [
              const Icon(Icons.commit_rounded, color: AppTheme.primaryCyan, size: 24),
              const SizedBox(width: 10),
              Text(
                "Confirm Commit",
                style: GoogleFonts.inter(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: AppTheme.textPrimary,
                ),
              ),
            ],
          ),
          const SizedBox(height: 16),
          const Divider(color: AppTheme.borderDark, height: 1),
          const SizedBox(height: 16),

          // Repository & Branch metadata
          _buildMetaRow(Icons.folder_outlined, "Repository", widget.repoName),
          const SizedBox(height: 10),
          _buildMetaRow(Icons.alt_route_rounded, "Branch", widget.branch),
          const SizedBox(height: 14),

          // Changed files summary list
          Text(
            "Changed files (${widget.changedFiles.length}):",
            style: GoogleFonts.inter(
              fontSize: 13,
              fontWeight: FontWeight.w600,
              color: AppTheme.textSecondary,
            ),
          ),
          const SizedBox(height: 6),
          Container(
            constraints: const BoxConstraints(maxHeight: 120),
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: AppTheme.surfaceBg,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: AppTheme.borderDark),
            ),
            child: ListView.builder(
              shrinkWrap: true,
              itemCount: widget.changedFiles.length,
              itemBuilder: (ctx, idx) {
                return Padding(
                  padding: const EdgeInsets.symmetric(vertical: 2),
                  child: Row(
                    children: [
                      const Icon(Icons.insert_drive_file_outlined, size: 14, color: AppTheme.primaryCyan),
                      const SizedBox(width: 6),
                      Expanded(
                        child: Text(
                          widget.changedFiles[idx],
                          style: GoogleFonts.jetBrainsMono(
                            fontSize: 12,
                            color: AppTheme.textPrimary,
                          ),
                          overflow: TextOverflow.ellipsis,
                        ),
                      ),
                    ],
                  ),
                );
              },
            ),
          ),
          const SizedBox(height: 16),

          // Commit message input field
          Text(
            "Commit message:",
            style: GoogleFonts.inter(
              fontSize: 13,
              fontWeight: FontWeight.w600,
              color: AppTheme.textSecondary,
            ),
          ),
          const SizedBox(height: 6),
          TextField(
            controller: _controller,
            maxLines: 2,
            style: GoogleFonts.inter(fontSize: 14, color: AppTheme.textPrimary),
            decoration: const InputDecoration(
              hintText: "Enter a descriptive commit message...",
            ),
          ),
          const SizedBox(height: 12),

          if (_errorMessage != null) ...[
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: AppTheme.dangerRed.withOpacity(0.15),
                borderRadius: BorderRadius.circular(8),
                border: Border.all(color: AppTheme.dangerRed),
              ),
              child: Row(
                children: [
                  const Icon(Icons.error_outline, color: AppTheme.dangerRed, size: 18),
                  const SizedBox(width: 8),
                  Expanded(
                    child: Text(
                      _errorMessage!,
                      style: GoogleFonts.inter(color: AppTheme.dangerRed, fontSize: 12),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 12),
          ],

          // Primary Commit Button
          SizedBox(
            width: double.infinity,
            height: 48,
            child: ElevatedButton(
              onPressed: _isCommitting ? null : _handleCommit,
              style: ElevatedButton.styleFrom(
                backgroundColor: AppTheme.primaryCyan,
                foregroundColor: Colors.black,
              ),
              child: _isCommitting
                  ? const SizedBox(
                      width: 22,
                      height: 22,
                      child: CircularProgressIndicator(
                        strokeWidth: 2.5,
                        color: Colors.black,
                      ),
                    )
                  : Text(
                      "[ Commit Changes ]",
                      style: GoogleFonts.inter(
                        fontSize: 15,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
            ),
          ),
          const SizedBox(height: 10),
        ],
      ),
    );
  }

  Widget _buildMetaRow(IconData icon, String label, String value) {
    return Row(
      children: [
        Icon(icon, size: 16, color: AppTheme.primaryCyan),
        const SizedBox(width: 8),
        Text(
          "$label: ",
          style: GoogleFonts.inter(fontSize: 13, color: AppTheme.textSecondary),
        ),
        Expanded(
          child: Text(
            value,
            style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
            overflow: TextOverflow.ellipsis,
          ),
        ),
      ],
    );
  }
}
