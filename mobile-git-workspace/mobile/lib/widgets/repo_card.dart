import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:intl/intl.dart';
import '../models/repository.dart';
import '../theme/app_theme.dart';

class RepoCard extends StatelessWidget {
  final Repository repo;
  final VoidCallback onTap;

  const RepoCard({
    super.key,
    required this.repo,
    required this.onTap,
  });

  String _formatDate(String isoString) {
    if (isoString.isEmpty) return "Recently";
    try {
      final dt = DateTime.parse(isoString);
      final now = DateTime.now();
      final diff = now.difference(dt);
      if (diff.inDays == 0) return "Today";
      if (diff.inDays == 1) return "Yesterday";
      if (diff.inDays < 30) return "${diff.inDays} days ago";
      return DateFormat('MMM d, yyyy').format(dt);
    } catch (_) {
      return isoString;
    }
  }

  Future<void> _launchUrl(String url) async {
    final uri = Uri.parse(url);
    if (await canLaunchUrl(uri)) {
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Header: Name & Public/Private Badge
              Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  const Icon(Icons.book_outlined, color: AppTheme.primaryCyan, size: 20),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Text(
                      repo.name,
                      style: GoogleFonts.inter(
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                        color: AppTheme.textPrimary,
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                  const SizedBox(width: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                    decoration: BoxDecoration(
                      color: repo.private ? AppTheme.warningOrange.withOpacity(0.15) : AppTheme.primaryCyan.withOpacity(0.15),
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(
                        color: repo.private ? AppTheme.warningOrange : AppTheme.primaryCyan,
                        width: 0.8,
                      ),
                    ),
                    child: Text(
                      repo.private ? "Private" : "Public",
                      style: GoogleFonts.inter(
                        fontSize: 11,
                        fontWeight: FontWeight.w600,
                        color: repo.private ? AppTheme.warningOrange : AppTheme.primaryCyan,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 8),

              // Description
              if (repo.description.isNotEmpty) ...[
                Text(
                  repo.description,
                  style: GoogleFonts.inter(
                    fontSize: 13,
                    color: AppTheme.textSecondary,
                    height: 1.3,
                  ),
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                ),
                const SizedBox(height: 12),
              ],

              // Meta row: Branch, Updated info, Language
              Row(
                children: [
                  const Icon(Icons.alt_route_rounded, size: 14, color: AppTheme.textSecondary),
                  const SizedBox(width: 4),
                  Text(
                    repo.defaultBranch,
                    style: GoogleFonts.inter(fontSize: 12, color: AppTheme.textSecondary),
                  ),
                  const SizedBox(width: 16),
                  if (repo.language != null) ...[
                    Container(
                      width: 8,
                      height: 8,
                      decoration: const BoxDecoration(
                        color: AppTheme.secondaryTeal,
                        shape: BoxShape.circle,
                      ),
                    ),
                    const SizedBox(width: 6),
                    Text(
                      repo.language!,
                      style: GoogleFonts.inter(fontSize: 12, color: AppTheme.textSecondary),
                    ),
                    const SizedBox(width: 16),
                  ],
                  const Icon(Icons.access_time_rounded, size: 14, color: AppTheme.textSecondary),
                  const SizedBox(width: 4),
                  Expanded(
                    child: Text(
                      _formatDate(repo.updatedAt),
                      style: GoogleFonts.inter(fontSize: 12, color: AppTheme.textSecondary),
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 14),

              // Action Buttons: Open Live Demo (if exists) & Open on GitHub
              Row(
                children: [
                  if (repo.hasPages || repo.pagesUrl != null) ...[
                    Expanded(
                      child: OutlinedButton.icon(
                        onPressed: () {
                          final url = repo.pagesUrl ?? "https://${repo.owner}.github.io/${repo.name}";
                          _launchUrl(url);
                        },
                        icon: const Icon(Icons.language_rounded, size: 16),
                        label: const Text("Open Live Demo"),
                        style: OutlinedButton.styleFrom(
                          padding: const EdgeInsets.symmetric(vertical: 8),
                          foregroundColor: AppTheme.secondaryTeal,
                          side: const BorderSide(color: AppTheme.secondaryTeal),
                        ),
                      ),
                    ),
                    const SizedBox(width: 8),
                  ],
                  Expanded(
                    child: OutlinedButton.icon(
                      onPressed: () => _launchUrl(repo.htmlUrl),
                      icon: const Icon(Icons.open_in_new_rounded, size: 16),
                      label: const Text("Open on GitHub"),
                      style: OutlinedButton.styleFrom(
                        padding: const EdgeInsets.symmetric(vertical: 8),
                        foregroundColor: AppTheme.primaryCyan,
                        side: const BorderSide(color: AppTheme.borderDark),
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
