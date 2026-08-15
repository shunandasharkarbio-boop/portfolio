class FileExplorerItem {
  final String name;
  final String path;
  final String sha;
  final int size;
  final String type; // "file" or "dir"
  final String? downloadUrl;
  final String? htmlUrl;

  FileExplorerItem({
    required this.name,
    required this.path,
    required this.sha,
    required this.size,
    required this.type,
    this.downloadUrl,
    this.htmlUrl,
  });

  bool get isDirectory => type == "dir";

  String get formattedSize {
    if (isDirectory) return "";
    if (size < 1024) return "$size B";
    if (size < 1024 * 1024) return "${(size / 1024).toStringAsFixed(1)} KB";
    return "${(size / (1024 * 1024)).toStringAsFixed(1)} MB";
  }

  factory FileExplorerItem.fromJson(Map<String, dynamic> json) {
    return FileExplorerItem(
      name: json['name'] ?? '',
      path: json['path'] ?? '',
      sha: json['sha'] ?? '',
      size: json['size'] ?? 0,
      type: json['type'] ?? 'file',
      downloadUrl: json['download_url'],
      htmlUrl: json['html_url'],
    );
  }
}
