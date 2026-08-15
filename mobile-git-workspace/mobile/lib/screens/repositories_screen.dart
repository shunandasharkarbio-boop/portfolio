import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import '../services/auth_service.dart';
import '../providers/app_provider.dart';
import '../widgets/repo_card.dart';
import '../theme/app_theme.dart';
import 'repository_explorer_screen.dart';

class RepositoriesScreen extends StatefulWidget {
  const RepositoriesScreen({super.key});

  @override
  State<RepositoriesScreen> createState() => _RepositoriesScreenState();
}

class _RepositoriesScreenState extends State<RepositoriesScreen> {
  final TextEditingController _searchController = TextEditingController();

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final auth = Provider.of<AuthService>(context, listen: false);
      final appProv = Provider.of<AppProvider>(context, listen: false);
      if (auth.token != null) {
        appProv.loadRepositories(auth.token!);
      }
    });
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final auth = Provider.of<AuthService>(context);
    final appProv = Provider.of<AppProvider>(context);

    // Filter repos by search query
    final query = _searchController.text.trim().toLowerCase();
    final filteredRepos = query.isEmpty
        ? appProv.repositories
        : appProv.repositories.where((r) {
            return r.name.toLowerCase().contains(query) ||
                r.description.toLowerCase().contains(query);
          }).toList();

    return Scaffold(
      backgroundColor: AppTheme.darkBg,
      appBar: AppBar(
        title: Text("Repositories", style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh_rounded, color: AppTheme.primaryCyan),
            onPressed: () {
              if (auth.token != null) {
                appProv.loadRepositories(auth.token!, force: true);
              }
            },
          ),
        ],
      ),
      body: Column(
        children: [
          // Search Input Bar
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
            child: TextField(
              controller: _searchController,
              onChanged: (_) => setState(() {}),
              style: GoogleFonts.inter(color: AppTheme.textPrimary, fontSize: 14),
              decoration: InputDecoration(
                hintText: "Search repositories...",
                prefixIcon: const Icon(Icons.search_rounded, color: AppTheme.primaryCyan),
                suffixIcon: _searchController.text.isNotEmpty
                    ? IconButton(
                        icon: const Icon(Icons.clear_rounded, color: AppTheme.textSecondary),
                        onPressed: () {
                          _searchController.clear();
                          setState(() {});
                        },
                      )
                    : null,
              ),
            ),
          ),

          // Repo List
          Expanded(
            child: appProv.isLoadingRepos
                ? const Center(
                    child: CircularProgressIndicator(color: AppTheme.primaryCyan),
                  )
                : appProv.reposError != null
                    ? Center(
                        child: Padding(
                          padding: const EdgeInsets.all(20),
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              const Icon(Icons.error_outline_rounded, color: AppTheme.dangerRed, size: 42),
                              const SizedBox(height: 12),
                              Text(
                                appProv.reposError!,
                                style: GoogleFonts.inter(color: AppTheme.textSecondary, fontSize: 14),
                                textAlign: TextAlign.center,
                              ),
                              const SizedBox(height: 16),
                              ElevatedButton(
                                onPressed: () {
                                  if (auth.token != null) {
                                    appProv.loadRepositories(auth.token!, force: true);
                                  }
                                },
                                child: const Text("Retry"),
                              ),
                            ],
                          ),
                        ),
                      )
                    : filteredRepos.isEmpty
                        ? Center(
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                const Icon(Icons.folder_open_rounded, color: AppTheme.textSecondary, size: 48),
                                const SizedBox(height: 12),
                                Text(
                                  query.isEmpty ? "No repositories found." : "No matching repositories.",
                                  style: GoogleFonts.inter(color: AppTheme.textSecondary, fontSize: 14),
                                ),
                              ],
                            ),
                          )
                        : RefreshIndicator(
                            onRefresh: () async {
                              if (auth.token != null) {
                                await appProv.loadRepositories(auth.token!, force: true);
                              }
                            },
                            color: AppTheme.primaryCyan,
                            child: ListView.builder(
                              padding: const EdgeInsets.all(16),
                              itemCount: filteredRepos.length,
                              itemBuilder: (ctx, idx) {
                                final repo = filteredRepos[idx];
                                return RepoCard(
                                  repo: repo,
                                  onTap: () async {
                                    if (auth.token != null) {
                                      await appProv.selectRepository(auth.token!, repo);
                                      if (mounted) {
                                        Navigator.push(
                                          context,
                                          MaterialPageRoute(
                                            builder: (_) => const RepositoryExplorerScreen(),
                                          ),
                                        );
                                      }
                                    }
                                  },
                                );
                              },
                            ),
                          ),
          ),
        ],
      ),
    );
  }
}
