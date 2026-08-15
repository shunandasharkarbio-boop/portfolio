import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import '../services/auth_service.dart';
import '../services/api_service.dart';
import '../services/activity_service.dart';
import '../providers/app_provider.dart';
import '../widgets/pre_commit_dialog.dart';
import '../theme/app_theme.dart';

class ChatMessage {
  final String text;
  final bool isUser;
  final String timestamp;
  final Map<String, dynamic>? proposedChange;

  ChatMessage({
    required this.text,
    required this.isUser,
    required this.timestamp,
    this.proposedChange,
  });
}

class AIAssistantScreen extends StatefulWidget {
  const AIAssistantScreen({super.key});

  @override
  State<AIAssistantScreen> createState() => _AIAssistantScreenState();
}

class _AIAssistantScreenState extends State<AIAssistantScreen> {
  final TextEditingController _promptCtrl = TextEditingController();
  final ScrollController _scrollCtrl = ScrollController();
  final List<ChatMessage> _messages = [];
  bool _isSending = false;

  @override
  void initState() {
    super.initState();
    _messages.add(
      ChatMessage(
        text: "Hello! I am your Portfolio AI Assistant. I can analyze your GitHub repositories, update your portfolio About section, propose code changes, or commit coursework files.",
        isUser: false,
        timestamp: "Now",
      ),
    );
  }

  @override
  void dispose() {
    _promptCtrl.dispose();
    _scrollCtrl.dispose();
    super.dispose();
  }

