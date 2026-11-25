"""
Quick Revision — Day 1: Core Python
==================================
Types (str/list/dict), builtins, lambda, map/filter, generator, decorator.
Full course: ../week1, ../week2/day1–2
"""

from pathlib import Path

_LAB = Path(__file__).resolve().parent / "_lab"


def demo_crud_types() -> None:
    s = "hello"
    print("str slice:", s[1:4])
    s = s.replace("l", "L")
    print("str replace:", s)

    lst = [10, 20, 30]
    lst[1] = 99
    lst.append(40)
    lst.remove(99)
    print("list:", lst)

    d = {"a": 1, "b": 2}
    d["c"] = 3
    d.pop("b")
    print("dict:", d)
    print("Recall: str/tuple immutable; list/dict mutable")


def demo_builtins() -> None:
    a = [3, 1, 4, 1]
    print("len/sum/max:", len(a), sum(a), max(a))
    print("sorted (new):", sorted(a))
    print("enumerate:", list(enumerate(a, start=1)))
    print("zip:", list(zip(a, ["x", "y", "z", "w"])))


def demo_map_filter() -> None:
    nums = [1, 2, 3, 4, 5]
    print("map square:", list(map(lambda x: x**2, nums)))
    print("filter even:", list(filter(lambda x: x % 2 == 0, nums)))


def demo_generator() -> None:
    def count_up(n: int):
        for i in range(1, n + 1):
            yield i

    print("generator:", list(count_up(3)))


def demo_decorator() -> None:
    def log_calls(func):
        def wrapper(*args, **kwargs):
            print("  [decorator] before")
            out = func(*args, **kwargs)
            print("  [decorator] after")
            return out

        return wrapper

    @log_calls
    def greet(name: str) -> str:
        return f"Hello, {name}"

    print(greet("Python"))


def demo_with_file() -> None:
    _LAB.mkdir(parents=True, exist_ok=True)
    path = _LAB / "sample.txt"
    with path.open("w", encoding="utf-8") as f:
        f.write("Hello World\n")
    with path.open("r", encoding="utf-8") as f:
        print("with read:", f.read().strip())


def run_revision() -> None:
    demo_crud_types()
    demo_builtins()
    demo_map_filter()
    demo_generator()
    demo_decorator()
    demo_with_file()


if __name__ == "__main__":
    run_revision()