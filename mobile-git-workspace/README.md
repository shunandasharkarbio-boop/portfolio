# Mobile Git Workspace

A mobile-first application designed to allow developers to manage GitHub repositories, edit code, and **upload files directly from a smartphone** when away from a laptop.

---

## Features

1. **GitHub Authentication**:
   - OAuth 2.0 flow & Personal Access Token support.
   - Credentials stored in encrypted local storage (`SharedPreferences`).

2. **Repository Dashboard**:
   - Displays all GitHub repositories (Public & Private).
   - Shows description, default branch, last updated time, star counts, and badges.
   - **Open Live Demo** button for GitHub Pages sites.
   - **Open on GitHub** button for direct browser navigation.

3. **Repository File Explorer**:
   - Breadcrumb navigation (`Repo > folder > subfolder`).
   - Type-specific file icons & formatted sizes.
   - Branch switching and new branch creation.
   - Up/Back folder navigation and pull-to-refresh.

4. **Upload Files From Phone (Primary Feature)**:
   - Built-in mobile file picker (`file_picker`) for single and multi-file selection from phone storage.
   - Target repository selector & subfolder path picker (`docs/`, `src/`).
   - Live pre-upload file list review and commit message input (`"Add laboratory coursework"`).
   - Direct commit to GitHub API with real-time progress bar.

5. **Mobile Code Editor & File Creation**:
   - Code editor supporting 12+ languages (Python, JS, TS, HTML, CSS, Markdown, JSON, YAML, XML, Shell, Dart, TXT).
   - Line numbers, search within file, undo/redo.
   - Rendered Markdown preview tab and image viewer tab.

6. **Folder Creation & File Deletion**:
   - Create directories via placeholder `.gitkeep` commits.
   - Delete files with confirmation dialog.

7. **Pre-Commit Verification System**:
   - Standardized modal preview before any repository modification displaying Repository, Target Branch, Changed Files, and Commit Message.

8. **Mobile Dark UI**:
   - Mobile-first layout with bottom navigation bar: **Home**, **Repositories**, **Search**, **Activity**, **Settings**.
   - Sleek dark theme (`#0D1117`) with Cyan (`#00F2FE`) and Teal (`#4FACFE`) accents.

---

## Directory Structure

```
mobile-git-workspace/
├── backend/
│   ├── app/
│   │   ├── api/          # Route handlers (auth, repos, files)
│   │   ├── services/     # GitHub REST API service wrapper
│   │   ├── models/       # Pydantic schemas
│   │   └── main.py       # FastAPI application
│   └── requirements.txt
│
└── mobile/
    ├── lib/
    │   ├── models/       # Data models
    │   ├── services/     # API & auth services
    │   ├── theme/        # Mobile dark theme
    │   ├── widgets/      # Pre-commit modal, file icon, cards
    │   ├── screens/      # Home, Repos, Explorer, Upload, Editor, Search, Activity, Settings
    │   └── main.dart
    └── pubspec.yaml
```

---

## How to Run

### 1. Run Backend Server (FastAPI)
```bash
cd mobile-git-workspace/backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Backend endpoints will be available at: `http://localhost:8000` (API Docs at `http://localhost:8000/docs`).

### 2. Run Mobile Frontend (Flutter)
```bash
cd mobile-git-workspace/mobile
flutter run -d chrome   # Or run on Android/iOS device
```
