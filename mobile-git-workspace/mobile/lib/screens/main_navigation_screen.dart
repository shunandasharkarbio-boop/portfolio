import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import '../providers/app_provider.dart';
import '../services/connection_service.dart';
import '../services/api_service.dart';
import '../theme/app_theme.dart';
import 'home_screen.dart';
import 'repositories_screen.dart';
import 'ai_assistant_screen.dart';
import 'search_screen.dart';
import 'activity_screen.dart';
import 'settings_screen.dart';

class MainNavigationScreen extends StatelessWidget {
  const MainNavigationScreen({super.key});

  static const List<Widget> _screens = [
    HomeScreen(),
    RepositoriesScreen(),
    AIAssistantScreen(),
    SearchScreen(),
    ActivityScreen(),
    SettingsScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    final appProv = Provider.of<AppProvider>(context);
    final connService = Provider.of<ConnectionService>(context);

    Color connColor;
    String connLabel;

    switch (connService.status) {
      case ConnectionStatus.connected:
        connColor = AppTheme.successGreen;
        connLabel = "Connected";
        break;
      case ConnectionStatus.connecting:
        connColor = AppTheme.warningOrange;
        connLabel = "Connecting...";
        break;
      case ConnectionStatus.disconnected:
        connColor = AppTheme.dangerRed;
        connLabel = "Disconnected";
        break;
    }

    return Scaffold(
      backgroundColor: AppTheme.darkBg,
      body: SafeArea(
        child: Column(
          children: [
            // Top Connection Status Header Bar
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
              color: AppTheme.cardBg,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Row(
                    children: [
                      Container(
                        width: 8,
                        height: 8,
                        decoration: BoxDecoration(color: connColor, shape: BoxShape.circle),
                      ),
                      const SizedBox(width: 8),
                      Text(
                        connLabel,
                        style: GoogleFonts.inter(fontSize: 11, fontWeight: FontWeight.bold, color: connColor),
                      ),
                    ],
                  ),
                  Text(
                    ApiService.backendBaseUrl,
                    style: GoogleFonts.jetBrainsMono(fontSize: 10, color: AppTheme.textSecondary),
                    overflow: TextOverflow.ellipsis,
                  ),
                ],
              ),
            ),

            // Disconnected Banner Error Card
            if (connService.status == ConnectionStatus.disconnected)
              Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                color: AppTheme.dangerRed.withOpacity(0.18),
                child: Row(
                  children: [
                    const Icon(Icons.wifi_off_rounded, color: AppTheme.dangerRed, size: 18),
                    const SizedBox(width: 8),
                    Expanded(
                      child: Text(
                        "Unable to connect to Portfolio Assistant server.",
                        style: GoogleFonts.inter(color: AppTheme.dangerRed, fontSize: 11, fontWeight: FontWeight.w600),
                      ),
                    ),
                    TextButton(
                      style: TextButton.styleFrom(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                        minimumSize: Size.zero,
                        tapTargetSize: MaterialTapTargetSize.shrinkWrap,
                      ),
                      onPressed: () => connService.checkConnection(),
                      child: Text(
                        "Retry",
                        style: GoogleFonts.inter(color: AppTheme.primaryCyan, fontSize: 11, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ],
                ),
              ),

            // Active Tab View
            Expanded(
              child: IndexedStack(
                index: appProv.currentTabIndex,
                children: _screens,
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: appProv.currentTabIndex,
        onTap: (index) => appProv.setTabIndex(index),
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home_outlined),
            activeIcon: Icon(Icons.home_rounded, color: AppTheme.primaryCyan),
            label: "Home",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.folder_outlined),
            activeIcon: Icon(Icons.folder_rounded, color: AppTheme.primaryCyan),
            label: "Repos",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.auto_awesome_outlined),
            activeIcon: Icon(Icons.auto_awesome_rounded, color: AppTheme.primaryCyan),
            label: "AI Chat",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.search_outlined),
            activeIcon: Icon(Icons.search_rounded, color: AppTheme.primaryCyan),
            label: "Search",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.history_outlined),
            activeIcon: Icon(Icons.history_rounded, color: AppTheme.primaryCyan),
            label: "Activity",
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings_outlined),
            activeIcon: Icon(Icons.settings_rounded, color: AppTheme.primaryCyan),
            label: "Settings",
          ),
        ],
      ),
    );
  }
}
