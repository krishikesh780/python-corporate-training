"""
Week 1 — Day 4: Core Data Structures & Iteration
================================================

PYTHON CLASSROOM (Today's flow)
-------------------------------
1. Collections overview: list [], tuple (), set {}, dict {k:v}
2. List — CRUD, slice, loop
3. Tuple — index, count (immutable)
4. Set — unique, union / intersection / difference
5. Dict — keys, values, items()
6. List & dict comprehensions
7. Iterate all four + 2D matrix nested loop
8. Practice P1–P5

PYTHON RECALL
-------------
- list mutable; tuple immutable; set no duplicates; dict keyed lookup.
- list[i:j] slice; append / remove / pop on lists only.
- set uses | & - for union, intersection, difference.
- for k, v in d.items() on dictionaries.
- Day 5 deep-dives list methods & advanced dict (don't repeat there from scratch).
"""

# -----------------------------------------------------------------------------
# 1. List
# -----------------------------------------------------------------------------

def demo_list() -> None:
    fruits = ["apple", "banana", "mango", "apple"]
    print("Fruits:", fruits)
    fruits.append("orange")
    fruits.remove("banana")
    print("Updated:", fruits)
    print("Slice [1:3]:", fruits[1:3])
    for f in fruits:
        print(" ", f)


# -----------------------------------------------------------------------------
# 2. Tuple
# -----------------------------------------------------------------------------

def demo_tuple() -> None:
    coordinates = (10, 20, 30, 20)
    print("Coordinates:", coordinates)
    print("index(20):", coordinates.index(20))
    print("count(20):", coordinates.count(20))


# -----------------------------------------------------------------------------
# 3. Set
# -----------------------------------------------------------------------------

def demo_set() -> None:
    unique_ids = {101, 102, 103, 101}
    print("IDs:", unique_ids)
    unique_ids.add(104)
    unique_ids.discard(102)
    print("Updated:", unique_ids)

    dept_a = {"Ravi", "Anu", "Sita"}
    dept_b = {"Anu", "Vikram"}
    print("Union:", dept_a | dept_b)
    print("Intersection:", dept_a & dept_b)
    print("Difference:", dept_a - dept_b)


# -----------------------------------------------------------------------------
# 4. Dictionary
# -----------------------------------------------------------------------------

def demo_dict() -> None:
    employee = {"name": "Ravi", "dept": "IT", "salary": 50000}
    print("Employee:", employee)
    employee["salary"] = 60000
    employee["location"] = "Pune"
    for key, value in employee.items():
        print(f"  {key}: {value}")


# -----------------------------------------------------------------------------
# 5. Comprehensions
# -----------------------------------------------------------------------------

def demo_list_comprehension() -> None:
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    evens = [x for x in numbers if x % 2 == 0]
    print("Squares:", squares)
    print("Evens:", evens)


def demo_dict_comprehension() -> None:
    names = ["Ravi", "Anu", "Sita"]
    scores = [90, 85, 88]
    student_dict = {name: score for name, score in zip(names, scores)}
    print("Student dict:", student_dict)


# -----------------------------------------------------------------------------
# 6. Iteration & 2D matrix
# -----------------------------------------------------------------------------

def demo_iteration_all() -> None:
    print("List:", end=" ")
    for f in ["apple", "mango"]:
        print(f, end=" ")
    print()

    print("Dict:")
    for k, v in {"name": "Ravi", "dept": "IT"}.items():
        print(f"  {k} -> {v}")

    print("Set:", end=" ")
    for i in {101, 102}:
        print(i, end=" ")
    print()


def demo_two_dimension_matrix() -> None:
    matrix = [[1, 2, 3], [4, 5, 6]]
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()


# -----------------------------------------------------------------------------
# PYTHON RECALL — Practice (P1–P5)
# -----------------------------------------------------------------------------
# P1: Build a list of 5 cities; append, remove, print slice.
# P2: Tuple of marks — print max using loop (no built-in max yet optional).
# P3: Two sets of roll numbers — print common (intersection).
# P4: Dict product → price; update one key; loop items().
# P5: List comprehension: squares of evens from 1..20.

def run_classroom_demo() -> None:
    demo_list()
    demo_tuple()
    demo_set()
    demo_dict()
    demo_list_comprehension()
    demo_dict_comprehension()
    demo_iteration_all()
    demo_two_dimension_matrix()


if __name__ == "__main__":
    run_classroom_demo()