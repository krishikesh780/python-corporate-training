"""
Week 4 — Day 3: CLI & Git Basics
=================================

PYTHON CLASSROOM
----------------
1. Terminal navigation & files
2. View / create / append text files
3. Environment variables & .env idea
4. Git init → status → add → commit → log
5. Branch checkout / merge (intro)
6. Practice P1–P5

PYTHON RECALL
-------------
- This file prints reference cheatsheets — run commands yourself in terminal.
- Windows: dir, cd, type, echo, set | Linux/macOS: ls, cat, export.
- .gitignore / GitHub / CI: week4/day4.py (not duplicated here).
- OOP week: day1–day2; project: day5.
"""

CLI_BASICS = """
# Navigation & files
pwd / cd                         # pwd (Git Bash); cd (Windows)
ls / dir                         # list entries
cd foldername   |   cd ..        # enter / go up
mkdir project   |   rm file      # create dir / remove (careful)

# View / edit
cat file.txt / type file.txt     # print file
echo Hello > file.txt            # write (overwrite)
echo World >> file.txt           # append

# Environment
export NAME=Ravi   (bash)  |  set NAME=Ravi  (cmd)
echo $NAME / echo %NAME%

# .env (do not commit secrets — see day4)
# DB_USER=admin
# DB_PASS=****
"""

GIT_BASICS = """
# One-time
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Local workflow
git init
git status
git add file.py
git commit -m "Add feature"
git log --oneline

# Branches (intro)
git branch feature
git checkout feature    # or: git switch feature
git merge feature
"""


def demo_cli_reference() -> None:
    print("=== CLI reference (copy into terminal) ===")
    print(CLI_BASICS)


def demo_git_basics_reference() -> None:
    print("=== Git basics (copy into terminal) ===")
    print(GIT_BASICS)


# PYTHON RECALL — Practice (P1–P5)
# P1: Create training/ folder; add notes.txt with echo.
# P2: git init in a scratch folder; two commits with messages.
# P3: Create branch bugfix; switch back to main.
# P4: Show git diff before staging.
# P5: Explain untracked vs modified in git status.

def run_classroom_demo() -> None:
    demo_cli_reference()
    demo_git_basics_reference()


if __name__ == "__main__":
    run_classroom_demo()