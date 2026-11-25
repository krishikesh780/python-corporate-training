"""
Week 3 — Day 3: File I/O (Text & EDI)
=====================================

PYTHON CLASSROOM
----------------
1. open(), modes r / w / a
2. read(), readlines(), write()
3. encoding="utf-8" (why it matters)
4. Context manager: with open(...) as f
5. EDI-style segments (~ delimiter)
6. Practice P1–P5

PYTHON RECALL
-------------
- Always specify encoding=utf-8 for text files (Windows default may differ).
- 'w' truncates file; 'a' appends; 'r' read-only.
- Paths / folders: week3/day2.py.
- pandas read_csv / Excel: week3/day5.py (not duplicated here).
- DataFrame analysis: week3/day4.py.
"""

from pathlib import Path

_LAB = Path(__file__).resolve().parent / "_classroom_lab" / "day3"


def _ensure_lab() -> Path:
    _LAB.mkdir(parents=True, exist_ok=True)
    return _LAB


def demo_write_and_read_whole() -> None:
    lab = _ensure_lab()
    path = lab / "data.txt"
    path.write_text("Line1: Hello\nLine2: Python\n", encoding="utf-8")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    print("Full content:\n", content)


def demo_readlines() -> None:
    lab = _ensure_lab()
    path = lab / "data.txt"
    with open(path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            print("stripped:", line.strip())


def demo_append_mode() -> None:
    lab = _ensure_lab()
    path = lab / "log.txt"
    path.write_text("Start\n", encoding="utf-8")
    with open(path, "a", encoding="utf-8") as f:
        f.write("Appended line\n")
    print(path.read_text(encoding="utf-8"))


def demo_encoding_note() -> None:
    print(
        "UTF-8 maps every character (A, अ, emoji) to bytes — "
        "use encoding='utf-8' for consistent corporate pipelines."
    )


def demo_edi_read_write() -> None:
    lab = _ensure_lab()
    sample = (
        "ISA*00*          *00*          *ZZ*ABC*ZZ*XYZ*210101*1253*^*00501*000000905*0*T*:~"
        "GS*PO*ABC*XYZ*20210101*1253*905*X*005010~"
    )
    edi_path = lab / "data.edi"
    edi_path.write_text(sample, encoding="utf-8")

    with open(edi_path, "r", encoding="utf-8") as f:
        edi_content = f.read()
    print("Raw EDI:", edi_content[:80], "...")

    segments = [s.strip() for s in edi_content.split("~") if s.strip()]
    print("Segment count:", len(segments))
    for seg in segments:
        print(" ", seg)

    out_path = lab / "output.edi"
    new_segments = [
        "ISA*00*          *00*          *ZZ*ABC*ZZ*XYZ*210101*1253*^*00501*000000905*0*T*:",
        "GS*PO*ABC*XYZ*20210101*1253*905*X*005010",
    ]
    with open(out_path, "w", encoding="utf-8") as f:
        for seg in new_segments:
            f.write(seg + "~\n")
    print("Wrote:", out_path)


# PYTHON RECALL — Practice (P1–P5)
# P1: Count lines in a text file without loading whole file if huge (loop).
# P2: Copy file content using read/write (no shutil).
# P3: Handle FileNotFoundError with try/except (day1 pattern).
# P4: Write JSON as plain text string (before pandas — day5).
# P5: Parse CSV line manually: "Amit,25" → split on comma.

def run_classroom_demo() -> None:
    demo_encoding_note()
    demo_write_and_read_whole()
    demo_readlines()
    demo_append_mode()
    demo_edi_read_write()


if __name__ == "__main__":
    run_classroom_demo()