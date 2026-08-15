import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import '../services/auth_service.dart';
import '../providers/app_provider.dart';
import '../widgets/repo_card.dart';
import '../theme/app_theme.dart';
import 'repository_explorer_screen.dart';

class SearchScreen extends StatefulWidget {
  const SearchScreen({super.key});

  @override
  State<SearchScreen> createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  final TextEditingController _searchCtrl = TextEditingController();

  @override
  void dispose() {
    _searchCtrl.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final auth = Provider.of<AuthService>(context);
    final appProv = Provider.of<AppProvider>(context);

    final query = _searchCtrl.text.trim().toLowerCase();
    final matchingRepos = query.isEmpty
        ? []
        : appProv.repositories.where((r) {
            return r.name.toLowerCase().contains(query) ||
                r.description.toLowerCase().contains(query) ||
                r.owner.toLowerCase().contains(query);
          }).toList();

    return Scaffold(
      backgroundColor: AppTheme.darkBg,
      appBar: AppBar(
        title: Text("Search Workspace", style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16),
            child: TextField(
              controller: _searchCtrl,
              autofocus: true,
              onChanged: (_) => setState(() {}),
              style: GoogleFonts.inter(color: AppTheme.textPrimary, fontSize: 14),
              decoration: InputDecoration(
                hintText: "Search repositories, files, or paths...",
                prefixIcon: const Icon(Icons.search_rounded, color: AppTheme.primaryCyan),
                suffixIcon: _searchCtrl.text.isNotEmpty
                    ? IconButton(
                        icon: const Icon(Icons.clear_rounded, color: AppTheme.textSecondary),
                        onPressed: () {
                          _searchCtrl.clear();
                          setState(() {});
                        },
                      )
                    : null,
              ),
            ),
          ),
          Expanded(
            child: query.isEmpty
                ? Center(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        const Icon(Icons.search_rounded, size: 64, color: AppTheme.textSecondary),
                        const SizedBox(height: 14),
                        Text(
                          "Type to search across your GitHub account",
                          style: GoogleFonts.inter(color: AppTheme.textSecondary, fontSize: 14),
                        ),
                      ],
                    ),
                  )
                : matchingRepos.isEmpty
                    ? Center(
                        child: Text(
                          "No results found for '$query'",
                          style: GoogleFonts.inter(color: AppTheme.textSecondary, fontSize: 14),
                        ),
                      )
                    : ListView.builder(
                        padding: const EdgeInsets.symmetric(horizontal: 16),
                        itemCount: matchingRepos.length,
                        itemBuilder: (ctx, idx) {
                          final repo = matchingRepos[idx];
                          return RepoCard(
                            repo: repo,
                            onTap: () async {
                              if (auth.token != null) {
                                await appProv.selectRepository(auth.token!, repo);
                                if (mounted) {
                                  Navigator.push(
                                    context,
                                    MaterialPageRoute(builder: (_) => const RepositoryExplorerScreen()),
                                  );
                                }
                              }
                            },
                          );
                        },
                      ),
          ),
        ],
      ),
    );
  }
}
