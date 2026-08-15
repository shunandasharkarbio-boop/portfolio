from fastapi import APIRouter, Header, HTTPException, Query
from typing import List, Optional
from app.models.schemas import RepoSummary, BranchInfo, CreateBranchPayload, CommitHistoryItem
from app.services.github_service import GitHubService

router = APIRouter(prefix="/api/repos", tags=["repos"])

def _extract_token(authorization: Optional[str]) -> str:
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    return authorization

@router.get("", response_model=List[RepoSummary])
async def list_repositories(
    authorization: Optional[str] = Header(None),
    page: int = Query(1, ge=1),
    per_page: int = Query(100, le=100),
    search: Optional[str] = None
):
    token = _extract_token(authorization)
    repos_raw = await GitHubService.get_user_repos(token, page=page, per_page=per_page)
    
    results: List[RepoSummary] = []
    for r in repos_raw:
        name = r.get("name", "")
        owner = r.get("owner", {}).get("login", "")
        description = r.get("description") or ""
        
        # Filter by search if provided
        if search:
            q = search.lower()
            if q not in name.lower() and q not in description.lower():
                continue
                
        has_pages = r.get("has_pages", False)
        pages_url = f"https://{owner}.github.io/{name}" if has_pages else None

        results.append(
            RepoSummary(
                id=r.get("id", 0),
                name=name,
                full_name=r.get("full_name", f"{owner}/{name}"),
                owner=owner,
                private=r.get("private", False),
                description=description,
                default_branch=r.get("default_branch", "main"),
                updated_at=r.get("updated_at", ""),
                stargazers_count=r.get("stargazers_count", 0),
                forks_count=r.get("forks_count", 0),
                language=r.get("language"),
                html_url=r.get("html_url", f"https://github.com/{owner}/{name}"),
                has_pages=has_pages,
                pages_url=pages_url
            )
        )
    return results

@router.get("/{owner}/{repo}", response_model=RepoSummary)
async def get_repository_details(
    owner: str,
    repo: str,
    authorization: Optional[str] = Header(None)
):
    token = _extract_token(authorization)
    # Check Pages
    pages_info = await GitHubService.get_pages_site(token, owner, repo)
    has_pages = pages_info is not None
    pages_url = pages_info.get("html_url") if pages_info else f"https://{owner}.github.io/{repo}" if has_pages else None
    
    # We can fetch contents or basic info
    contents = await GitHubService.get_repo_contents(token, owner, repo, "")
    
    return RepoSummary(
        id=0,
        name=repo,
        full_name=f"{owner}/{repo}",
        owner=owner,
        private=False,  # Default
        description=f"Repository {owner}/{repo}",
        default_branch="main",
        updated_at="",
        html_url=f"https://github.com/{owner}/{repo}",
        has_pages=has_pages,
        pages_url=pages_url
    )

@router.get("/{owner}/{repo}/branches", response_model=List[BranchInfo])
async def list_branches(
    owner: str,
    repo: str,
    authorization: Optional[str] = Header(None)
):
    token = _extract_token(authorization)
    branches_raw = await GitHubService.get_branches(token, owner, repo)
    res = []
    for b in branches_raw:
        res.append(
            BranchInfo(
                name=b.get("name", ""),
                commit_sha=b.get("commit", {}).get("sha", ""),
                protected=b.get("protected", False)
            )
        )
    return res

@router.post("/{owner}/{repo}/branches")
async def create_branch(
    owner: str,
    repo: str,
    payload: CreateBranchPayload,
    authorization: Optional[str] = Header(None)
):
    token = _extract_token(authorization)
    res = await GitHubService.create_branch(
        token, owner, repo, payload.new_branch, payload.base_branch
    )
    return {"status": "success", "branch": payload.new_branch, "ref": res.get("ref")}

@router.get("/{owner}/{repo}/commits", response_model=List[CommitHistoryItem])
async def list_commits(
    owner: str,
    repo: str,
    branch: str = Query("main"),
    authorization: Optional[str] = Header(None)
):
    token = _extract_token(authorization)
    commits_raw = await GitHubService.get_commits(token, owner, repo, branch=branch)
    res = []
    for c in commits_raw:
        commit_obj = c.get("commit", {})
        author_obj = c.get("author") or {}
        res.append(
            CommitHistoryItem(
                sha=c.get("sha", "")[:7],
                message=commit_obj.get("message", "").split("\n")[0],
                author_name=commit_obj.get("author", {}).get("name", "Unknown"),
                author_avatar=author_obj.get("avatar_url"),
                date=commit_obj.get("author", {}).get("date", ""),
                html_url=c.get("html_url", "")
            )
        )
    return res
