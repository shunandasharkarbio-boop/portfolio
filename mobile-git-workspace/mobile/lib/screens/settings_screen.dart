import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import '../services/auth_service.dart';
import '../services/api_service.dart';
import '../theme/app_theme.dart';

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  late TextEditingController _branchCtrl;
  late TextEditingController _commitMsgCtrl;
  late TextEditingController _backendUrlCtrl;

  @override
  void initState() {
    super.initState();
    final auth = Provider.of<AuthService>(context, listen: false);
    _branchCtrl = TextEditingController(text: auth.defaultBranch);
    _commitMsgCtrl = TextEditingController(text: auth.defaultCommitMessageTemplate);
    _backendUrlCtrl = TextEditingController(text: ApiService.backendBaseUrl);
  }

  @override
  void dispose() {
    _branchCtrl.dispose();
    _commitMsgCtrl.dispose();
    _backendUrlCtrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final auth = Provider.of<AuthService>(context);
    final user = auth.user;

    return Scaffold(
      backgroundColor: AppTheme.darkBg,
      appBar: AppBar(
        title: Text("Settings", style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Account Profile Section
            Text("GitHub Account", style: GoogleFonts.inter(fontSize: 14, fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
            const SizedBox(height: 10),
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: AppTheme.cardBg,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: AppTheme.borderDark),
              ),
              child: Row(
                children: [
                  CircleAvatar(
                    radius: 28,
                    backgroundColor: AppTheme.primaryCyan,
                    backgroundImage: (user?.avatarUrl != null && user!.avatarUrl.isNotEmpty)
                        ? NetworkImage(user.avatarUrl)
                        : null,
                    child: (user?.avatarUrl == null || user!.avatarUrl.isEmpty)
                        ? Text(
                            (user?.login.isNotEmpty == true) ? user!.login[0].toUpperCase() : 'U',
                            style: GoogleFonts.inter(fontWeight: FontWeight.bold, color: Colors.black, fontSize: 22),
                          )
                        : null,
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          user?.name ?? user?.login ?? "Developer",
                          style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
                        ),
                        if (user?.login != null)
                          Text("@${user!.login}", style: GoogleFonts.inter(fontSize: 12, color: AppTheme.primaryCyan)),
                        const SizedBox(height: 4),
                        Text(
                          "Public repos: ${user?.publicRepos ?? 0} • Private repos: ${user?.totalPrivateRepos ?? 0}",
                          style: GoogleFonts.inter(fontSize: 11, color: AppTheme.textSecondary),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),

            // Workspace Preferences Section
            Text("Workspace Preferences", style: GoogleFonts.inter(fontSize: 14, fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
            const SizedBox(height: 10),
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: AppTheme.cardBg,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: AppTheme.borderDark),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text("Default Branch Preference", style: GoogleFonts.inter(fontSize: 13, color: AppTheme.textSecondary)),
                  const SizedBox(height: 6),
                  TextField(
                    controller: _branchCtrl,
                    style: GoogleFonts.inter(color: AppTheme.textPrimary, fontSize: 14),
                    decoration: const InputDecoration(hintText: "main"),
                    onChanged: (val) {
                      auth.updatePreferences(defaultBranch: val.trim());
                    },
                  ),
                  const SizedBox(height: 14),
                  Text("Default Commit Message Template", style: GoogleFonts.inter(fontSize: 13, color: AppTheme.textSecondary)),
                  const SizedBox(height: 6),
                  TextField(
                    controller: _commitMsgCtrl,
                    style: GoogleFonts.inter(color: AppTheme.textPrimary, fontSize: 14),
                    decoration: const InputDecoration(hintText: "Update {file} via Mobile Git Workspace"),
                    onChanged: (val) {
                      auth.updatePreferences(defaultCommitMsg: val.trim());
                    },
                  ),
                  const SizedBox(height: 14),
                  Text("Backend Server URL", style: GoogleFonts.inter(fontSize: 13, color: AppTheme.textSecondary)),
                  const SizedBox(height: 6),
                  TextField(
                    controller: _backendUrlCtrl,
                    style: GoogleFonts.jetBrainsMono(color: AppTheme.textPrimary, fontSize: 13),
                    decoration: const InputDecoration(hintText: "http://localhost:8000"),
                    onChanged: (val) {
                      ApiService.backendBaseUrl = val.trim();
                    },
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),

            // App Information Section
            Text("Application Information", style: GoogleFonts.inter(fontSize: 14, fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
            const SizedBox(height: 10),
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: AppTheme.cardBg,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: AppTheme.borderDark),
              ),
              child: Column(
                children: [
                  _buildInfoRow("App Name", "Mobile Git Workspace"),
                  const Divider(color: AppTheme.borderDark, height: 16),
                  _buildInfoRow("Version", "1.0.0 (Production)"),
                  const Divider(color: AppTheme.borderDark, height: 16),
                  _buildInfoRow("Architecture", "Flutter Mobile + FastAPI Backend"),
                  const Divider(color: AppTheme.borderDark, height: 16),
                  _buildInfoRow("GitHub REST API", "Active v3 Integration"),
                ],
              ),
            ),
            const SizedBox(height: 28),

            // Logout Button
            SizedBox(
              width: double.infinity,
              height: 50,
              child: OutlinedButton.icon(
                onPressed: () async {
                  await auth.logout();
                },
                icon: const Icon(Icons.logout_rounded, color: AppTheme.dangerRed),
                label: Text("Logout from Mobile Git Workspace", style: GoogleFonts.inter(color: AppTheme.dangerRed, fontWeight: FontWeight.bold)),
                style: OutlinedButton.styleFrom(
                  side: const BorderSide(color: AppTheme.dangerRed),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildInfoRow(String label, String value) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Text(label, style: GoogleFonts.inter(fontSize: 13, color: AppTheme.textSecondary)),
        Text(value, style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
      ],
    );
  }
}
