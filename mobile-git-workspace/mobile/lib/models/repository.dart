class Repository {
  final int id;
  final String name;
  final String fullName;
  final String owner;
  final bool private;
  final String description;
  final String defaultBranch;
  final String updatedAt;
  final int stargazersCount;
  final int forksCount;
  final String? language;
  final String htmlUrl;
  final bool hasPages;
  final String? pagesUrl;

  Repository({
    required this.id,
    required this.name,
    required this.fullName,
    required this.owner,
    required this.private,
    required this.description,
    required this.defaultBranch,
    required this.updatedAt,
    this.stargazersCount = 0,
    this.forksCount = 0,
    this.language,
    required this.htmlUrl,
    this.hasPages = false,
    this.pagesUrl,
  });

  factory Repository.fromJson(Map<String, dynamic> json) {
    return Repository(
      id: json['id'] ?? 0,
      name: json['name'] ?? '',
      fullName: json['full_name'] ?? json['name'] ?? '',
      owner: json['owner'] is Map ? json['owner']['login'] ?? '' : (json['owner'] ?? ''),
      private: json['private'] ?? false,
      description: json['description'] ?? '',
      defaultBranch: json['default_branch'] ?? 'main',
      updatedAt: json['updated_at'] ?? '',
      stargazersCount: json['stargazers_count'] ?? 0,
      forksCount: json['forks_count'] ?? 0,
      language: json['language'],
      htmlUrl: json['html_url'] ?? '',
      hasPages: json['has_pages'] ?? false,
      pagesUrl: json['pages_url'],
    );
  }
}
