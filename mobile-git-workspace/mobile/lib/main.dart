import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'theme/app_theme.dart';
import 'services/auth_service.dart';
import 'services/activity_service.dart';
import 'services/connection_service.dart';
import 'services/api_service.dart';
import 'providers/app_provider.dart';
import 'widgets/mobile_frame.dart';
import 'screens/auth_screen.dart';
import 'screens/main_navigation_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await ApiService.initBackendUrl();
  runApp(const MobileGitWorkspaceApp());
}

class MobileGitWorkspaceApp extends StatelessWidget {
  const MobileGitWorkspaceApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthService()),
        ChangeNotifierProvider(create: (_) => AppProvider()),
        ChangeNotifierProvider(create: (_) => ActivityService()),
        ChangeNotifierProvider(create: (_) => ConnectionService()),
      ],
      child: Consumer<AuthService>(
        builder: (context, auth, _) {
          return MaterialApp(
            title: 'Portfolio AI Assistant',
            debugShowCheckedModeBanner: false,
            theme: AppTheme.darkTheme,
            home: MobileFrameWrapper(
              child: auth.isLoading
                  ? const Scaffold(
                      backgroundColor: AppTheme.darkBg,
                      body: Center(
                        child: CircularProgressIndicator(color: AppTheme.primaryCyan),
                      ),
                    )
                  : auth.isAuthenticated
                      ? const MainNavigationScreen()
                      : const AuthScreen(),
            ),
          );
        },
      ),
    );
  }
}
