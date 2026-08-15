import 'package:flutter_test/flutter_test.dart';
import 'package:mobile_git_workspace/main.dart';

void main() {
  testWidgets('App loads test', (WidgetTester tester) async {
    await tester.pumpWidget(const MobileGitWorkspaceApp());
    expect(find.byType(MobileGitWorkspaceApp), findsOneWidget);
  });
}
