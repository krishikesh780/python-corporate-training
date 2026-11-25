"""Step 1b — DeepSeek API hello. Key: https://platform.deepseek.com/"""

import os
from pathlib import Path

import requests
from dotenv import load_dotenv

from deepseek_client import chat

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def main() -> None:
    key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    if not key:
        print("Set DEEPSEEK_API_KEY in week6/.env (see .env.example)")
        return

    try:
        print(chat("Say one line: why RAG helps enterprise chatbots.", api_key=key))
    except requests.HTTPError as exc:
        print("DeepSeek error:", exc.response.text if exc.response else exc)
    except Exception as exc:
        print("Error:", exc)


if __name__ == "__main__":
    main()