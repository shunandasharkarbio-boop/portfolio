import base64
import httpx
from typing import List, Dict, Any, Optional
from fastapi import HTTPException, status

GITHUB_API_BASE = "https://api.github.com"

class GitHubService:
    @staticmethod
    def _headers(token: str) -> Dict[str, str]:
        clean_token = token.strip()
        if clean_token.startswith("Bearer ") or clean_token.startswith("token "):
            auth_val = clean_token
        else:
            auth_val = f"Bearer {clean_token}"
        return {
            "Authorization": auth_val,
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "MobileGitWorkspace/1.0"
        }

    @classmethod
    async def get_user_profile(cls, token: str) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            res = await client.get(f"{GITHUB_API_BASE}/user", headers=cls._headers(token))
            if res.status_code != 200:
                raise HTTPException(
                    status_code=res.status_code,
                    detail=f"GitHub API Error: {res.json().get('message', res.text)}"
                )
            return res.json()

    @classmethod
    async def get_user_repos(
        cls, token: str, page: int = 1, per_page: int = 100, sort: str = "updated"
    ) -> List[Dict[str, Any]]:
        async with httpx.AsyncClient() as client:
            params = {
                "page": page,
                "per_page": per_page,
                "sort": sort,
                "affiliation": "owner,collaborator,organization_member"
            }
            res = await client.get(
                f"{GITHUB_API_BASE}/user/repos",
                headers=cls._headers(token),
                params=params
            )
            if res.status_code != 200:
                raise HTTPException(
                    status_code=res.status_code,
                    detail=f"GitHub API Error fetching repos: {res.json().get('message', res.text)}"
                )
            return res.json()

    @classmethod
    async def get_repo_contents(
        cls, token: str, owner: str, repo: str, path: str = "", ref: str = ""
    ) -> Any:
        async with httpx.AsyncClient() as client:
            url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}".rstrip("/")
            params = {}
            if ref:
                params["ref"] = ref
            res = await client.get(url, headers=cls._headers(token), params=params)
            if res.status_code == 404:
                return []
            if res.status_code != 200:
                raise HTTPException(
                    status_code=res.status_code,
                    detail=f"Error fetching contents: {res.json().get('message', res.text)}"
                )
            return res.json()

    @classmethod
    async def create_or_update_file(
        cls,
        token: str,
        owner: str,
        repo: str,
        path: str,
        message: str,
        content_b64: str,
        branch: str = "main",
        sha: Optional[str] = None
    ) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"
            
            # If SHA not provided, try to fetch current SHA to allow update over overwrite
            if not sha:
                try:
                    existing = await cls.get_repo_contents(token, owner, repo, path, ref=branch)
                    if isinstance(existing, dict) and "sha" in existing:
                        sha = existing["sha"]
                except Exception:
                    pass

            body: Dict[str, Any] = {
                "message": message,
                "content": content_b64,
                "branch": branch
            }
            if sha:
                body["sha"] = sha

            res = await client.put(url, headers=cls._headers(token), json=body)
            if res.status_code not in (200, 201):
                raise HTTPException(
                    status_code=res.status_code,
                    detail=f"GitHub commit failed: {res.json().get('message', res.text)}"
                )
            return res.json()

    @classmethod
    async def delete_file(
        cls,
        token: str,
        owner: str,
        repo: str,
        path: str,
        message: str,
        sha: str,
        branch: str = "main"
    ) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"
            body = {
                "message": message,
                "sha": sha,
                "branch": branch
            }
            res = await client.request("DELETE", url, headers=cls._headers(token), json=body)
            if res.status_code != 200:
                raise HTTPException(
                    status_code=res.status_code,
                    detail=f"GitHub delete file failed: {res.json().get('message', res.text)}"
                )
            return res.json()

    @classmethod
    async def get_branches(cls, token: str, owner: str, repo: str) -> List[Dict[str, Any]]:
        async with httpx.AsyncClient() as client:
            url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/branches"
            res = await client.get(url, headers=cls._headers(token))
            if res.status_code != 200:
                raise HTTPException(
                    status_code=res.status_code,
                    detail=f"Error listing branches: {res.json().get('message', res.text)}"
                )
            return res.json()

    @classmethod
    async def create_branch(
        cls, token: str, owner: str, repo: str, new_branch: str, base_branch: str = "main"
    ) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            # 1. Get base ref commit sha
            ref_url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/git/ref/heads/{base_branch}"
            ref_res = await client.get(ref_url, headers=cls._headers(token))
            if ref_res.status_code != 200:
                raise HTTPException(
                    status_code=ref_res.status_code,
                    detail=f"Failed to find base branch '{base_branch}': {ref_res.text}"
                )
            base_sha = ref_res.json()["object"]["sha"]

            # 2. Create new branch ref
            create_url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/git/refs"
            create_body = {
                "ref": f"refs/heads/{new_branch}",
                "sha": base_sha
            }
            res = await client.post(create_url, headers=cls._headers(token), json=create_body)
            if res.status_code != 201:
                raise HTTPException(
                    status_code=res.status_code,
                    detail=f"Failed to create branch '{new_branch}': {res.json().get('message', res.text)}"
                )
            return res.json()

    @classmethod
    async def get_commits(
        cls, token: str, owner: str, repo: str, branch: str = "main", per_page: int = 20
    ) -> List[Dict[str, Any]]:
        async with httpx.AsyncClient() as client:
            url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/commits"
            params = {"sha": branch, "per_page": per_page}
            res = await client.get(url, headers=cls._headers(token), params=params)
            if res.status_code != 200:
                return []
            return res.json()

    @classmethod
    async def get_pages_site(cls, token: str, owner: str, repo: str) -> Optional[Dict[str, Any]]:
        async with httpx.AsyncClient() as client:
            url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pages"
            res = await client.get(url, headers=cls._headers(token))
            if res.status_code == 200:
                return res.json()
            return None
