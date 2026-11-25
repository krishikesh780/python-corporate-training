"""
Scheduled automation job — runs locally, in GitHub Actions, or after Cloud Scheduler HTTP hit.

  python run_job.py
  python run_job.py --notify
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_runs"


def write_report(status: str, detail: str = "") -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = OUT / f"job_{stamp}.json"
    payload = {
        "status": status,
        "utc": stamp,
        "detail": detail,
        "trigger": os.getenv("GITHUB_EVENT_NAME", "local"),
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def maybe_notify(report: Path) -> None:
    url = os.getenv("AUTOMATION_WEBHOOK_URL", "").strip()
    if not url:
        print("Skip notify (set AUTOMATION_WEBHOOK_URL)")
        return
    try:
        import requests

        body = json.loads(report.read_text(encoding="utf-8"))
        r = requests.post(url, json=body, timeout=15)
        print("Webhook:", r.status_code)
    except Exception as exc:
        print("Webhook failed:", exc)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--notify", action="store_true", help="POST report to AUTOMATION_WEBHOOK_URL")
    args = parser.parse_args()

    print("Automation job started (UTC)", datetime.now(timezone.utc).isoformat())
    # Demo task: ping week5 regression idea (no DB required in CI)
    detail = "ok — replace with your ETL / RAG / tests"
    report = write_report("success", detail)
    print("Report:", report)

    if args.notify or os.getenv("AUTOMATION_NOTIFY") == "1":
        maybe_notify(report)

    print("Automation job finished")
    return 0


if __name__ == "__main__":
    sys.exit(main())