  Future<void> _sendPrompt(String text) async {
    final promptText = text.trim();
    if (promptText.isEmpty) return;

    final auth = Provider.of<AuthService>(context, listen: false);
    final appProv = Provider.of<AppProvider>(context, listen: false);
    final repo = appProv.selectedRepo;

    if (repo == null) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Please select a target repository first.")),
      );
      return;
    }

    setState(() {
      _messages.add(
        ChatMessage(text: promptText, isUser: true, timestamp: "Just now"),
      );
      _promptCtrl.clear();
      _isSending = true;
    });

    _scrollToBottom();

    try {
      final res = await ApiService.sendAIChatPrompt(
        token: auth.token!,
        prompt: promptText,
        owner: repo.owner,
        repo: repo.name,
        branch: appProv.currentBranch,
        currentPath: appProv.currentFolderPath,
      );

      final aiText = res["ai_response"] ?? "I analyzed your request.";

      if (mounted) {
        setState(() {
          _messages.add(
            ChatMessage(
              text: aiText,
              isUser: false,
              timestamp: "Just now",
              proposedChange: res["target_file"] != null ? res : null,
            ),
          );
          _isSending = false;
        });
        _scrollToBottom();
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _messages.add(
            ChatMessage(
              text: "Sorry, error processing AI request: $e",
              isUser: false,
              timestamp: "Just now",
            ),
          );
          _isSending = false;
        });
        _scrollToBottom();
      }
    }
  }

  void _scrollToBottom() {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (_scrollCtrl.hasClients) {
        _scrollCtrl.animateTo(
          _scrollCtrl.position.maxScrollExtent,
          duration: const Duration(milliseconds: 300),
          curve: Curves.easeOut,
        );
      }
    });
  }

  void _approveAndCommit(Map<String, dynamic> change) {
    final auth = Provider.of<AuthService>(context, listen: false);
    final appProv = Provider.of<AppProvider>(context, listen: false);
    final repo = appProv.selectedRepo!;

    final targetFile = change["target_file"] as String;
    final b64Content = change["proposed_content_b64"] as String;
    final suggestedMsg = change["suggested_commit_message"] ?? "AI Portfolio Update";

    PreCommitDialog.show(
      context,
      repoName: repo.name,
      branch: appProv.currentBranch,
      changedFiles: ["AI MODIFIED: $targetFile"],
      initialCommitMessage: suggestedMsg,
      onCommit: (commitMsg) async {
        await ApiService.commitFile(
          token: auth.token!,
          owner: repo.owner,
          repo: repo.name,
          path: targetFile,
          message: commitMsg,
          contentB64: b64Content,
          branch: appProv.currentBranch,
        );

        final activity = Provider.of<ActivityService>(context, listen: false);
        activity.logActivity(
          actionType: "updated",
          repoName: repo.name,
          filePath: targetFile,
          commitMessage: commitMsg,
          branch: appProv.currentBranch,
        );

        await appProv.refreshDirectoryContents(auth.token!);

        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              backgroundColor: AppTheme.successGreen,
              content: Text("AI Changes committed to ${repo.name}!"),
            ),
          );
        }
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final appProv = Provider.of<AppProvider>(context);
    final repo = appProv.selectedRepo;

    return Scaffold(
      backgroundColor: AppTheme.darkBg,
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                const Icon(Icons.auto_awesome_rounded, color: AppTheme.primaryCyan, size: 18),
                const SizedBox(width: 8),
                Text("Portfolio AI Assistant", style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 16)),
              ],
            ),
            if (repo != null)
              Text("Target: ${repo.fullName} (${appProv.currentBranch})", style: GoogleFonts.inter(fontSize: 11, color: AppTheme.textSecondary)),
          ],
        ),
      ),
      body: Column(
        children: [
          // Preset Prompt Action Chips
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
            color: AppTheme.cardBg,
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Row(
                children: [
                  _buildPresetChip("Change my portfolio About section", Icons.person_outline_rounded),
                  const SizedBox(width: 8),
                  _buildPresetChip("Analyze repository structure", Icons.analytics_outlined),
                  const SizedBox(width: 8),
                  _buildPresetChip("Review recent commits", Icons.commit_rounded),
                ],
              ),
            ),
          ),

          // Messages List
          Expanded(
            child: ListView.builder(
              controller: _scrollCtrl,
              padding: const EdgeInsets.all(16),
              itemCount: _messages.length,
              itemBuilder: (ctx, idx) {
                final msg = _messages[idx];
                return _buildMessageBubble(msg);
              },
            ),
          ),

          if (_isSending)
            const Padding(
              padding: EdgeInsets.symmetric(vertical: 8),
              child: SizedBox(
                width: 24,
                height: 24,
                child: CircularProgressIndicator(strokeWidth: 2, color: AppTheme.primaryCyan),
              ),
            ),

          // Input Box
          Container(
            padding: const EdgeInsets.all(12),
            color: AppTheme.cardBg,
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _promptCtrl,
                    style: GoogleFonts.inter(color: AppTheme.textPrimary, fontSize: 14),
                    decoration: const InputDecoration(
                      hintText: "Ask AI e.g. Change About section...",
                    ),
                    onSubmitted: (val) => _sendPrompt(val),
                  ),
                ),
                const SizedBox(width: 10),
                IconButton.filled(
                  style: IconButton.styleFrom(backgroundColor: AppTheme.primaryCyan),
                  icon: const Icon(Icons.send_rounded, color: Colors.black),
                  onPressed: () => _sendPrompt(_promptCtrl.text),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildPresetChip(String text, IconData icon) {
    return ActionChip(
      avatar: Icon(icon, size: 14, color: AppTheme.primaryCyan),
      label: Text(text, style: GoogleFonts.inter(fontSize: 12, color: AppTheme.textPrimary)),
      backgroundColor: AppTheme.surfaceBg,
      side: const BorderSide(color: AppTheme.borderDark),
      onPressed: () => _sendPrompt(text),
    );
  }

  Widget _buildMessageBubble(ChatMessage msg) {
    return Align(
      alignment: msg.isUser ? Alignment.centerRight : Alignment.centerLeft,
      child: Container(
        margin: const EdgeInsets.only(bottom: 12),
        constraints: BoxConstraints(maxWidth: MediaQuery.of(context).size.width * 0.85),
        padding: const EdgeInsets.all(14),
        decoration: BoxDecoration(
          color: msg.isUser ? AppTheme.primaryCyan.withOpacity(0.15) : AppTheme.cardBg,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: msg.isUser ? AppTheme.primaryCyan : AppTheme.borderDark,
            width: 1,
          ),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(
                  msg.isUser ? Icons.person_rounded : Icons.auto_awesome_rounded,
                  size: 14,
                  color: msg.isUser ? AppTheme.primaryCyan : AppTheme.secondaryTeal,
                ),
                const SizedBox(width: 6),
                Text(
                  msg.isUser ? "You" : "Portfolio AI Assistant",
                  style: GoogleFonts.inter(
                    fontSize: 11,
                    fontWeight: FontWeight.bold,
                    color: msg.isUser ? AppTheme.primaryCyan : AppTheme.secondaryTeal,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 6),
            Text(
              msg.text,
              style: GoogleFonts.inter(fontSize: 13, color: AppTheme.textPrimary, height: 1.3),
            ),

            // Proposed change card with Approve button
            if (msg.proposedChange != null) ...[
              const SizedBox(height: 12),
              Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: AppTheme.surfaceBg,
                  borderRadius: BorderRadius.circular(8),
                  border: Border.all(color: AppTheme.borderDark),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      "Proposed Change: ${msg.proposedChange!['target_file']}",
                      style: GoogleFonts.inter(fontSize: 12, fontWeight: FontWeight.bold, color: AppTheme.primaryCyan),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      msg.proposedChange!['diff_summary'] ?? "",
                      style: GoogleFonts.jetBrainsMono(fontSize: 11, color: AppTheme.textSecondary),
                    ),
                    const SizedBox(height: 10),
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton.icon(
                        onPressed: () => _approveAndCommit(msg.proposedChange!),
                        icon: const Icon(Icons.check_rounded, size: 16, color: Colors.black),
                        label: Text("Approve & Commit to GitHub", style: GoogleFonts.inter(fontSize: 12, fontWeight: FontWeight.bold)),
                        style: ElevatedButton.styleFrom(
                          padding: const EdgeInsets.symmetric(vertical: 8),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }
}
