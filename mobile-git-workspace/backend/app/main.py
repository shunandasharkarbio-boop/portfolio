import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv

load_dotenv()

from app.api import auth, repos, files, ai

app = FastAPI(
    title="Portfolio AI Assistant & Mobile Git Workspace Backend",
    description="Backend service supporting GitHub OAuth, API proxying, Android uploads, and AI repository analysis.",
    version="1.0.0"
)

# Enable CORS for Mobile web, native Android apps, and Wi-Fi devices
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
app.include_router(ai.router)

@app.get("/api/health")
def health_check():
    return {
        "status": "online",
        "app": "Portfolio AI Assistant Backend",
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
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host=host, port=port, reload=True)
