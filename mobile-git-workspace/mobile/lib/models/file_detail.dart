import 'dart:convert';

class FileDetail {
  final String name;
  final String path;
  final String sha;
  final int size;
  final String encoding;
  final String? contentB64;
  final bool isText;
  final String htmlUrl;
  final String? downloadUrl;

  FileDetail({
    required this.name,
    required this.path,
    required this.sha,
    required this.size,
    required this.encoding,
    this.contentB64,
    required this.isText,
    required this.htmlUrl,
    this.downloadUrl,
  });

  String get decodedText {
    if (contentB64 == null || contentB64!.isEmpty) return "";
    try {
      final clean = contentB64!.replaceAll(RegExp(r'\s+'), '');
      final bytes = base64.decode(clean);
      return utf8.decode(bytes, allowMalformed: true);
    } catch (e) {
      return "Unable to decode text content: $e";
    }
  }

  factory FileDetail.fromJson(Map<String, dynamic> json) {
    return FileDetail(
      name: json['name'] ?? '',
      path: json['path'] ?? '',
      sha: json['sha'] ?? '',
      size: json['size'] ?? 0,
      encoding: json['encoding'] ?? 'base64',
      contentB64: json['content_b64'] ?? json['content'],
      isText: json['is_text'] ?? true,
      htmlUrl: json['html_url'] ?? '',
      downloadUrl: json['download_url'],
    );
  }
}
