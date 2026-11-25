"""Mini RAG demo with DeepSeek — pass your text file as context."""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from deepseek_client import chat

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

RAG_TEMPLATE = """Answer ONLY using the context below. If missing, say "Not in document".

Context:
{context}

Question: {question}
"""


def load_context(path: Path) -> str:
    return path.read_text(encoding="utf-8")[:8000]


def simple_chunks(text: str, size: int = 600) -> list[str]:
    words = text.split()
    chunks: list[str] = []
    for i in range(0, len(words), size):
        chunks.append(" ".join(words[i : i + size]))
    return chunks or [text]


def pick_chunks(chunks: list[str], question: str, k: int = 3) -> str:
    q = set(question.lower().split())
    scored = []
    for c in chunks:
        words = set(c.lower().split())
        scored.append((len(q & words), c))
    scored.sort(key=lambda x: x[0], reverse=True)
    top = [c for _, c in scored[:k]]
    return "\n---\n".join(top)


def main() -> None:
    key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    if not key:
        print("Set DEEPSEEK_API_KEY in week6/.env")
        return

    context_file = Path(__file__).with_name("sample_context.txt")
    if not context_file.exists():
        context_file.write_text(
            "Our insurance policy POL123 covers health up to 500000. "
            "Claims must be filed within 30 days. Premium is due monthly.",
            encoding="utf-8",
        )

    text = load_context(context_file)
    question = sys.argv[1] if len(sys.argv) > 1 else "What is the claim deadline?"
    context = pick_chunks(simple_chunks(text), question)
    prompt = RAG_TEMPLATE.format(context=context, question=question)

    print(chat(prompt, api_key=key, system="You are a helpful document assistant."))


if __name__ == "__main__":
    main()