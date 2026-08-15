import 'package:flutter/foundation.dart';
import '../models/repository.dart';
import '../models/file_item.dart';
import '../models/branch_info.dart';
import '../services/api_service.dart';

class AppProvider extends ChangeNotifier {
  int _currentTabIndex = 0;
  List<Repository> _repositories = [];
  bool _isLoadingRepos = false;
  String? _reposError;

  // Active Repository & Explorer State
  Repository? _selectedRepo;
  String _currentBranch = "main";
  List<BranchInfo> _branches = [];
  bool _isLoadingBranches = false;

  List<String> _pathSegments = [];
  List<FileExplorerItem> _currentDirectoryItems = [];
  bool _isLoadingExplorer = false;
  String? _explorerError;

  // Search
  String _searchQuery = "";

  // Getters
  int get currentTabIndex => _currentTabIndex;
  List<Repository> get repositories => _repositories;
  bool get isLoadingRepos => _isLoadingRepos;
  String? get reposError => _reposError;

  Repository? get selectedRepo => _selectedRepo;
  String get currentBranch => _currentBranch;
  List<BranchInfo> get branches => _branches;
  bool get isLoadingBranches => _isLoadingBranches;

  List<String> get pathSegments => _pathSegments;
  String get currentFolderPath => _pathSegments.join("/");
  List<FileExplorerItem> get currentDirectoryItems => _currentDirectoryItems;
  bool get isLoadingExplorer => _isLoadingExplorer;
  String? get explorerError => _explorerError;

  String get searchQuery => _searchQuery;

  void setTabIndex(int index) {
    _currentTabIndex = index;
    notifyListeners();
  }

  void setSearchQuery(String query) {
    _searchQuery = query;
    notifyListeners();
  }

  // Load Repositories
  Future<void> loadRepositories(String token, {bool force = false}) async {
    if (_repositories.isNotEmpty && !force && !_isLoadingRepos) return;
    _isLoadingRepos = true;
    _reposError = null;
    notifyListeners();

    try {
      _repositories = await ApiService.fetchRepositories(token);
    } catch (e) {
      _reposError = e.toString().replaceAll("Exception: ", "");
    } finally {
      _isLoadingRepos = false;
      notifyListeners();
    }
  }

  // Select Repository & Open Explorer
  Future<void> selectRepository(String token, Repository repo, {int targetTab = 1}) async {
    _selectedRepo = repo;
    _currentBranch = repo.defaultBranch;
    _pathSegments = [];
    _currentTabIndex = targetTab;
    notifyListeners();

    await loadBranches(token, repo.owner, repo.name);
    await refreshDirectoryContents(token);
  }

  // Load Branches
  Future<void> loadBranches(String token, String owner, String repoName) async {
    _isLoadingBranches = true;
    notifyListeners();
    try {
      _branches = await ApiService.fetchBranches(token, owner, repoName);
      if (!_branches.any((b) => b.name == _currentBranch) && _branches.isNotEmpty) {
        _currentBranch = _branches.first.name;
      }
    } catch (e) {
      debugPrint("Error fetching branches: $e");
    } finally {
      _isLoadingBranches = false;
      notifyListeners();
    }
  }

  // Switch Active Branch
  Future<void> switchBranch(String token, String newBranch) async {
    if (_currentBranch == newBranch) return;
    _currentBranch = newBranch;
    notifyListeners();
    await refreshDirectoryContents(token);
  }

  // Refresh Directory Contents
  Future<void> refreshDirectoryContents(String token) async {
    if (_selectedRepo == null) return;
    _isLoadingExplorer = true;
    _explorerError = null;
    notifyListeners();

    try {
      _currentDirectoryItems = await ApiService.fetchDirectoryContents(
        token,
        _selectedRepo!.owner,
        _selectedRepo!.name,
        path: currentFolderPath,
        branch: _currentBranch,
      );
    } catch (e) {
      _explorerError = e.toString().replaceAll("Exception: ", "");
    } finally {
      _isLoadingExplorer = false;
      notifyListeners();
    }
  }

  // Navigate Into Folder
  Future<void> navigateIntoFolder(String token, String folderName) async {
    _pathSegments.add(folderName);
    notifyListeners();
    await refreshDirectoryContents(token);
  }

  // Navigate Up / Back Folder
  Future<void> navigateUpFolder(String token) async {
    if (_pathSegments.isNotEmpty) {
      _pathSegments.removeLast();
      notifyListeners();
      await refreshDirectoryContents(token);
    }
  }

  // Jump to Breadcrumb index
  Future<void> jumpToBreadcrumb(String token, int index) async {
    if (index < 0) {
      _pathSegments.clear();
    } else if (index < _pathSegments.length) {
      _pathSegments = _pathSegments.sublist(0, index + 1);
    }
    notifyListeners();
    await refreshDirectoryContents(token);
  }
}
