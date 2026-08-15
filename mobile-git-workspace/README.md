# Portfolio AI Assistant / Mobile Git Workspace

A mobile-first application designed to allow developers to manage GitHub repositories, edit code, **upload files directly from a physical Android phone**, and perform **AI-driven portfolio updates**.

---

## Features

1. **Physical Android App & Cleartext Traffic Support**:
   - Production-ready APK build (`flutter build apk --release`).
   - Configured with `INTERNET`, `READ_MEDIA_IMAGES`, `READ_EXTERNAL_STORAGE` permissions and `android:usesCleartextTraffic="true"` to connect to computer's local IP address over Wi-Fi (`http://192.168.x.x:8000`).

2. **Dynamic Backend URL Configuration (`API_BASE_URL`)**:
   - Dynamic backend URL setting stored in local storage and editable via Settings without rebuilding the APK binary.
   - Switch seamlessly between local Wi-Fi IP (`http://192.168.x.x:8000`) and production cloud HTTPS backend (`https://my-backend-domain.com`).

3. **Backend Connection Status Indicator**:
   - Live top bar connection indicator:
     - `Connected` (Green badge)
     - `Connecting...` (Yellow badge)
     - `Disconnected` (Red badge)
   - Diagnostic banner with **"Unable to connect to Portfolio Assistant server"** + **Retry** button.

4. **Portfolio AI Assistant & Repository Analysis**:
   - Dedicated **AI Chat** tab in bottom navigation.
   - Presets: *"Change my portfolio About section"*, *"Analyze repository structure"*, *"Review recent commits"*.
   - Evaluates target repository, suggests file modifications, renders diff summary, and provides a 1-tap **[ Approve & Commit to GitHub ]** button.

5. **Upload Files From Android Phone**:
   - Pick documents, images, laboratory coursework from Android storage via `file_picker`.
   - Choose target repository, destination folder (`docs/`, `src/`), branch, and custom commit message.
   - Direct commit to GitHub API with real-time progress bar.

---

## Guide: How to Setup, Build & Deploy

### A. How to Run Backend Locally
Run the FastAPI backend server on all network interfaces (`0.0.0.0`):

```bash
cd mobile-git-workspace/backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

### B. How to Connect Physical Android Phone over Wi-Fi

1. Ensure both your computer and your Android phone are connected to the **same Wi-Fi network**.
2. Find your computer's local IP address:
   - **Windows**: Open Command Prompt / PowerShell and run `ipconfig` (Look for `IPv4 Address`, e.g., `192.168.1.15`).
   - **Mac/Linux**: Run `ifconfig` or `ip a` (e.g., `192.168.1.15`).
3. Open the app on your Android phone, go to **Settings** or the top Connection bar, and set the Backend URL to:
   ```
   http://192.168.1.15:8000
   ```
4. The connection indicator will turn green (`Connected`).

---

### C. How to Build the Release APK

To build the standalone release APK for installation on Android devices:

```bash
cd mobile-git-workspace/mobile
flutter build apk --release
```

The compiled APK will be generated at:
```
mobile/build/app/outputs/flutter-apk/app-release.apk
```

---

### D. How to Configure Production Backend URL

1. Deploy your FastAPI backend to a cloud host (see Section E).
2. Open the installed Android app on your phone.
3. Go to **Settings** -> **Backend Server URL**.
4. Enter your production HTTPS domain (e.g. `https://api.myportfolioassistant.com`).
5. Tap **Save**. The app immediately communicates with your production server without requiring an APK rebuild.

---

### E. How to Deploy the Backend to Production

#### Option 1: Docker / Render / Railway
Create a `Dockerfile` inside `mobile-git-workspace/backend/`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Set Environment Variables in your hosting provider dashboard:
- `GITHUB_CLIENT_ID`: Your GitHub OAuth Client ID
- `GITHUB_CLIENT_SECRET`: Your GitHub OAuth Client Secret
- `HOST`: `0.0.0.0`
- `PORT`: `8000`

---

### F. How to Install the APK on Android Phone

1. Transfer `app-release.apk` (from `mobile/build/app/outputs/flutter-apk/app-release.apk`) to your phone via USB, Google Drive, Email, or WhatsApp.
2. Tap the `.apk` file on your Android phone.
3. If prompted with *"Install unknown apps"*, enable permission for your file manager or browser.
4. Tap **Install** and open **Portfolio AI Assistant**!
