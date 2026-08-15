import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import '../models/user_profile.dart';
import '../models/repository.dart';
import '../models/file_item.dart';
import '../models/file_detail.dart';
import '../models/branch_info.dart';
import '../models/commit_item.dart';

class ApiService {
  static String backendBaseUrl = "http://localhost:8000";

  static Map<String, String> _headers(String token) {
    final cleanToken = token.trim();
    final authVal = (cleanToken.startsWith("Bearer ") || cleanToken.startsWith("token "))
        ? cleanToken
        : "Bearer $cleanToken";
    return {
      "Authorization": authVal,
      "Content-Type": "application/json",
      "Accept": "application/json",
    };
  }

  // 1. Verify User Token
  static Future<UserProfile> verifyToken(String token) async {
    // Try FastAPI Backend
    try {
      final res = await http.post(
        Uri.parse("$backendBaseUrl/api/auth/verify"),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"token": token}),
      ).timeout(const Duration(seconds: 4));
      if (res.statusCode == 200) {
        return UserProfile.fromJson(jsonDecode(res.body));
      }
    } catch (_) {}

    // Fallback: Direct GitHub API
    final ghRes = await http.get(
      Uri.parse("https://api.github.com/user"),
      headers: {
        "Authorization": "Bearer $token",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "MobileGitWorkspace/1.0"
      },
    );
    if (ghRes.statusCode == 200) {
      return UserProfile.fromJson(jsonDecode(ghRes.body));
    } else {
      final err = jsonDecode(ghRes.body)['message'] ?? ghRes.body;
      throw Exception("GitHub Auth Error ($ghRes.statusCode): $err");
    }
  }

  // 2. Fetch User Repositories
  static Future<List<Repository>> fetchRepositories(String token, {String search = ""}) async {
    // Try FastAPI Backend
    try {
      final uri = Uri.parse("$backendBaseUrl/api/repos").replace(
        queryParameters: search.isNotEmpty ? {"search": search} : null,
      );
      final res = await http.get(uri, headers: _headers(token)).timeout(const Duration(seconds: 4));
      if (res.statusCode == 200) {
        final List<dynamic> list = jsonDecode(res.body);
        return list.map((e) => Repository.fromJson(e)).toList();
      }
    } catch (_) {}

    // Fallback: Direct GitHub API
    final uri = Uri.parse("https://api.github.com/user/repos?sort=updated&per_page=100&affiliation=owner,collaborator,organization_member");
    final ghRes = await http.get(
      uri,
      headers: {
        "Authorization": "Bearer $token",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "MobileGitWorkspace/1.0"
      },
    );
    if (ghRes.statusCode == 200) {
      final List<dynamic> list = jsonDecode(ghRes.body);
      final repos = list.map((e) => Repository.fromJson(e)).toList();
      if (search.isNotEmpty) {
        final q = search.toLowerCase();
        return repos.where((r) => r.name.toLowerCase().contains(q) || r.description.toLowerCase().contains(q)).toList();
      }
      return repos;
    } else {
      throw Exception("Failed to load repos from GitHub (${ghRes.statusCode})");
    }
  }

  // 3. Fetch Directory Contents
  static Future<List<FileExplorerItem>> fetchDirectoryContents(
    String token,
    String owner,
    String repo, {
    String path = "",
    String branch = "main",
  }) async {
    // Try FastAPI Backend
    try {
      final uri = Uri.parse("$backendBaseUrl/api/files/contents/$owner/$repo").replace(
        queryParameters: {
          "path": path,
          "ref": branch,
        },
      );
      final res = await http.get(uri, headers: _headers(token)).timeout(const Duration(seconds: 4));
      if (res.statusCode == 200) {
        final data = jsonDecode(res.body);
        if (data['is_file'] == false && data['items'] is List) {
          final List<dynamic> items = data['items'];
          return items.map((e) => FileExplorerItem.fromJson(e)).toList();
        }
      }
    } catch (_) {}

    // Fallback: Direct GitHub API
    final cleanPath = path.trim().replaceAll(RegExp(r'^/|/$'), '');
    final ghUrl = "https://api.github.com/repos/$owner/$repo/contents/$cleanPath${branch.isNotEmpty ? '?ref=$branch' : ''}";
    final ghRes = await http.get(
      Uri.parse(ghUrl),
      headers: {
        "Authorization": "Bearer $token",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "MobileGitWorkspace/1.0"
      },
    );

    if (ghRes.statusCode == 200) {
      final data = jsonDecode(ghRes.body);
      if (data is List) {
        final items = data.map((e) => FileExplorerItem.fromJson(e)).toList();
        items.sort((a, b) => (a.isDirectory ? 0 : 1).compareTo(b.isDirectory ? 0 : 1));
        return items;
      }
      return [];
    } else if (ghRes.statusCode == 404) {
      return [];
    } else {
      throw Exception("Error fetching directory contents (${ghRes.statusCode})");
    }
  }

  // 4. Fetch File Detail (Content)
  static Future<FileDetail> fetchFileDetail(
    String token,
    String owner,
    String repo,
    String path, {
    String branch = "main",
  }) async {
    // Try FastAPI Backend
    try {
      final uri = Uri.parse("$backendBaseUrl/api/files/contents/$owner/$repo").replace(
        queryParameters: {
          "path": path,
          "ref": branch,
        },
      );
      final res = await http.get(uri, headers: _headers(token)).timeout(const Duration(seconds: 4));
      if (res.statusCode == 200) {
        final data = jsonDecode(res.body);
        if (data['is_file'] == true && data['file'] != null) {
          return FileDetail.fromJson(data['file']);
        }
      }
    } catch (_) {}

    // Fallback: Direct GitHub API
    final cleanPath = path.trim().replaceAll(RegExp(r'^/|/$'), '');
    final ghUrl = "https://api.github.com/repos/$owner/$repo/contents/$cleanPath${branch.isNotEmpty ? '?ref=$branch' : ''}";
    final ghRes = await http.get(
      Uri.parse(ghUrl),
      headers: {
        "Authorization": "Bearer $token",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "MobileGitWorkspace/1.0"
      },
    );

    if (ghRes.statusCode == 200) {
      final data = jsonDecode(ghRes.body);
      if (data is Map<String, dynamic>) {
        return FileDetail.fromJson(data);
      }
    }
    throw Exception("Failed to load file details (${ghRes.statusCode})");
  }

  // 5. Commit Single File (Create or Update)
  static Future<String> commitFile({
    required String token,
    required String owner,
    required String repo,
    required String path,
    required String message,
    required String contentB64,
    String branch = "main",
    String? sha,
  }) async {
    // Try Backend
    try {
      final res = await http.post(
        Uri.parse("$backendBaseUrl/api/files/commit/$owner/$repo"),
        headers: _headers(token),
        body: jsonEncode({
          "owner": owner,
          "repo": repo,
          "path": path,
          "message": message,
          "content_b64": contentB64,
          "branch": branch,
          "sha": sha,
        }),
      ).timeout(const Duration(seconds: 5));
      if (res.statusCode == 200) {
        final data = jsonDecode(res.body);
        return data['commit_sha'] ?? 'success';
      }
    } catch (_) {}

    // Direct GitHub REST API Fallback
    final cleanPath = path.trim().replaceAll(RegExp(r'^/|/$'), '');
    final ghUrl = "https://api.github.com/repos/$owner/$repo/contents/$cleanPath";

    // If SHA not given, fetch current SHA if updating
    String? currentSha = sha;
    if (currentSha == null) {
      try {
        final existRes = await http.get(
          Uri.parse("$ghUrl?ref=$branch"),
          headers: {
            "Authorization": "Bearer $token",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "MobileGitWorkspace/1.0"
          },
        );
        if (existRes.statusCode == 200) {
          final data = jsonDecode(existRes.body);
          if (data is Map && data.containsKey("sha")) {
            currentSha = data["sha"];
          }
        }
      } catch (_) {}
    }

    final body = {
      "message": message,
      "content": contentB64,
      "branch": branch,
      if (currentSha != null) "sha": currentSha,
    };

    final ghRes = await http.put(
      Uri.parse(ghUrl),
      headers: {
        "Authorization": "Bearer $token",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "MobileGitWorkspace/1.0"
      },
      body: jsonEncode(body),
    );

    if (ghRes.statusCode == 200 || ghRes.statusCode == 201) {
      final data = jsonDecode(ghRes.body);
      return data['commit']?['sha'] ?? 'success';
    } else {
      final err = jsonDecode(ghRes.body)['message'] ?? ghRes.body;
      throw Exception("Commit failed (${ghRes.statusCode}): $err");
    }
  }

  // 6. Upload Raw File Bytes from Phone Storage
  static Future<String> uploadPhoneFile({
    required String token,
    required String owner,
    required String repo,
    required String folderPath,
    required String filename,
    required Uint8List bytes,
    required String message,
    String branch = "main",
  }) async {
    final b64 = base64Encode(bytes);
    final cleanFolder = folderPath.trim().replaceAll(RegExp(r'^/|/$'), '');
    final fullPath = cleanFolder.isNotEmpty ? "$cleanFolder/$filename" : filename;

    return await commitFile(
      token: token,
      owner: owner,
      repo: repo,
      path: fullPath,
      message: message,
      contentB64: b64,
      branch: branch,
    );
  }

  // 7. Create Folder
  static Future<String> createFolder({
    required String token,
    required String owner,
    required String repo,
    required String folderPath,
    required String message,
    String branch = "main",
  }) async {
    final cleanFolder = folderPath.trim().replaceAll(RegExp(r'^/|/$'), '');
    final targetPath = "$cleanFolder/.gitkeep";
    final b64Content = base64Encode(utf8.encode(""));

    return await commitFile(
      token: token,
      owner: owner,
      repo: repo,
      path: targetPath,
      message: message.isNotEmpty ? message : "Create folder $cleanFolder",
      contentB64: b64Content,
      branch: branch,
    );
  }

  // 8. Delete File
  static Future<String> deleteFile({
    required String token,
    required String owner,
    required String repo,
    required String path,
    required String sha,
    required String message,
    String branch = "main",
  }) async {
    // Try Backend
    try {
      final res = await http.post(
        Uri.parse("$backendBaseUrl/api/files/delete/$owner/$repo"),
        headers: _headers(token),
        body: jsonEncode({
          "owner": owner,
          "repo": repo,
          "path": path,
          "message": message,
          "sha": sha,
          "branch": branch,
        }),
      ).timeout(const Duration(seconds: 5));
      if (res.statusCode == 200) {
        final data = jsonDecode(res.body);
        return data['commit_sha'] ?? 'deleted';
      }
    } catch (_) {}

    // Direct GitHub REST API Fallback
    final cleanPath = path.trim().replaceAll(RegExp(r'^/|/$'), '');
    final ghUrl = "https://api.github.com/repos/$owner/$repo/contents/$cleanPath";

    final ghRes = await http.delete(
      Uri.parse(ghUrl),
      headers: {
        "Authorization": "Bearer $token",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "MobileGitWorkspace/1.0"
      },
      body: jsonEncode({
        "message": message,
        "sha": sha,
        "branch": branch,
      }),
    );

    if (ghRes.statusCode == 200) {
      final data = jsonDecode(ghRes.body);
      return data['commit']?['sha'] ?? 'deleted';
    } else {
      final err = jsonDecode(ghRes.body)['message'] ?? ghRes.body;
      throw Exception("Delete failed (${ghRes.statusCode}): $err");
    }
  }

  // 9. Fetch Branches
  static Future<List<BranchInfo>> fetchBranches(String token, String owner, String repo) async {
    final ghUrl = "https://api.github.com/repos/$owner/$repo/branches";
    final ghRes = await http.get(
      Uri.parse(ghUrl),
      headers: {
        "Authorization": "Bearer $token",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "MobileGitWorkspace/1.0"
      },
    );
    if (ghRes.statusCode == 200) {
      final List<dynamic> list = jsonDecode(ghRes.body);
      return list.map((e) => BranchInfo.fromJson(e)).toList();
    }
    return [BranchInfo(name: "main", commitSha: "")];
  }

  // 10. Create Branch
  static Future<void> createBranch({
    required String token,
    required String owner,
    required String repo,
    required String newBranch,
    String baseBranch = "main",
  }) async {
    // 1. Get base sha
    final refRes = await http.get(
      Uri.parse("https://api.github.com/repos/$owner/$repo/git/ref/heads/$baseBranch"),
      headers: {
        "Authorization": "Bearer $token",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "MobileGitWorkspace/1.0"
      },
    );
    if (refRes.statusCode != 200) {
      throw Exception("Base branch '$baseBranch' not found");
    }
    final baseSha = jsonDecode(refRes.body)["object"]["sha"];

    // 2. Create ref
    final createRes = await http.post(
      Uri.parse("https://api.github.com/repos/$owner/$repo/git/refs"),
      headers: {
        "Authorization": "Bearer $token",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "MobileGitWorkspace/1.0"
      },
      body: jsonEncode({
        "ref": "refs/heads/$newBranch",
        "sha": baseSha,
      }),
    );

    if (createRes.statusCode != 201) {
      final err = jsonDecode(createRes.body)['message'] ?? createRes.body;
      throw Exception("Failed to create branch '$newBranch': $err");
    }
  }

  // 11. Fetch Commit History
  static Future<List<CommitItem>> fetchCommits(String token, String owner, String repo, {String branch = "main"}) async {
    final ghUrl = "https://api.github.com/repos/$owner/$repo/commits?sha=$branch&per_page=20";
    final ghRes = await http.get(
      Uri.parse(ghUrl),
      headers: {
        "Authorization": "Bearer $token",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "MobileGitWorkspace/1.0"
      },
    );

    if (ghRes.statusCode == 200) {
      final List<dynamic> list = jsonDecode(ghRes.body);
      final res = <CommitItem>[];
      for (var c in list) {
        final commitObj = c["commit"] ?? {};
        final authorObj = c["author"] ?? {};
        res.add(CommitItem(
          sha: (c["sha"] ?? "").toString().substring(0, 7),
          message: (commitObj["message"] ?? "").toString().split('\n').first,
          authorName: commitObj["author"]?["name"] ?? "Unknown",
          authorAvatar: authorObj["avatar_url"],
          date: commitObj["author"]?["date"] ?? "",
          htmlUrl: c["html_url"] ?? "",
        ));
      }
      return res;
    }
    return [];
  }
}
