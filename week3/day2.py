"""
Week 3 — Day 2: Paths & OS (File System)
========================================

PYTHON CLASSROOM
----------------
1. Absolute vs relative paths
2. os.getcwd(), os.listdir()
3. os.path.join() — cross-platform paths
4. Create folder / check exists / isfile / isdir
5. Demo write via joined path
6. Organize files by extension (lab folder)
7. Practice P1–P5

PYTHON RECALL
-------------
- Never hard-code `C:\\...` only — use join + cwd for portability.
- Prefer pathlib in new code; os.path still common in legacy repos.
- File *content* read/write: week3/day3.py (not repeated here).
- Error handling on I/O: week3/day1.py.
"""

import os
import shutil
from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent / "_classroom_lab" / "day2"


def demo_absolute_vs_relative() -> None:
    absolute = Path.home() / "Desktop" / "sample.txt"
    relative = Path("sample.txt")
    print("Absolute (example):", absolute)
    print("Relative:", relative)


def demo_cwd_and_list() -> None:
    print("Current directory:", os.getcwd())
    week3 = Path(__file__).resolve().parent
    names = sorted(os.listdir(week3))[:8]
    print("week3 (first 8 entries):", names, "...")


def demo_path_join() -> None:
    base = _LAB_DIR
    joined = os.path.join(base, "myfolder", "data.txt")
    print("Joined path:", joined)


def demo_create_and_write() -> None:
    _LAB_DIR.mkdir(parents=True, exist_ok=True)
    folder = _LAB_DIR / "myfolder"
    folder.mkdir(exist_ok=True)
    file_path = folder / "notes.txt"
    file_path.write_text("Created using pathlib + os.path.join pattern.\n", encoding="utf-8")
    print("File created at:", file_path)
    print("Exists?", file_path.exists())
    print("Is file?", file_path.is_file())
    print("Is dir?", folder.is_dir())


def demo_organize_by_extension() -> None:
    """Creates sample files, moves into organized/<ext>/ — all under _classroom_lab/day2."""
    staging = _LAB_DIR / "staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    test_files = ["report.docx", "data.csv", "image.png", "notes.txt"]
    for fname in test_files:
        (staging / fname).write_text("Demo content", encoding="utf-8")

    organized_root = staging / "organized"
    for fname in test_files:
        ext = fname.rsplit(".", 1)[-1]
        ext_folder = organized_root / ext
        ext_folder.mkdir(parents=True, exist_ok=True)
        src = staging / fname
        dest = ext_folder / fname
        shutil.move(str(src), str(dest))
        print(f"Moved {fname} → {ext_folder.name}/")

    print("Organized under:", organized_root)


# PYTHON RECALL — Practice (P1–P5)
# P1: List only .py files in week3 with endswith / pathlib.glob.
# P2: Walk a folder with os.walk (print dirs + files count).
# P3: os.path.basename vs dirname on a full path.
# P4: Create nested dirs with os.makedirs(..., exist_ok=True).
# P5: Check file size with os.path.getsize.

def run_classroom_demo() -> None:
    demo_absolute_vs_relative()
    demo_cwd_and_list()
    demo_path_join()
    demo_create_and_write()
    demo_organize_by_extension()


if __name__ == "__main__":
    run_classroom_demo()