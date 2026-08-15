class ActivityItem {
  final String id;
  final String actionType; // "uploaded", "created", "updated", "deleted", "branch"
  final String repoName;
  final String filePath;
  final String commitMessage;
  final String timestamp;
  final String branch;

  ActivityItem({
    required this.id,
    required this.actionType,
    required this.repoName,
    required this.filePath,
    required this.commitMessage,
    required this.timestamp,
    required this.branch,
  });

  factory ActivityItem.fromJson(Map<String, dynamic> json) {
    return ActivityItem(
      id: json['id'] ?? '',
      actionType: json['action_type'] ?? 'updated',
      repoName: json['repo_name'] ?? '',
      filePath: json['file_path'] ?? '',
      commitMessage: json['commit_message'] ?? '',
      timestamp: json['timestamp'] ?? '',
      branch: json['branch'] ?? 'main',
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'action_type': actionType,
      'repo_name': repoName,
      'file_path': filePath,
      'commit_message': commitMessage,
      'timestamp': timestamp,
      'branch': branch,
    };
  }
}
