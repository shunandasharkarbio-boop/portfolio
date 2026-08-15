import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import 'package:intl/intl.dart';
import '../services/activity_service.dart';
import '../models/activity_item.dart';
import '../theme/app_theme.dart';

class ActivityScreen extends StatelessWidget {
  const ActivityScreen({super.key});

  String _formatTimestamp(String isoString) {
    if (isoString.isEmpty) return "";
    try {
      final dt = DateTime.parse(isoString);
      final diff = DateTime.now().difference(dt);
      if (diff.inMinutes < 1) return "Just now";
      if (diff.inMinutes < 60) return "${diff.inMinutes}m ago";
      if (diff.inHours < 24) return "${diff.inHours}h ago";
      return DateFormat('MMM d, h:mm a').format(dt);
    } catch (_) {
      return isoString;
    }
  }

  IconData _getActionIcon(String type) {
    switch (type.toLowerCase()) {
      case 'uploaded': return Icons.cloud_upload_rounded;
      case 'created': return Icons.note_add_rounded;
      case 'updated': return Icons.edit_note_rounded;
      case 'deleted': return Icons.delete_forever_rounded;
      case 'branch': return Icons.alt_route_rounded;
      default: return Icons.history_rounded;
    }
  }

  Color _getActionColor(String type) {
    switch (type.toLowerCase()) {
      case 'uploaded': return AppTheme.primaryCyan;
      case 'created': return AppTheme.secondaryTeal;
      case 'updated': return AppTheme.warningOrange;
      case 'deleted': return AppTheme.dangerRed;
      case 'branch': return Colors.purpleAccent;
      default: return AppTheme.textPrimary;
    }
  }

  @override
  Widget build(BuildContext context) {
    final activityService = Provider.of<ActivityService>(context);
    final items = activityService.activities;

    return Scaffold(
      backgroundColor: AppTheme.darkBg,
      appBar: AppBar(
        title: Text("Recent Activity", style: GoogleFonts.inter(fontWeight: FontWeight.bold)),
        actions: [
          if (items.isNotEmpty)
            IconButton(
              icon: const Icon(Icons.delete_sweep_rounded, color: AppTheme.textSecondary),
              onPressed: () => activityService.clearActivities(),
            ),
        ],
      ),
      body: items.isEmpty
          ? Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Icon(Icons.history_toggle_off_rounded, size: 54, color: AppTheme.textSecondary),
                  const SizedBox(height: 14),
                  Text(
                    "No actions performed yet.",
                    style: GoogleFonts.inter(color: AppTheme.textSecondary, fontSize: 14),
                  ),
                  const SizedBox(height: 6),
                  Text(
                    "Files uploaded, created, or edited via the app will appear here.",
                    style: GoogleFonts.inter(color: AppTheme.textSecondary, fontSize: 12),
                    textAlign: TextAlign.center,
                  ),
                ],
              ),
            )
          : ListView.separated(
              padding: const EdgeInsets.all(16),
              itemCount: items.length,
              separatorBuilder: (_, __) => const SizedBox(height: 10),
              itemBuilder: (ctx, idx) {
                final item = items[idx];
                final icon = _getActionIcon(item.actionType);
                final color = _getActionColor(item.actionType);

                return Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(
                    color: AppTheme.cardBg,
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(color: AppTheme.borderDark),
                  ),
                  child: Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Container(
                        padding: const EdgeInsets.all(8),
                        decoration: BoxDecoration(
                          color: color.withOpacity(0.15),
                          shape: BoxShape.circle,
                        ),
                        child: Icon(icon, color: color, size: 20),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              mainAxisAlignment: MainAxisAlignment.spaceBetween,
                              children: [
                                Text(
                                  "${item.actionType.toUpperCase()} • ${item.repoName}",
                                  style: GoogleFonts.inter(fontSize: 12, fontWeight: FontWeight.bold, color: color),
                                ),
                                Text(
                                  _formatTimestamp(item.timestamp),
                                  style: GoogleFonts.inter(fontSize: 11, color: AppTheme.textSecondary),
                                ),
                              ],
                            ),
                            const SizedBox(height: 4),
                            Text(
                              item.filePath,
                              style: GoogleFonts.jetBrainsMono(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
                              overflow: TextOverflow.ellipsis,
                            ),
                            const SizedBox(height: 4),
                            Text(
                              "Commit: ${item.commitMessage}",
                              style: GoogleFonts.inter(fontSize: 12, color: AppTheme.textSecondary),
                              maxLines: 2,
                              overflow: TextOverflow.ellipsis,
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                );
              },
            ),
    );
  }
}
