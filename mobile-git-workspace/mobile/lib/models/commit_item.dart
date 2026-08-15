class CommitItem {
  final String sha;
  final String message;
  final String authorName;
  final String? authorAvatar;
  final String date;
  final String htmlUrl;

  CommitItem({
    required this.sha,
    required this.message,
    required this.authorName,
    this.authorAvatar,
    required this.date,
    required this.htmlUrl,
  });

  factory CommitItem.fromJson(Map<String, dynamic> json) {
    return CommitItem(
      sha: json['sha'] ?? '',
      message: json['message'] ?? '',
      authorName: json['author_name'] ?? 'Unknown',
      authorAvatar: json['author_avatar'],
      date: json['date'] ?? '',
      htmlUrl: json['html_url'] ?? '',
    );
  }
}
