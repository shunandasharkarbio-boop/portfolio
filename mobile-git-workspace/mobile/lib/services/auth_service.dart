import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/user_profile.dart';

class AuthService extends ChangeNotifier {
  static const String _tokenKey = "github_access_token";
  static const String _userKey = "github_user_profile";
  static const String _defaultBranchKey = "default_branch_pref";
  static const String _defaultCommitMsgKey = "default_commit_msg_pref";

  String? _token;
  UserProfile? _user;
  bool _isLoading = true;
  String _defaultBranch = "main";
  String _defaultCommitMessageTemplate = "Update {file} via Mobile Git Workspace";

  String? get token => _token;
  UserProfile? get user => _user;
  bool get isAuthenticated => _token != null && _token!.isNotEmpty;
  bool get isLoading => _isLoading;
  String get defaultBranch => _defaultBranch;
  String get defaultCommitMessageTemplate => _defaultCommitMessageTemplate;

  AuthService() {
    initAuth();
  }

  Future<void> initAuth() async {
    _isLoading = true;
    notifyListeners();
    try {
      final prefs = await SharedPreferences.getInstance();
      _token = prefs.getString(_tokenKey);
      final userStr = prefs.getString(_userKey);
      if (userStr != null && userStr.isNotEmpty) {
        _user = UserProfile.fromJson(jsonDecode(userStr));
      }
      _defaultBranch = prefs.getString(_defaultBranchKey) ?? "main";
      _defaultCommitMsgKey;
      _defaultCommitMessageTemplate = prefs.getString(_defaultCommitMsgKey) ?? "Update {file} via Mobile Git Workspace";
    } catch (e) {
      debugPrint("Error initializing auth: $e");
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

  Future<void> saveAuth(String token, UserProfile user) async {
    _token = token;
    _user = user;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_tokenKey, token);
    await prefs.setString(_userKey, jsonEncode(user.toJson()));
    notifyListeners();
  }

  Future<void> updatePreferences({String? defaultBranch, String? defaultCommitMsg}) async {
    final prefs = await SharedPreferences.getInstance();
    if (defaultBranch != null) {
      _defaultBranch = defaultBranch;
      await prefs.setString(_defaultBranchKey, defaultBranch);
    }
    if (defaultCommitMsg != null) {
      _defaultCommitMessageTemplate = defaultCommitMsg;
      await prefs.setString(_defaultCommitMsgKey, defaultCommitMsg);
    }
    notifyListeners();
  }

  Future<void> logout() async {
    _token = null;
    _user = null;
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(_tokenKey);
    await prefs.remove(_userKey);
    notifyListeners();
  }
}
