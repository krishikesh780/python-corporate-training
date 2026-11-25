"""
Week 4 — Day 4: GitHub, Secrets & CI/CD Intro
=============================================

PYTHON CLASSROOM
----------------
1. .gitignore patterns
2. .env + python-dotenv (never commit secrets)
3. GitHub: remote, branch push, Pull Request flow
4. GitHub Actions YAML skeleton
5. Practice P1–P5

PYTHON RECALL
-------------
- git add/commit basics: week4/day3.py.
- Sample workflow file: week4/day5/project3/.github/workflows/ci.yml
- Store API keys in GitHub Secrets for Actions: ${{ secrets.NAME }}
- OOP insurance package layout: day5/project3/docs.md
"""

from pathlib import Path

GITIGNORE_AND_SECRETS = """
# .gitignore examples
__pycache__/
*.pyc
.env
.vscode/
.DS_Store

# Python + dotenv (after pip install python-dotenv)
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")   # never hard-code in source
"""

GITHUB_WORKFLOW = """
git remote add origin <repo-url>
git push -u origin main
git checkout -b feature-x
git push origin feature-x
# → Open Pull Request on GitHub → review → merge
# Link issues with #42 in PR description
"""

CICD_INTRO = """
# .github/workflows/python-app.yml (concept)
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest
"""


def demo_gitignore_and_secrets() -> None:
    print("=== .gitignore & secrets ===")
    print(GITIGNORE_AND_SECRETS)


def demo_github_flow() -> None:
    print("=== GitHub workflow ===")
    print(GITHUB_WORKFLOW)


def demo_cicd_skeleton() -> None:
    print("=== CI/CD intro ===")
    print(CICD_INTRO)
    ci_path = Path(__file__).resolve().parent / "day5" / "project3" / ".github" / "workflows" / "ci.yml"
    if ci_path.exists():
        print("Project CI file:", ci_path)


# PYTHON RECALL — Practice (P1–P5)
# P1: Write .gitignore for a Python + Excel data project.
# P2: Load OLD_CUSTOMERS from .env in project3.
# P3: Open a draft PR checklist (tests, secrets, .gitignore).
# P4: Name three triggers for GitHub Actions (push, PR, schedule).
# P5: Difference between CI and CD in one sentence each.


def run_classroom_demo() -> None:
    demo_gitignore_and_secrets()
    demo_github_flow()
    demo_cicd_skeleton()


if __name__ == "__main__":
    run_classroom_demo()