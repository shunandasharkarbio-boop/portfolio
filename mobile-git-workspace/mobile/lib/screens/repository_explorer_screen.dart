import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import '../services/auth_service.dart';
import '../services/api_service.dart';
import '../services/activity_service.dart';
import '../providers/app_provider.dart';
import '../widgets/file_icon.dart';
import '../widgets/pre_commit_dialog.dart';
import '../theme/app_theme.dart';
import 'code_editor_screen.dart';
import 'upload_screen.dart';

class RepositoryExplorerScreen extends StatelessWidget {
  const RepositoryExplorerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final auth = Provider.of<AuthService>(context);
    final appProv = Provider.of<AppProvider>(context);
    final repo = appProv.selectedRepo;

    if (repo == null) {
      return Scaffold(
        backgroundColor: AppTheme.darkBg,
        appBar: AppBar(title: const Text("Repository Explorer")),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(Icons.folder_off_rounded, color: AppTheme.textSecondary, size: 48),
              const SizedBox(height: 12),
              Text("No repository selected.", style: GoogleFonts.inter(color: AppTheme.textSecondary)),
              const SizedBox(height: 16),
              ElevatedButton(
                onPressed: () => appProv.setTabIndex(1),
                child: const Text("Choose Repository"),
              ),
            ],
          ),
        ),
      );
    }

    return Scaffold(
      backgroundColor: AppTheme.darkBg,
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              repo.name,
              style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 16),
            ),
            Text(
              repo.owner,
              style: GoogleFonts.inter(fontSize: 11, color: AppTheme.textSecondary),
            ),
          ],
        ),
        actions: [
          // Branch Switcher Badge Button
          Padding(
            padding: const EdgeInsets.only(right: 8),
            child: ActionChip(
              avatar: const Icon(Icons.alt_route_rounded, size: 14, color: Colors.black),
              label: Text(
                appProv.currentBranch,
                style: GoogleFonts.inter(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.black),
              ),
              backgroundColor: AppTheme.primaryCyan,
              onPressed: () => _showBranchSelectorModal(context, auth.token!),
            ),
          ),
          IconButton(
            icon: const Icon(Icons.refresh_rounded, color: AppTheme.primaryCyan),
            onPressed: () {
              if (auth.token != null) appProv.refreshDirectoryContents(auth.token!);
            },
          ),
        ],
      ),
      body: Column(
        children: [
          // Folder Breadcrumbs Navigation Bar
          Container(
            width: double.infinity,
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
            color: AppTheme.cardBg,
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Row(
                children: [
                  InkWell(
                    onTap: () {
                      if (auth.token != null) appProv.jumpToBreadcrumb(auth.token!, -1);
                    },
                    child: Row(
                      children: [
                        const Icon(Icons.home_rounded, size: 16, color: AppTheme.primaryCyan),
                        const SizedBox(width: 4),
                        Text(repo.name, style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.primaryCyan)),
                      ],
                    ),
                  ),
                  for (int i = 0; i < appProv.pathSegments.length; i++) ...[
                    const Padding(
                      padding: EdgeInsets.symmetric(horizontal: 4),
                      child: Icon(Icons.chevron_right_rounded, size: 16, color: AppTheme.textSecondary),
                    ),
                    InkWell(
                      onTap: () {
                        if (auth.token != null) appProv.jumpToBreadcrumb(auth.token!, i);
                      },
                      child: Text(
                        appProv.pathSegments[i],
                        style: GoogleFonts.inter(
                          fontSize: 13,
                          fontWeight: (i == appProv.pathSegments.length - 1) ? FontWeight.bold : FontWeight.w500,
                          color: (i == appProv.pathSegments.length - 1) ? AppTheme.textPrimary : AppTheme.secondaryTeal,
                        ),
                      ),
                    ),
                  ],
                ],
              ),
            ),
          ),

          // Main Directory Content List
          Expanded(
            child: appProv.isLoadingExplorer
                ? const Center(child: CircularProgressIndicator(color: AppTheme.primaryCyan))
                : appProv.explorerError != null
                    ? Center(
                        child: Padding(
                          padding: const EdgeInsets.all(20),
                          child: Text(appProv.explorerError!, style: GoogleFonts.inter(color: AppTheme.dangerRed)),
                        ),
                      )
                    : appProv.currentDirectoryItems.isEmpty
                        ? Center(
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                const Icon(Icons.folder_open_outlined, size: 48, color: AppTheme.textSecondary),
                                const SizedBox(height: 12),
                                Text("This folder is empty.", style: GoogleFonts.inter(color: AppTheme.textSecondary)),
                              ],
                            ),
                          )
                        : RefreshIndicator(
                            onRefresh: () async {
                              if (auth.token != null) await appProv.refreshDirectoryContents(auth.token!);
                            },
                            color: AppTheme.primaryCyan,
                            child: ListView.separated(
                              padding: const EdgeInsets.symmetric(vertical: 8),
                              itemCount: (appProv.pathSegments.isNotEmpty ? 1 : 0) + appProv.currentDirectoryItems.length,
                              separatorBuilder: (_, __) => const Divider(color: AppTheme.borderDark, height: 1),
                              itemBuilder: (ctx, idx) {
                                // ".." Go up folder item
                                if (appProv.pathSegments.isNotEmpty && idx == 0) {
                                  return ListTile(
                                    leading: const Icon(Icons.drive_file_move_rtl_outlined, color: AppTheme.primaryCyan, size: 22),
                                    title: Text(".. (Go Back)", style: GoogleFonts.inter(fontSize: 14, fontWeight: FontWeight.w600, color: AppTheme.primaryCyan)),
                                    onTap: () {
                                      if (auth.token != null) appProv.navigateUpFolder(auth.token!);
                                    },
                                  );
                                }

                                final itemIndex = appProv.pathSegments.isNotEmpty ? idx - 1 : idx;
                                final item = appProv.currentDirectoryItems[itemIndex];

                                return ListTile(
                                  leading: FileTypeIcon(fileName: item.name, isDirectory: item.isDirectory),
                                  title: Text(
                                    item.name,
                                    style: GoogleFonts.inter(
                                      fontSize: 14,
                                      fontWeight: item.isDirectory ? FontWeight.bold : FontWeight.w500,
                                      color: AppTheme.textPrimary,
                                    ),
                                  ),
                                  subtitle: item.isDirectory
                                      ? null
                                      : Text(item.formattedSize, style: GoogleFonts.inter(fontSize: 11, color: AppTheme.textSecondary)),
                                  trailing: item.isDirectory
                                      ? const Icon(Icons.chevron_right_rounded, color: AppTheme.textSecondary, size: 20)
                                      : IconButton(
                                          icon: const Icon(Icons.more_vert_rounded, color: AppTheme.textSecondary, size: 20),
                                          onPressed: () => _showFileActionMenu(context, auth.token!, repo.owner, repo.name, item, appProv.currentBranch),
                                        ),
                                  onTap: () {
                                    if (item.isDirectory) {
                                      if (auth.token != null) appProv.navigateIntoFolder(auth.token!, item.name);
                                    } else {
                                      // Open file editor/preview
                                      Navigator.push(
                                        context,
                                        MaterialPageRoute(
                                          builder: (_) => CodeEditorScreen(
                                            repoOwner: repo.owner,
                                            repoName: repo.name,
                                            filePath: item.path,
                                            initialBranch: appProv.currentBranch,
                                            fileSha: item.sha,
                                            isNewFile: false,
                                          ),
                                        ),
                                      );
                                    }
                                  },
                                );
                              },
                            ),
                          ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () => _showCreateOrUploadActionSheet(context, repo.owner, repo.name, appProv.currentFolderPath, appProv.currentBranch),
        icon: const Icon(Icons.add_rounded, color: Colors.black),
        label: Text("Action", style: GoogleFonts.inter(fontWeight: FontWeight.bold, color: Colors.black)),
        backgroundColor: AppTheme.primaryCyan,
      ),
    );
  }

  // File Options Action Menu (Edit / Delete)
  void _showFileActionMenu(BuildContext context, String token, String owner, String repoName, item, String branch) {
    showModalBottomSheet(
      context: context,
      backgroundColor: AppTheme.cardBg,
      shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
      builder: (ctx) => Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                FileTypeIcon(fileName: item.name, isDirectory: false),
                const SizedBox(width: 10),
                Expanded(
                  child: Text(
                    item.name,
                    style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            ListTile(
              leading: const Icon(Icons.edit_note_rounded, color: AppTheme.primaryCyan),
              title: Text("View / Edit File", style: GoogleFonts.inter(color: AppTheme.textPrimary)),
              onTap: () {
                Navigator.pop(ctx);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => CodeEditorScreen(
                      repoOwner: owner,
                      repoName: repoName,
                      filePath: item.path,
                      initialBranch: branch,
                      fileSha: item.sha,
                      isNewFile: false,
                    ),
                  ),
                );
              },
            ),
            ListTile(
              leading: const Icon(Icons.delete_forever_rounded, color: AppTheme.dangerRed),
              title: Text("Delete File", style: GoogleFonts.inter(color: AppTheme.dangerRed)),
              onTap: () {
                Navigator.pop(ctx);
                _confirmDeleteFile(context, token, owner, repoName, item, branch);
              },
            ),
          ],
        ),
      ),
    );
  }

  // Delete Confirmation Dialog with Commit System
  void _confirmDeleteFile(BuildContext context, String token, String owner, String repoName, item, String branch) {
    PreCommitDialog.show(
      context,
      repoName: repoName,
      branch: branch,
      changedFiles: ["DELETE: ${item.path}"],
      initialCommitMessage: "Delete ${item.name} via Mobile Git Workspace",
      onCommit: (commitMsg) async {
        await ApiService.deleteFile(
          token: token,
          owner: owner,
          repo: repoName,
          path: item.path,
          sha: item.sha,
          message: commitMsg,
          branch: branch,
        );

        final activity = Provider.of<ActivityService>(context, listen: false);
        activity.logActivity(
          actionType: "deleted",
          repoName: repoName,
          filePath: item.path,
          commitMessage: commitMsg,
          branch: branch,
        );

        final appProv = Provider.of<AppProvider>(context, listen: false);
        await appProv.refreshDirectoryContents(token);
      },
    );
  }

  // Create or Upload Action Sheet
  void _showCreateOrUploadActionSheet(BuildContext context, String owner, String repoName, String currentFolder, String branch) {
    showModalBottomSheet(
      context: context,
      backgroundColor: AppTheme.cardBg,
      shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
      builder: (ctx) => Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            ListTile(
              leading: const Icon(Icons.upload_file_rounded, color: AppTheme.primaryCyan, size: 24),
              title: Text("Upload Files From Phone", style: GoogleFonts.inter(fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
              subtitle: Text("Select documents/images from phone storage", style: GoogleFonts.inter(fontSize: 12, color: AppTheme.textSecondary)),
              onTap: () {
                Navigator.pop(ctx);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => UploadScreen(initialRepoOwner: owner, initialRepoName: repoName, initialFolder: currentFolder),
                  ),
                );
              },
            ),
            const Divider(color: AppTheme.borderDark),
            ListTile(
              leading: const Icon(Icons.note_add_rounded, color: AppTheme.secondaryTeal, size: 24),
              title: Text("Create New File", style: GoogleFonts.inter(fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
              subtitle: Text("Write code or text with mobile code editor", style: GoogleFonts.inter(fontSize: 12, color: AppTheme.textSecondary)),
              onTap: () {
                Navigator.pop(ctx);
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => CodeEditorScreen(
                      repoOwner: owner,
                      repoName: repoName,
                      initialBranch: branch,
                      initialFolder: currentFolder,
                      isNewFile: true,
                    ),
                  ),
                );
              },
            ),
            const Divider(color: AppTheme.borderDark),
            ListTile(
              leading: const Icon(Icons.create_new_folder_rounded, color: Colors.purpleAccent, size: 24),
              title: Text("Create New Folder", style: GoogleFonts.inter(fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
              subtitle: Text("Creates directory with initial .gitkeep", style: GoogleFonts.inter(fontSize: 12, color: AppTheme.textSecondary)),
              onTap: () {
                Navigator.pop(ctx);
                _showCreateFolderModal(context, owner, repoName, currentFolder, branch);
              },
            ),
          ],
        ),
      ),
    );
  }

  // Create Folder Modal
  void _showCreateFolderModal(BuildContext context, String owner, String repoName, String currentFolder, String branch) {
    final folderCtrl = TextEditingController();
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        backgroundColor: AppTheme.cardBg,
        title: Text("Create New Folder", style: GoogleFonts.inter(color: AppTheme.textPrimary, fontWeight: FontWeight.bold)),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            TextField(
              controller: folderCtrl,
              style: GoogleFonts.inter(color: AppTheme.textPrimary),
              decoration: InputDecoration(
                labelText: "Folder Name",
                prefixText: currentFolder.isNotEmpty ? "$currentFolder/" : "",
              ),
            ),
          ],
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(ctx), child: const Text("Cancel")),
          ElevatedButton(
            onPressed: () async {
              final newFolder = folderCtrl.text.trim();
              if (newFolder.isEmpty) return;
              Navigator.pop(ctx);

              final fullFolderPath = currentFolder.isNotEmpty ? "$currentFolder/$newFolder" : newFolder;
              final auth = Provider.of<AuthService>(context, listen: false);

              PreCommitDialog.show(
                context,
                repoName: repoName,
                branch: branch,
                changedFiles: ["NEW FOLDER: $fullFolderPath/"],
                initialCommitMessage: "Create folder $fullFolderPath via Mobile Git Workspace",
                onCommit: (commitMsg) async {
                  await ApiService.createFolder(
                    token: auth.token!,
                    owner: owner,
                    repo: repoName,
                    folderPath: fullFolderPath,
                    message: commitMsg,
                    branch: branch,
                  );

                  final activity = Provider.of<ActivityService>(context, listen: false);
                  activity.logActivity(
                    actionType: "created",
                    repoName: repoName,
                    filePath: "$fullFolderPath/",
                    commitMessage: commitMsg,
                    branch: branch,
                  );

                  final appProv = Provider.of<AppProvider>(context, listen: false);
                  await appProv.refreshDirectoryContents(auth.token!);
                },
              );
            },
            child: const Text("Create"),
          ),
        ],
      ),
    );
  }

  // Branch Switcher & Creation Modal
  void _showBranchSelectorModal(BuildContext context, String token) {
    final appProv = Provider.of<AppProvider>(context, listen: false);
    final repo = appProv.selectedRepo!;
    final newBranchCtrl = TextEditingController();

    showModalBottomSheet(
      context: context,
      backgroundColor: AppTheme.cardBg,
      shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(20))),
      builder: (ctx) => Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text("Select Branch", style: GoogleFonts.inter(fontSize: 18, fontWeight: FontWeight.bold, color: AppTheme.textPrimary)),
                IconButton(
                  icon: const Icon(Icons.add_rounded, color: AppTheme.primaryCyan),
                  onPressed: () {
                    showDialog(
                      context: ctx,
                      builder: (dialogCtx) => AlertDialog(
                        backgroundColor: AppTheme.cardBg,
                        title: Text("Create New Branch", style: GoogleFonts.inter(color: AppTheme.textPrimary)),
                        content: TextField(
                          controller: newBranchCtrl,
                          style: GoogleFonts.inter(color: AppTheme.textPrimary),
                          decoration: InputDecoration(hintText: "branch-name", prefixText: "From ${appProv.currentBranch}: "),
                        ),
                        actions: [
                          TextButton(onPressed: () => Navigator.pop(dialogCtx), child: const Text("Cancel")),
                          ElevatedButton(
                            onPressed: () async {
                              final name = newBranchCtrl.text.trim();
                              if (name.isNotEmpty) {
                                Navigator.pop(dialogCtx);
                                try {
                                  await ApiService.createBranch(
                                    token: token,
                                    owner: repo.owner,
                                    repo: repo.name,
                                    newBranch: name,
                                    baseBranch: appProv.currentBranch,
                                  );
                                  await appProv.loadBranches(token, repo.owner, repo.name);
                                  await appProv.switchBranch(token, name);

                                  final activity = Provider.of<ActivityService>(context, listen: false);
                                  activity.logActivity(
                                    actionType: "branch",
                                    repoName: repo.name,
                                    filePath: "heads/$name",
                                    commitMessage: "Created branch $name",
                                    branch: name,
                                  );

                                  Navigator.pop(ctx);
                                } catch (e) {
                                  ScaffoldMessenger.of(context).showSnackBar(
                                    SnackBar(content: Text("Failed to create branch: $e")),
                                  );
                                }
                              }
                            },
                            child: const Text("Create Branch"),
                          ),
                        ],
                      ),
                    );
                  },
                ),
              ],
            ),
            const Divider(color: AppTheme.borderDark),
            SizedBox(
              height: 200,
              child: ListView.builder(
                itemCount: appProv.branches.length,
                itemBuilder: (bCtx, idx) {
                  final b = appProv.branches[idx];
                  final isSelected = b.name == appProv.currentBranch;
                  return ListTile(
                    leading: Icon(
                      Icons.alt_route_rounded,
                      color: isSelected ? AppTheme.primaryCyan : AppTheme.textSecondary,
                    ),
                    title: Text(
                      b.name,
                      style: GoogleFonts.inter(
                        color: isSelected ? AppTheme.primaryCyan : AppTheme.textPrimary,
                        fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                      ),
                    ),
                    trailing: isSelected ? const Icon(Icons.check_rounded, color: AppTheme.primaryCyan) : null,
                    onTap: () {
                      appProv.switchBranch(token, b.name);
                      Navigator.pop(ctx);
                    },
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
