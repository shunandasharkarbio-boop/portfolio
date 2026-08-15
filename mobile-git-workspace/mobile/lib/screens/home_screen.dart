import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import '../services/auth_service.dart';
import '../services/api_service.dart';
import '../providers/app_provider.dart';
import '../widgets/repo_card.dart';
import '../models/commit_item.dart';
import '../theme/app_theme.dart';
import 'upload_screen.dart';
import 'code_editor_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  List<CommitItem> _recentCommits = [];
  bool _isLoadingCommits = false;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _loadHomeData();
    });
  }

  Future<void> _loadHomeData() async {
    final auth = Provider.of<AuthService>(context, listen: false);
    final appProv = Provider.of<AppProvider>(context, listen: false);

    if (auth.token != null) {
      await appProv.loadRepositories(auth.token!);
      if (appProv.repositories.isNotEmpty) {
        _loadRecentCommits(auth.token!, appProv.repositories.first);
      }
    }
  }

  Future<void> _loadRecentCommits(String token, repo) async {
    setState(() => _isLoadingCommits = true);
    try {
      final commits = await ApiService.fetchCommits(token, repo.owner, repo.name, branch: repo.defaultBranch);
      if (mounted) {
        setState(() => _recentCommits = commits.take(5).toList());
      }
    } catch (_) {
    } finally {
      if (mounted) setState(() => _isLoadingCommits = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    final auth = Provider.of<AuthService>(context);
    final appProv = Provider.of<AppProvider>(context);
    final user = auth.user;

    return Scaffold(
      backgroundColor: AppTheme.darkBg,
      appBar: AppBar(
        title: Row(
          children: [
            Container(
              width: 32,
              height: 32,
              decoration: const BoxDecoration(
                shape: BoxShape.circle,
                gradient: LinearGradient(colors: [AppTheme.primaryCyan, AppTheme.secondaryTeal]),
              ),
              child: const Icon(Icons.mobile_friendly, size: 18, color: Colors.black),
            ),
            const SizedBox(width: 10),
            Text(
              "Mobile Git Workspace",
              style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 16),
            ),
          ],
        ),
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh_rounded, color: AppTheme.primaryCyan),
            onPressed: () => _loadHomeData(),
          ),
        ],
      ),
      body: RefreshIndicator(
        onRefresh: _loadHomeData,
        color: AppTheme.primaryCyan,
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16),
          physics: const AlwaysScrollableScrollPhysics(),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Welcome Back Header
              Container(
                padding: const EdgeInsets.all(18),
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [
                      AppTheme.cardBg,
                      AppTheme.surfaceBg,
                    ],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: AppTheme.borderDark),
                ),
                child: Row(
                  children: [
                    CircleAvatar(
                      radius: 26,
                      backgroundColor: AppTheme.primaryCyan,
                      backgroundImage: (user?.avatarUrl != null && user!.avatarUrl.isNotEmpty)
                          ? NetworkImage(user.avatarUrl)
                          : null,
                      child: (user?.avatarUrl == null || user!.avatarUrl.isEmpty)
                          ? Text(
                              (user?.login.isNotEmpty == true) ? user!.login[0].toUpperCase() : 'U',
                              style: GoogleFonts.inter(fontWeight: FontWeight.bold, color: Colors.black, fontSize: 20),
                            )
                          : null,
                    ),
                    const SizedBox(width: 14),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            "Welcome back,",
                            style: GoogleFonts.inter(fontSize: 12, color: AppTheme.textSecondary),
                          ),
                          Text(
                            user?.name ?? user?.login ?? "Developer",
                            style: GoogleFonts.inter(fontSize: 18, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
                            overflow: TextOverflow.ellipsis,
                          ),
                          if (user?.login != null)
                            Text(
                              "@${user!.login}",
                              style: GoogleFonts.inter(fontSize: 12, color: AppTheme.primaryCyan),
                            ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 20),

              // Quick Actions Header
              Text(
                "Quick Actions",
                style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
              ),
              const SizedBox(height: 12),

              Row(
                children: [
                  Expanded(
                    child: _buildQuickActionCard(
                      icon: Icons.upload_file_rounded,
                      label: "+ Upload File",
                      color: AppTheme.primaryCyan,
                      onTap: () {
                        Navigator.push(context, MaterialPageRoute(builder: (_) => const UploadScreen()));
                      },
                    ),
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: _buildQuickActionCard(
                      icon: Icons.note_add_rounded,
                      label: "+ Create File",
                      color: AppTheme.secondaryTeal,
                      onTap: () {
                        if (appProv.selectedRepo != null) {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (_) => CodeEditorScreen(
                                repoOwner: appProv.selectedRepo!.owner,
                                repoName: appProv.selectedRepo!.name,
                                initialBranch: appProv.currentBranch,
                                initialFolder: appProv.currentFolderPath,
                                isNewFile: true,
                              ),
                            ),
                          );
                        } else {
                          appProv.setTabIndex(1); // Go to Repos tab
                        }
                      },
                    ),
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: _buildQuickActionCard(
                      icon: Icons.folder_copy_rounded,
                      label: "Repositories",
                      color: Colors.purpleAccent,
                      onTap: () => appProv.setTabIndex(1),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 24),

              // Recent Repositories Section
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    "Recent Repositories",
                    style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
                  ),
                  TextButton(
                    onPressed: () => appProv.setTabIndex(1),
                    child: Text("View All (${appProv.repositories.length})", style: GoogleFonts.inter(color: AppTheme.primaryCyan, fontSize: 13)),
                  ),
                ],
              ),
              const SizedBox(height: 8),

              if (appProv.isLoadingRepos)
                const Center(child: Padding(padding: EdgeInsets.all(20), child: CircularProgressIndicator(color: AppTheme.primaryCyan)))
              else if (appProv.repositories.isEmpty)
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    color: AppTheme.cardBg,
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(color: AppTheme.borderDark),
                  ),
                  child: Center(
                    child: Text("No repositories found.", style: GoogleFonts.inter(color: AppTheme.textSecondary)),
                  ),
                )
              else
                Column(
                  children: appProv.repositories.take(3).map((repo) {
                    return RepoCard(
                      repo: repo,
                      onTap: () {
                        if (auth.token != null) {
                          appProv.selectRepository(auth.token!, repo, targetTab: 1);
                        }
                      },
                    );
                  }).toList(),
                ),
              const SizedBox(height: 20),

              // Recent Commits Section
              if (appProv.selectedRepo != null) ...[
                Text(
                  "Recent Commits (${appProv.selectedRepo!.name})",
                  style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
                ),
                const SizedBox(height: 10),
                if (_isLoadingCommits)
                  const Center(child: Padding(padding: EdgeInsets.all(16), child: CircularProgressIndicator(color: AppTheme.primaryCyan)))
                else if (_recentCommits.isEmpty)
                  Text("No commit history found.", style: GoogleFonts.inter(color: AppTheme.textSecondary, fontSize: 13))
                else
                  Column(
                    children: _recentCommits.map((c) {
                      return Container(
                        margin: const EdgeInsets.only(bottom: 8),
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: AppTheme.cardBg,
                          borderRadius: BorderRadius.circular(10),
                          border: Border.all(color: AppTheme.borderDark),
                        ),
                        child: Row(
                          children: [
                            const Icon(Icons.commit_rounded, color: AppTheme.primaryCyan, size: 20),
                            const SizedBox(width: 10),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    c.message,
                                    style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.w600, color: AppTheme.textPrimary),
                                    maxLines: 1,
                                    overflow: TextOverflow.ellipsis,
                                  ),
                                  const SizedBox(height: 2),
                                  Text(
                                    "${c.authorName} • ${c.sha}",
                                    style: GoogleFonts.jetBrainsMono(fontSize: 11, color: AppTheme.textSecondary),
                                  ),
                                ],
                              ),
                            ),
                          ],
                        ),
                      );
                    }).toList(),
                  ),
              ],
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildQuickActionCard({
    required IconData icon,
    required String label,
    required Color color,
    required VoidCallback onTap,
  }) {
    return Card(
      color: AppTheme.cardBg,
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 16, horizontal: 8),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: color.withOpacity(0.15),
                  shape: BoxShape.circle,
                ),
                child: Icon(icon, color: color, size: 22),
              ),
              const SizedBox(height: 8),
              Text(
                label,
                style: GoogleFonts.inter(fontSize: 12, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
                textAlign: TextAlign.center,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
