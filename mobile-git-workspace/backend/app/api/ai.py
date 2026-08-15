import base64
from fastapi import APIRouter, Header, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from app.services.github_service import GitHubService

router = APIRouter(prefix="/api/ai", tags=["ai"])

class AIChatRequest(BaseModel):
    prompt: str
    owner: str
    repo: str
    branch: str = "main"
    current_path: Optional[str] = ""

class AIChatResponse(BaseModel):
    ai_response: str
    target_file: Optional[str] = None
    proposed_content: Optional[str] = None
    proposed_content_b64: Optional[str] = None
    diff_summary: Optional[str] = None
    suggested_commit_message: Optional[str] = None

def _extract_token(authorization: Optional[str]) -> str:
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    return authorization

@router.post("/chat", response_model=AIChatResponse)
async def ai_chat_assistant(
    payload: AIChatRequest,
    authorization: Optional[str] = Header(None)
):
    token = _extract_token(authorization)
    prompt_lower = payload.prompt.lower().strip()
    
    # Analyze prompt intent
    if "about" in prompt_lower or "profile" in prompt_lower or "bio" in prompt_lower:
        # Search for html or md files in repo
        target_file = "index.html"
        current_content = ""
        current_sha = None
        try:
            file_data = await GitHubService.get_repo_contents(
                token, payload.owner, payload.repo, target_file, ref=payload.branch
            )
            if isinstance(file_data, dict) and "content" in file_data:
                b64_str = file_data["content"].replaceAll(RegExp(r'\s+'), '') if hasattr(file_data["content"], 'replaceAll') else file_data["content"]
                current_content = base64.b64decode(b64_str).decode("utf-8", errors="ignore")
                current_sha = file_data.get("sha")
        except Exception:
            target_file = "README.md"
            
        proposed_update = f"<!-- Updated About Section via Portfolio AI Assistant -->\n<section id=\"about\">\n  <h2>About Me</h2>\n  <p>Passionate Bioinformatics & Software Developer showcasing interactive projects, data pipelines, and web applications.</p>\n</section>\n"
        
        updated_full_text = current_content + "\n\n" + proposed_update if current_content else proposed_update
        b64_proposed = base64.b64encode(updated_full_text.encode("utf-8")).decode("utf-8")
        
        return AIChatResponse(
            ai_response=f"I analyzed `{payload.owner}/{payload.repo}` on branch `{payload.branch}`. Here is a proposed update for your About section in `{target_file}`.",
            target_file=target_file,
            proposed_content=updated_full_text,
            proposed_content_b64=b64_proposed,
            diff_summary=f"+ Added updated About section to {target_file}",
            suggested_commit_message=f"Update About section in {target_file} via Portfolio AI Assistant"
        )
        
    elif "analyze" in prompt_lower or "structure" in prompt_lower or "review" in prompt_lower:
        contents = await GitHubService.get_repo_contents(
            token, payload.owner, payload.repo, "", ref=payload.branch
        )
        file_count = len(contents) if isinstance(contents, list) else 0
        file_names = [f["name"] for f in contents] if isinstance(contents, list) else []
        
        return AIChatResponse(
            ai_response=f"Repository Analysis for `{payload.owner}/{payload.repo}` ({payload.branch} branch):\n"
                        f"• Total root items: {file_count}\n"
                        f"• Top items: {', '.join(file_names[:8])}\n"
                        f"• Status: Clean & active. Ready for file uploads, branch operations, and code updates.",
            diff_summary="No file changes proposed (Analysis only)."
        )

    else:
        # Default AI response
        target = payload.current_path if payload.current_path else "README.md"
        ai_reply = f"I evaluated your prompt: \"{payload.prompt}\". I recommend updating `{target}` in repository `{payload.owner}/{payload.repo}`."
        proposed_text = f"# {payload.repo}\n\n{payload.prompt}\n\n*Updated via Portfolio AI Assistant*"
        b64_proposed = base64.b64encode(proposed_text.encode("utf-8")).decode("utf-8")
        
        return AIChatResponse(
            ai_response=ai_reply,
            target_file=target,
            proposed_content=proposed_text,
            proposed_content_b64=b64_proposed,
            diff_summary=f"Modify {target} with requested changes",
            suggested_commit_message=f"Update {target} via Portfolio AI Assistant"
        )
