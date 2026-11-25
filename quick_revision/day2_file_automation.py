"""
Quick Revision — Day 2: File & automation modules
================================================
os, pathlib, shutil, requests, subprocess, logging, datetime.
Full course: ../week3/day1–day3
"""

import logging
import os
import shutil
import subprocess
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests

_LAB = Path(__file__).resolve().parent / "_lab"


def demo_os_pathlib() -> None:
    print("cwd:", os.getcwd())
    _LAB.mkdir(parents=True, exist_ok=True)
    p = _LAB / "pathlib_demo.txt"
    p.write_text("Hello Pathlib", encoding="utf-8")
    print("exists:", p.exists(), "| name:", p.name)


def demo_shutil() -> None:
    src = _LAB / "copy_src.txt"
    dst = _LAB / "copy_dst.txt"
    src.write_text("copy me", encoding="utf-8")
    shutil.copy(src, dst)
    print("shutil.copy:", dst.read_text(encoding="utf-8"))


def demo_requests() -> None:
    try:
        r = requests.get("https://httpbin.org/get", params={"q": "revision"}, timeout=8)
        print("HTTP", r.status_code, "| url key:", r.json().get("args"))
    except requests.RequestException as exc:
        print("requests skipped:", exc)


def demo_requests_retry() -> None:
    def fetch_with_retry(url: str, retries: int = 3):
        for attempt in range(1, retries + 1):
            try:
                return requests.get(url, timeout=5).json()
            except requests.RequestException as exc:
                print(f"  attempt {attempt}:", exc)
                time.sleep(1)
        return None

    data = fetch_with_retry("https://httpbin.org/json")
    print("retry ok:", bool(data))


def demo_subprocess() -> None:
    result = subprocess.run(
        ["python", "--version"], capture_output=True, text=True, check=False
    )
    print("subprocess:", result.stdout.strip() or result.stderr.strip())


def demo_logging() -> None:
    log_file = _LAB / "revision.log"
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
        force=True,
    )
    logging.info("revision demo")
    print("log written:", log_file)


def demo_datetime() -> None:
    now = datetime.now()
    print("now:", now.strftime("%d-%m-%Y %H:%M:%S"))
    print("+10 min:", (now + timedelta(minutes=10)).time())


def run_revision() -> None:
    demo_os_pathlib()
    demo_shutil()
    demo_requests()
    demo_requests_retry()
    demo_subprocess()
    demo_logging()
    demo_datetime()


if __name__ == "__main__":
    run_revision()