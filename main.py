"""Repo launcher — curriculum paths + where to read docs."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

WEEKS = {
    1: "Basics · strings · collections",
    2: "Functions · modules · JSON project",
    3: "Errors · I/O · pandas",
    4: "OOP · Git · insurance Excel",
    5: "SQLite · regression · CMS",
}


def main() -> None:
    print("Python Corporate Training\n")
    print("READ FIRST:")
    print(f"  {ROOT / 'docs' / 'HOW_TO_STUDY.md'}")
    print(f"  {ROOT / 'docs' / 'CURRICULUM.md'}")
    print(f"  {ROOT / 'README.md'}\n")

    for n, topic in WEEKS.items():
        week = ROOT / f"week{n}"
        days = sorted(week.glob("day*.py"))
        readme = week / "README.md"
        print(f"Week {n}: {topic}")
        if readme.exists():
            print(f"  guide: week{n}/README.md")
        if days:
            print(f"  days:  {', '.join(d.name for d in days)}")
        print()

    print("Run:  .venv\\Scripts\\activate")
    print("      python week1\\day1.py")
    print("Rev:  python quick_revision\\day1_core_python.py")
    print("Jobs: week6\\README.txt")
    print("Interview: interview_prep\\INTERVIEW_ALL.txt")


if __name__ == "__main__":
    main()