import base64
from fastapi import APIRouter, Header, HTTPException, Query, UploadFile, File, Form
from typing import List, Optional, Union
from app.models.schemas import (
    FileExplorerItem, FileDetailResponse, CommitPayload,
    CreateFolderPayload, DeleteFilePayload
)
from app.services.github_service import GitHubService

router = APIRouter(prefix="/api/files", tags=["files"])

def _extract_token(authorization: Optional[str]) -> str:
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    return authorization

TEXT_EXTENSIONS = {
    ".md", ".txt", ".py", ".js", ".ts", ".jsx", ".tsx", ".html", ".css",
    ".json", ".yaml", ".yml", ".xml", ".sh", ".bash", ".c", ".cpp", ".h",
    ".java", ".kt", ".dart", ".go", ".rs", ".php", ".rb", ".sql", ".env",
    ".gitignore", ".config"
}

@router.get("/contents/{owner}/{repo}")
async def get_contents(
    owner: str,
    repo: str,
    path: str = Query(""),
    ref: str = Query(""),
    authorization: Optional[str] = Header(None)
):
    token = _extract_token(authorization)
    data = await GitHubService.get_repo_contents(token, owner, repo, path=path, ref=ref)
    
    if isinstance(data, list):
        # Directory contents
        items: List[FileExplorerItem] = []
        for item in data:
            items.append(
                FileExplorerItem(
                    name=item.get("name", ""),
                    path=item.get("path", ""),
                    sha=item.get("sha", ""),
                    size=item.get("size", 0),
                    type=item.get("type", "file"),
                    download_url=item.get("download_url"),
                    html_url=item.get("html_url")
                )
            )
        # Sort folders first, then files alphabetically
        items.sort(key=lambda x: (0 if x.type == "dir" else 1, x.name.lower()))
        return {"is_file": False, "items": items, "path": path}

    elif isinstance(data, dict):
        # Single File details
        name = data.get("name", "")
        file_path = data.get("path", "")
        size = data.get("size", 0)
        sha = data.get("sha", "")
        content_b64 = data.get("content", "")
        
        # Check text extension or base64 decoding
        ext = "." + name.split(".")[-1].lower() if "." in name else ""
        is_text = ext in TEXT_EXTENSIONS or data.get("encoding") == "base64"
        
        return {
            "is_file": True,
            "file": FileDetailResponse(
                name=name,
                path=file_path,
                sha=sha,
                size=size,
                encoding=data.get("encoding", "base64"),
                content_b64=content_b64,
                is_text=is_text,
                html_url=data.get("html_url", ""),
                download_url=data.get("download_url")
            )
        }
    
    return {"is_file": False, "items": [], "path": path}

@router.post("/commit/{owner}/{repo}")
async def commit_file(
    owner: str,
    repo: str,
    payload: CommitPayload,
    authorization: Optional[str] = Header(None)
):
    token = _extract_token(authorization)
    result = await GitHubService.create_or_update_file(
        token=token,
        owner=owner,
        repo=repo,
        path=payload.path,
        message=payload.message,
        content_b64=payload.content_b64,
        branch=payload.branch,
        sha=payload.sha
    )
    return {
        "status": "success",
        "message": f"Successfully committed {payload.path}",
        "commit_sha": result.get("commit", {}).get("sha", "")
    }

@router.post("/upload/{owner}/{repo}")
async def upload_files_from_phone(
    owner: str,
    repo: str,
    files: List[UploadFile] = File(...),
    folder_path: str = Form(""),
    message: str = Form("Add files via Mobile Git Workspace"),
    branch: str = Form("main"),
    authorization: Optional[str] = Header(None)
):
    token = _extract_token(authorization)
    committed_files = []
    
    clean_folder = folder_path.strip().strip("/")
    
    for f in files:
        raw_bytes = await f.read()
        b64_content = base64.b64encode(raw_bytes).decode("utf-8")
        
        file_path = f"{clean_folder}/{f.filename}" if clean_folder else f.filename
        commit_msg = message if len(files) == 1 else f"{message} ({f.filename})"

        res = await GitHubService.create_or_update_file(
            token=token,
            owner=owner,
            repo=repo,
            path=file_path,
            message=commit_msg,
            content_b64=b64_content,
            branch=branch
        )
        committed_files.append({
            "filename": f.filename,
            "path": file_path,
            "commit_sha": res.get("commit", {}).get("sha", "")
        })

    return {
        "status": "success",
        "count": len(committed_files),
        "files": committed_files,
        "branch": branch
    }

@router.post("/folder/{owner}/{repo}")
async def create_folder(
    owner: str,
    repo: str,
    payload: CreateFolderPayload,
    authorization: Optional[str] = Header(None)
):
    token = _extract_token(authorization)
    clean_folder = payload.folder_path.strip().strip("/")
    file_name = payload.file_name or ".gitkeep"
    target_path = f"{clean_folder}/{file_name}"
    
    raw_content = payload.content or ""
    b64_content = base64.b64encode(raw_content.encode("utf-8")).decode("utf-8")
    
    res = await GitHubService.create_or_update_file(
        token=token,
        owner=owner,
        repo=repo,
        path=target_path,
        message=payload.message or f"Create folder {clean_folder}",
        content_b64=b64_content,
        branch=payload.branch
    )
    return {
        "status": "success",
        "folder": clean_folder,
        "created_file": target_path,
        "commit_sha": res.get("commit", {}).get("sha", "")
    }

@router.post("/delete/{owner}/{repo}")
async def delete_file(
    owner: str,
    repo: str,
    payload: DeleteFilePayload,
    authorization: Optional[str] = Header(None)
):
    token = _extract_token(authorization)
    res = await GitHubService.delete_file(
        token=token,
        owner=owner,
        repo=repo,
        path=payload.path,
        message=payload.message,
        sha=payload.sha,
        branch=payload.branch
    )
    return {
        "status": "success",
        "message": f"Deleted {payload.path}",
        "commit_sha": res.get("commit", {}).get("sha", "")
    }
