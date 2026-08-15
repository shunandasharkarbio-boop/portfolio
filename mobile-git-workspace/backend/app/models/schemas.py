from typing import Optional, List
from pydantic import BaseModel, Field

class TokenVerifyRequest(BaseModel):
    token: str

class UserProfile(BaseModel):
    login: str
    id: int
    avatar_url: str
    name: Optional[str] = None
    email: Optional[str] = None
    public_repos: int = 0
    total_private_repos: int = 0

class RepoSummary(BaseModel):
    id: int
    name: str
    full_name: str
    owner: str
    private: bool
    description: Optional[str] = ""
    default_branch: str = "main"
    updated_at: str
    stargazers_count: int = 0
    forks_count: int = 0
    language: Optional[str] = None
    html_url: str
    has_pages: bool = False
    pages_url: Optional[str] = None

class FileExplorerItem(BaseModel):
    name: str
    path: str
    sha: str
    size: int = 0
    type: str  # "file" or "dir"
    download_url: Optional[str] = None
    html_url: Optional[str] = None

class FileDetailResponse(BaseModel):
    name: str
    path: str
    sha: str
    size: int
    encoding: Optional[str] = "base64"
    content_b64: Optional[str] = None
    is_text: bool = True
    html_url: str
    download_url: Optional[str] = None

class CommitPayload(BaseModel):
    owner: str
    repo: str
    path: str
    message: str
    content_b64: str
    branch: str = "main"
    sha: Optional[str] = None  # Required if updating an existing file

class CreateFolderPayload(BaseModel):
    owner: str
    repo: str
    folder_path: str
    file_name: Optional[str] = ".gitkeep"
    message: str
    content: Optional[str] = ""
    branch: str = "main"

class DeleteFilePayload(BaseModel):
    owner: str
    repo: str
    path: str
    message: str
    sha: str
    branch: str = "main"

class CreateBranchPayload(BaseModel):
    owner: str
    repo: str
    new_branch: str
    base_branch: str = "main"

class BranchInfo(BaseModel):
    name: str
    commit_sha: str
    protected: bool = False

class CommitHistoryItem(BaseModel):
    sha: str
    message: str
    author_name: str
    author_avatar: Optional[str] = None
    date: str
    html_url: str

class ActivityItem(BaseModel):
    id: str
    action_type: str  # upload, create, update, delete, branch
    repo_name: str
    file_path: str
    commit_message: str
    timestamp: str
    branch: str
