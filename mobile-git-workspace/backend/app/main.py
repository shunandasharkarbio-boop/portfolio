import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv

load_dotenv()

from app.api import auth, repos, files

app = FastAPI(
    title="Mobile Git Workspace Backend",
    description="Backend service for Mobile Git Workspace app handling GitHub OAuth, API proxying, and file uploads.",
    version="1.0.0"
)

# Enable CORS for Mobile web & native apps
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(repos.router)
app.include_router(files.router)

@app.get("/api/health")
def health_check():
    return {
        "status": "online",
        "app": "Mobile Git Workspace Backend",
        "version": "1.0.0"
    }

# Serve Flutter Web app build if built in static directory
WEB_BUILD_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "mobile", "build", "web")
if os.path.exists(WEB_BUILD_DIR):
    app.mount("/app", StaticFiles(directory=WEB_BUILD_DIR, html=True), name="static_web")

    @app.get("/")
    def serve_root():
        return FileResponse(os.path.join(WEB_BUILD_DIR, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
