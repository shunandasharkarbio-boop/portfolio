import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/activity_item.dart';

class ActivityService extends ChangeNotifier {
  static const String _activityKey = "mobile_git_workspace_activity_log";
  List<ActivityItem> _activities = [];

  List<ActivityItem> get activities => _activities;

  ActivityService() {
    loadActivities();
  }

  Future<void> loadActivities() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final str = prefs.getString(_activityKey);
      if (str != null && str.isNotEmpty) {
        final List<dynamic> list = jsonDecode(str);
        _activities = list.map((e) => ActivityItem.fromJson(e)).toList();
      }
    } catch (e) {
      debugPrint("Error loading activities: $e");
    }
    notifyListeners();
  }

  Future<void> logActivity({
    required String actionType,
    required String repoName,
    required String filePath,
    required String commitMessage,
    required String branch,
  }) async {
    final item = ActivityItem(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      actionType: actionType,
      repoName: repoName,
      filePath: filePath,
      commitMessage: commitMessage,
      timestamp: DateTime.now().toIso8601String(),
      branch: branch,
    );

    _activities.insert(0, item);
    if (_activities.length > 100) {
      _activities = _activities.sublist(0, 100);
    }

    try {
      final prefs = await SharedPreferences.getInstance();
      final encoded = jsonEncode(_activities.map((e) => e.toJson()).toList());
      await prefs.setString(_activityKey, encoded);
    } catch (e) {
      debugPrint("Error saving activity: $e");
    }
    notifyListeners();
  }

  Future<void> clearActivities() async {
    _activities.clear();
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(_activityKey);
    notifyListeners();
  }
}
