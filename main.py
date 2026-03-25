import os
from pathlib import Path

import anthropic
import yaml
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Architect Agent", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

AGENT_DIR = Path(__file__).parent


def load_file(path: Path) -> str:
    if path.exists():
        return path.read_text()
    return ""


def build_system_prompt() -> str:
    """Assemble the full system prompt from agent definition files."""
    agent_yaml = yaml.safe_load(load_file(AGENT_DIR / "agent.yaml"))
    soul = load_file(AGENT_DIR / "SOUL.md")
    rules = load_file(AGENT_DIR / "RULES.md")

    # Load knowledge documents marked as always_load
    knowledge = ""
    knowledge_index = AGENT_DIR / "knowledge" / "index.yaml"
    if knowledge_index.exists():
        index = yaml.safe_load(knowledge_index.read_text())
        for doc in index.get("documents", []):
            if doc.get("always_load"):
                doc_path = AGENT_DIR / "knowledge" / doc["path"]
                content = load_file(doc_path)
                if content:
                    knowledge += f"\n## Knowledge: {doc['path']}\n{content}\n"

    # Load all skills
    skills_text = ""
    skills_dir = AGENT_DIR / "skills"
    if skills_dir.exists():
        for skill_name in sorted(agent_yaml.get("skills", [])):
            skill_file = skills_dir / skill_name / "SKILL.md"
            content = load_file(skill_file)
            if content:
                skills_text += f"\n## Skill: {skill_name}\n{content}\n"

    prompt = f"""# {agent_yaml.get('name', 'Agent')} v{agent_yaml.get('version', '1.0.0')}

{agent_yaml.get('description', '')}

{soul}

{rules}
{skills_text}
{knowledge}"""

    return prompt.strip()


SYSTEM_PROMPT = build_system_prompt()

client = anthropic.Anthropic()


class ChatRequest(BaseModel):
    message: str
    conversation_history: list[dict] = []


class ChatResponse(BaseModel):
    reply: str
    conversation_history: list[dict]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5-20250929")
    max_tokens = int(os.getenv("MAX_TOKENS", "8192"))

    messages = list(req.conversation_history)
    messages.append({"role": "user", "content": req.message})

    try:
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=SYSTEM_PROMPT,
            messages=messages,
        )
    except anthropic.APIError as e:
        raise HTTPException(status_code=502, detail=str(e))

    reply = response.content[0].text
    messages.append({"role": "assistant", "content": reply})

    return ChatResponse(reply=reply, conversation_history=messages)


@app.get("/prompt")
def get_prompt():
    """Preview the assembled system prompt."""
    return {"system_prompt": SYSTEM_PROMPT}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
