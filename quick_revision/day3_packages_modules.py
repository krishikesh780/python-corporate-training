"""
Quick Revision — Day 3: Modules & packages
==========================================
import styles, package layout, __name__ == "__main__".
Full course: ../week2/day3–4
"""

from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent


def demo_import_styles() -> None:
    import math
    from math import sqrt

    print("import math:", math.pi)
    print("from math import sqrt:", sqrt(16))


def demo_sys_path_note() -> None:
    print("Training code lives under:", _ROOT)
    print("Prefer: python -m package.module (absolute imports)")


def demo_main_guard() -> None:
    def welcome() -> None:
        print("welcome() — import-safe helper")

    welcome()
    print("__name__ here:", __name__)
    if __name__ == "__main__":
        print("Runs when executed directly, not on import.")


# Interview one-liners
INTERVIEW = """
Module  = one .py file
Package = folder + modules (+ __init__.py)
Avoid: from module import *
Use:   if __name__ == "__main__":
"""


def run_revision() -> None:
    demo_import_styles()
    demo_sys_path_note()
    demo_main_guard()
    print(INTERVIEW.strip())


if __name__ == "__main__":
    run_revision()