import 'dart:async';
import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'api_service.dart';

enum ConnectionStatus { connecting, connected, disconnected }

class ConnectionService extends ChangeNotifier {
  ConnectionStatus _status = ConnectionStatus.connecting;
  String? _lastError;
  Timer? _timer;

  ConnectionStatus get status => _status;
  String? get lastError => _lastError;
  bool get isConnected => _status == ConnectionStatus.connected;

  ConnectionService() {
    checkConnection();
    _timer = Timer.periodic(const Duration(seconds: 15), (_) => checkConnection());
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  Future<void> checkConnection() async {
    _status = ConnectionStatus.connecting;
    notifyListeners();

    try {
      final baseUrl = ApiService.backendBaseUrl;
      final uri = Uri.parse("$baseUrl/api/health");
      final res = await http.get(uri).timeout(const Duration(seconds: 3));

      if (res.statusCode == 200) {
        _status = ConnectionStatus.connected;
        _lastError = null;
      } else {
        _status = ConnectionStatus.disconnected;
        _lastError = "Server returned code ${res.statusCode}";
      }
    } catch (e) {
      _status = ConnectionStatus.disconnected;
      _lastError = "Unable to connect to Portfolio Assistant server ($e)";
    }
    notifyListeners();
  }
}
