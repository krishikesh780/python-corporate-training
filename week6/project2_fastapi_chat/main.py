"""Step 2 — Chat API stub. pip install fastapi uvicorn"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Week6 Chat API")


class ChatIn(BaseModel):
    message: str
    lang: str = "en"


class ChatOut(BaseModel):
    reply: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatOut)
def chat(body: ChatIn):
    # TODO: call Gemini (project1 client) when key is set
    echo = f"[{body.lang}] Echo: {body.message}"
    return ChatOut(reply=echo)


# uvicorn main:app --reload --app-dir week6/project2_fastapi_chat