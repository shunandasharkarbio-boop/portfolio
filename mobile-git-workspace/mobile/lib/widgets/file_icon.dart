import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class FileTypeIcon extends StatelessWidget {
  final String fileName;
  final bool isDirectory;
  final double size;

  const FileTypeIcon({
    super.key,
    required this.fileName,
    required this.isDirectory,
    this.size = 22,
  });

  @override
  Widget build(BuildContext context) {
    if (isDirectory) {
      return Icon(Icons.folder_rounded, color: const Color(0xFF54A0FF), size: size);
    }

    final ext = fileName.contains('.') ? fileName.split('.').last.toLowerCase() : '';

    IconData iconData = Icons.insert_drive_file_outlined;
    Color iconColor = AppTheme.textSecondary;

    switch (ext) {
      case 'py':
        iconData = Icons.code_rounded;
        iconColor = const Color(0xFF3572A5);
        break;
      case 'js':
      case 'jsx':
        iconData = Icons.javascript_rounded;
        iconColor = const Color(0xFFF1E05A);
        break;
      case 'ts':
      case 'tsx':
        iconData = Icons.code_rounded;
        iconColor = const Color(0xFF3178C6);
        break;
      case 'html':
      case 'htm':
        iconData = Icons.html_rounded;
        iconColor = const Color(0xFFE34C26);
        break;
      case 'css':
      case 'scss':
        iconData = Icons.css_rounded;
        iconColor = const Color(0xFF563D7C);
        break;
      case 'md':
      case 'markdown':
        iconData = Icons.article_outlined;
        iconColor = AppTheme.primaryCyan;
        break;
      case 'json':
      case 'yaml':
      case 'yml':
      case 'xml':
        iconData = Icons.data_object_rounded;
        iconColor = const Color(0xFFCB3837);
        break;
      case 'sh':
      case 'bash':
        iconData = Icons.terminal_rounded;
        iconColor = const Color(0xFF4E9A06);
        break;
      case 'png':
      case 'jpg':
      case 'jpeg':
      case 'gif':
      case 'svg':
      case 'webp':
        iconData = Icons.image_outlined;
        iconColor = const Color(0xFFFF9F43);
        break;
      case 'pdf':
        iconData = Icons.picture_as_pdf_outlined;
        iconColor = AppTheme.dangerRed;
        break;
      case 'txt':
        iconData = Icons.description_outlined;
        iconColor = AppTheme.textPrimary;
        break;
      case 'dart':
        iconData = Icons.flutter_dash;
        iconColor = const Color(0xFF00B4AB);
        break;
    }

    return Icon(iconData, color: iconColor, size: size);
  }
}
