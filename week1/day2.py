"""
Week 1 — Day 2: Control Flow
============================

PYTHON CLASSROOM (Today's flow)
-------------------------------
1. if / if-else / if-elif-else
2. for loop + range(start, stop, step)
3. while loop
4. break, continue, pass
5. Mini example: order total (if + for)
6. Operator precedence (extends Day 1 — no full operator repeat)
7. Practice P1–P5

PYTHON RECALL
-------------
- Falsey values: 0, "", None, [], {} — often used in conditions.
- range(n) → 0..n-1; range(10, 0, -1) counts down.
- break exits loop; continue skips to next iteration; pass is empty placeholder.
- elif = else-if chain; only one branch runs.
- Operators: * / % before + - ; use () when unsure.
  (Full operator list: week1/day1.py → python_operators())
"""

# -----------------------------------------------------------------------------
# 1. if statements
# -----------------------------------------------------------------------------

def demo_if_statement() -> None:
    x = 10
    if x > 5:
        print("x is greater than 5")


def demo_if_else(n: int = 7) -> None:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")


def demo_if_elif_else(marks: int = 45) -> None:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")


# -----------------------------------------------------------------------------
# 2. for & while
# -----------------------------------------------------------------------------

def demo_for_loop() -> None:
    print("Count down:")
    for i in range(5, 0, -1):
        print("  ", i)

    print("Iterate list:")
    for item in ["apple", "banana", "mango"]:
        print("  ", item)


def demo_while_loop() -> None:
    n = 1
    while n <= 5:
        print("Number:", n)
        n += 1


# -----------------------------------------------------------------------------
# 3. break, continue, pass
# -----------------------------------------------------------------------------

def demo_break() -> None:
    for i in range(1, 10):
        if i == 5:
            print("Breaking at", i)
            break
        print("Value:", i)


def demo_continue() -> None:
    for i in range(1, 6):
        if i == 3:
            print("Skipping 3")
            continue
        print("Value:", i)


def demo_pass() -> None:
    for i in range(3):
        if i == 1:
            pass  # placeholder — block must not be empty
        else:
            print("i =", i)


# -----------------------------------------------------------------------------
# 4. Classroom mini-project: order total
# -----------------------------------------------------------------------------

def calculate_total_price(items: list, discount: float = 0.0) -> float:
    if len(items) == 0:
        return 0.0
    total = sum(item["price"] for item in items)
    if discount > 0:
        total *= 1 - discount
    return total


def process_order(customer: dict, items: list) -> dict:
    print(f"Processing order for {customer['name']}")
    total_price = calculate_total_price(items, customer.get("discount", 0))
    if total_price > 100:
        print("High-value order!")
    else:
        print("Standard order.")
    return {"customer": customer["name"], "total": round(total_price, 2)}


# -----------------------------------------------------------------------------
# 5. Operator precedence (Day 2 only — not full Day 1 operator demo)
# -----------------------------------------------------------------------------

def demo_operator_precedence() -> None:
    print("(6 + 3) - (6 + 3) =", (6 + 3) - (6 + 3))
    print("100 + 5 * 3 =", 100 + 5 * 3)
    print("5 + 4 - 7 + 3 =", 5 + 4 - 7 + 3)


# -----------------------------------------------------------------------------
# PYTHON RECALL — Practice (P1–P5)
# -----------------------------------------------------------------------------
# P1: Print numbers 1–10 using for and range.
# P2: Print sum of 1..n using while (n from input).
# P3: FizzBuzz for 1–15 (mod 3 / mod 5 rules).
# P4: Grade calculator with if-elif-else (custom cutoffs).
# P5: Loop 1–20; continue on multiples of 3; break on 17.

def run_classroom_demo() -> None:
    demo_if_statement()
    demo_if_else()
    demo_if_else(4)
    demo_if_elif_else()
    demo_if_elif_else(82)
    demo_for_loop()
    demo_while_loop()
    demo_break()
    demo_continue()
    demo_pass()
    demo_operator_precedence()

    customer = {"name": "Ravi", "discount": 0.1}
    items = [{"price": 40}, {"price": 70}]
    print("Order:", process_order(customer, items))


if __name__ == "__main__":
    run_classroom_demo()