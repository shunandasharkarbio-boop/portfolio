import os
import httpx
from fastapi import APIRouter, HTTPException, Query, Header
from typing import Optional
from app.models.schemas import TokenVerifyRequest, UserProfile
from app.services.github_service import GitHubService

router = APIRouter(prefix="/api/auth", tags=["auth"])

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET", "")

@router.get("/github/url")
def get_github_oauth_url(redirect_uri: Optional[str] = None):
    if not GITHUB_CLIENT_ID:
        return {
            "oauth_available": False,
            "message": "OAuth Client ID not configured. Please use Personal Access Token."
        }
    scope = "repo,user,read:user"
    url = f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&scope={scope}"
    if redirect_uri:
        url += f"&redirect_uri={redirect_uri}"
    return {
        "oauth_available": True,
        "url": url
    }

@router.get("/github/callback")
async def github_oauth_callback(code: str = Query(...)):
    if not GITHUB_CLIENT_ID or not GITHUB_CLIENT_SECRET:
        raise HTTPException(
            status_code=400,
            detail="OAuth credentials missing on backend server."
        )
    
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://github.com/login/oauth/access_token",
            headers={"Accept": "application/json"},
            data={
                "client_id": GITHUB_CLIENT_ID,
                "client_secret": GITHUB_CLIENT_SECRET,
                "code": code
            }
        )
        if res.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to exchange GitHub OAuth code.")
        
        data = res.json()
        access_token = data.get("access_token")
        if not access_token:
            error_desc = data.get("error_description", "Unknown OAuth error")
            raise HTTPException(status_code=400, detail=f"OAuth failed: {error_desc}")

        # Fetch profile
        profile = await GitHubService.get_user_profile(access_token)
        return {
            "token": access_token,
            "token_type": data.get("token_type", "bearer"),
            "user": profile
        }

@router.post("/verify", response_model=UserProfile)
async def verify_token(req: TokenVerifyRequest):
    profile = await GitHubService.get_user_profile(req.token)
    return UserProfile(
        login=profile.get("login", ""),
        id=profile.get("id", 0),
        avatar_url=profile.get("avatar_url", ""),
        name=profile.get("name"),
        email=profile.get("email"),
        public_repos=profile.get("public_repos", 0),
        total_private_repos=profile.get("total_private_repos", 0)
    )
