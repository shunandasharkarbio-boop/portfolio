class UserProfile {
  final String login;
  final int id;
  final String avatarUrl;
  final String? name;
  final String? email;
  final int publicRepos;
  final int totalPrivateRepos;

  UserProfile({
    required this.login,
    required this.id,
    required this.avatarUrl,
    this.name,
    this.email,
    this.publicRepos = 0,
    this.totalPrivateRepos = 0,
  });

  factory UserProfile.fromJson(Map<String, dynamic> json) {
    return UserProfile(
      login: json['login'] ?? '',
      id: json['id'] ?? 0,
      avatarUrl: json['avatar_url'] ?? '',
      name: json['name'],
      email: json['email'],
      publicRepos: json['public_repos'] ?? 0,
      totalPrivateRepos: json['total_private_repos'] ?? 0,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'login': login,
      'id': id,
      'avatar_url': avatarUrl,
      'name': name,
      'email': email,
      'public_repos': publicRepos,
      'total_private_repos': totalPrivateRepos,
    };
  }
}
