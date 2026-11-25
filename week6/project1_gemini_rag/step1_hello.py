"""Step 1 — Gemini API hello. Needs: pip install google-genai python-dotenv"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def main() -> None:
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        print("Set GEMINI_API_KEY in week6/.env (see .env.example)")
        return

    try:
        from google import genai
    except ImportError:
        print("Run: pip install google-genai")
        return

    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Say one line: why RAG helps enterprise chatbots.",
    )
    print(response.text)


if __name__ == "__main__":
    main()