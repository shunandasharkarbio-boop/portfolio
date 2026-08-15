import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class MobileFrameWrapper extends StatelessWidget {
  final Widget child;

  const MobileFrameWrapper({super.key, required this.child});

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (ctx, constraints) {
        // If screen width > 600 (e.g. desktop/web browser), wrap in mobile phone mockup frame
        if (constraints.maxWidth > 600) {
          return Scaffold(
            backgroundColor: const Color(0xFF030712),
            body: Center(
              child: Container(
                width: 420,
                height: constraints.maxHeight * 0.94,
                margin: const EdgeInsets.symmetric(vertical: 20),
                decoration: BoxDecoration(
                  color: AppTheme.darkBg,
                  borderRadius: BorderRadius.circular(32),
                  border: Border.all(color: const Color(0xFF1F2937), width: 8),
                  boxShadow: [
                    BoxShadow(
                      color: AppTheme.primaryCyan.withOpacity(0.15),
                      blurRadius: 30,
                      spreadRadius: 5,
                    ),
                  ],
                ),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(24),
                  child: child,
                ),
              ),
            ),
          );
        }
        return child;
      },
    );
  }
}
