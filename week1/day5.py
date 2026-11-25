"""
Week 1 — Day 5: For-Loop Deep Dive & Collection Methods
=======================================================

PYTHON CLASSROOM (Today's flow)
-------------------------------
1. for with index: range(len), enumerate
2. Reverse / step loops [::-1]
3. Conditional list comprehensions
4. List methods: append, insert, slice assign, remove, pop, extend, sort
5. sorted() vs list.sort(); count, index
6. Dict: nested access, update, pop, clear; items comprehension
7. 2D list → flat dict with enumerate
8. Practice P1–P5

PYTHON RECALL
-------------
- enumerate(seq, start=0) gives (index, value).
- list.sort() in-place; sorted(lst) returns new list.
- remove(value) vs pop(index) vs del lst[i].
- extend merges iterables; + creates new concatenation.
- Structures intro: see week1/day4.py (no duplicate full demos).
"""

# -----------------------------------------------------------------------------
# 1. For-loop patterns
# -----------------------------------------------------------------------------

def demo_for_with_index() -> None:
    values = [10, 20, 30]
    for i in range(len(values)):
        print(f"index {i} -> {values[i]}")

    for idx, val in enumerate(values, start=1):
        print(f"#{idx}: {val}")


def demo_for_reverse() -> None:
    for i in [1, 2, 3, 4, 5][::-1]:
        print(i, end=" ")
    print()


def demo_conditional_comprehension() -> None:
    nums = [1, 2, 3, 4, 5]
    labels = ["even" if n % 2 == 0 else "odd" for n in nums]
    double_evens = [n * 2 for n in nums if n % 2 == 0]
    print("labels:", labels)
    print("double evens:", double_evens)


# -----------------------------------------------------------------------------
# 2. List CRUD & methods
# -----------------------------------------------------------------------------

def demo_list_add() -> None:
    lst = [1, 2, 3]
    lst.append(4)
    lst.insert(1, 99)
    print("after append/insert:", lst)


def demo_list_replace_slice() -> None:
    lst = [1, 2, 2, 3, 4]
    lst[1:3] = [20, 20]
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = 0
    print("after slice + in-place update:", lst)


def demo_list_remove() -> None:
    lst = [1, 2, 3, 2, 4]
    lst.remove(2)
    last = lst.pop()
    print("after remove(2) and pop():", lst, "| popped:", last)


def demo_list_join_and_sort() -> None:
    l1 = [3, 1, 2]
    l2 = [4, 5]
    merged = l1 + l2
    l1.extend(l2)
    print("merged (+):", merged)
    print("extended l1:", l1)
    print("sorted copy:", sorted(l1))
    l1.sort()
    print("l1.sort():", l1)
    print("count of 2:", l1.count(2))


# -----------------------------------------------------------------------------
# 3. Dictionary deep dive
# -----------------------------------------------------------------------------

def demo_dict_nested() -> None:
    family = {
        "child1": {"name": "Emil", "year": 2004},
        "child2": {"name": "Tobias", "year": 2007},
    }
    print("child2 year:", family["child2"]["year"])


def demo_dict_methods() -> None:
    d = {"A": 1, "B": 2, "C": 3}
    d["B"] = 22
    d.update({"D": 4})
    removed = d.pop("A")
    print("after update/pop A:", d, "| removed:", removed)


def demo_dict_comprehension() -> None:
    d = {"A": 1, "B": 2, "C": 3, "D": 4}
    items = [(k, v) for k, v in d.items() if v % 2 == 0]
    print("even-value items:", items)


def demo_matrix_to_dict() -> None:
    matrix = [[1, 2, 3], [4, 5, 6]]
    flat = {}
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            flat[f"r{i}c{j}"] = value
    print("flat dict:", flat)


# -----------------------------------------------------------------------------
# 4. Tuple ↔ list (when you need mutability)
# -----------------------------------------------------------------------------

def demo_tuple_to_list() -> None:
    t = (6, 7, 8)
    lst = list(t)
    lst.append(9)
    t2 = tuple(lst)
    print("tuple → list → tuple:", t2)


# -----------------------------------------------------------------------------
# PYTHON RECALL — Practice (P1–P5)
# -----------------------------------------------------------------------------
# P1: enumerate a list of names with start=101.
# P2: Replace all negatives in a list with 0 (loop or comprehension).
# P3: Merge two dicts with update; safe get() for missing keys.
# P4: Nested dict: store 3 students {id: {name, score}}; print one score.
# P5: Build dict from 2×3 matrix keys r0c0 … r1c2 (like demo_matrix_to_dict).

def run_classroom_demo() -> None:
    demo_for_with_index()
    demo_for_reverse()
    demo_conditional_comprehension()
    demo_list_add()
    demo_list_replace_slice()
    demo_list_remove()
    demo_list_join_and_sort()
    demo_dict_nested()
    demo_dict_methods()
    demo_dict_comprehension()
    demo_matrix_to_dict()
    demo_tuple_to_list()


if __name__ == "__main__":
    run_classroom_demo()