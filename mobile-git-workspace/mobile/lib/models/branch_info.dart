class BranchInfo {
  final String name;
  final String commitSha;
  final bool protected;

  BranchInfo({
    required this.name,
    required this.commitSha,
    this.protected = false,
  });

  factory BranchInfo.fromJson(Map<String, dynamic> json) {
    return BranchInfo(
      name: json['name'] ?? '',
      commitSha: json['commit_sha'] ?? (json['commit'] is Map ? json['commit']['sha'] ?? '' : ''),
      protected: json['protected'] ?? false,
    );
  }
}
