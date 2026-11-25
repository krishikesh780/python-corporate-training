"""
Week 1 — Day 3: Strings In-Depth
================================

PYTHON CLASSROOM (Today's flow)
-------------------------------
1. String literals (' vs ")
2. Indexing & slicing [start:end:step]
3. Common methods: upper, lower, strip, replace, split, join
4. Validation: isalpha, isdigit, startswith
5. Formatting: f-strings & precision
6. Regex intro (re.match, search, findall, sub)
7. Practice P1–P5

PYTHON RECALL
-------------
- Strings are immutable — methods return new strings.
- Slice end index is excluded; [::-1] reverses.
- len(s), s[i], s[-1] for last char.
- split() → list; "sep".join(list) → string.
- r"\\d+" raw strings help with regex patterns.
"""

import re

# -----------------------------------------------------------------------------
# 1. Literals & basics
# -----------------------------------------------------------------------------

def demo_string_literals() -> None:
    text1 = "It's alright"
    text2 = 'He is called "Johnny"'
    print(text1)
    print(text2)
    print("Length:", len(text1))


def demo_parse_user_record() -> None:
    """Slicing on a comma-separated profile string."""
    user = "Rishikesh Kumar, krishikesh780@gmail.com, 979529808099"
    name = user[0:15].strip()
    email = user[17:40]
    phone = user[42:]
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)


# -----------------------------------------------------------------------------
# 2. Slicing
# -----------------------------------------------------------------------------

def demo_string_slicing() -> None:
    text = "Python Programming"
    print("Original:", text)
    print("text[0:6]   ->", text[0:6])
    print("text[7:]    ->", text[7:])
    print("text[-6:]   ->", text[-6:])
    print("text[::2]   ->", text[::2])
    print("text[::-1]  ->", text[::-1])


# -----------------------------------------------------------------------------
# 3. Methods
# -----------------------------------------------------------------------------

def demo_string_methods() -> None:
    s = "  Hello world python "
    print("repr:", repr(s))
    print("upper:", s.upper())
    print("lower:", s.lower())
    print("strip:", s.strip())
    print("replace:", s.replace("world", "Python"))
    words = s.strip().split()
    print("split:", words)
    print("join:", "#".join(words))
    print("isdigit '123':", "123".isdigit())
    print("startswith 'He':", s.strip().startswith("He"))


# -----------------------------------------------------------------------------
# 4. Formatting
# -----------------------------------------------------------------------------

def demo_string_formatting() -> None:
    name, age = "Rishikesh", 28
    print(f"My name is {name} and I am {age} years old.")
    pi = 3.14159
    print(f"pi 2 decimals: {pi:.2f}")
    print(f"pi 3 decimals: {pi:.3f}")


# -----------------------------------------------------------------------------
# 5. Regex (3 levels)
# -----------------------------------------------------------------------------

def regex_level1() -> None:
    text = "My phone number is 9876543210"
    print("match 'My':", re.match(r"My", text))
    print("match 'phone':", re.match(r"phone", text))
    print("search 'phone':", re.search(r"phone", text))
    print("all digits:", re.findall(r"\d+", text))


def regex_level2() -> None:
    text = "Emails: test123@gmail.com, hello_world@yahoo.com"
    print("words:", re.findall(r"\w+", text))
    print("vowels:", re.findall(r"[aeiou]", text, flags=re.I))
    print("emails:", re.findall(r"[\w._]+@[\w.]+", text))


def regex_level3() -> None:
    text = "Call me at 9876543210 or 9123456789"
    print("10-digit phones:", re.findall(r"\d{10}", text))
    print("masked:", re.sub(r"\d{10}", "**********", text))


# -----------------------------------------------------------------------------
# PYTHON RECALL — Practice (P1–P5)
# -----------------------------------------------------------------------------
# P1: Reverse your full name using slicing only.
# P2: Count vowels in a sentence (loop or regex).
# P3: Clean "  email@site.com  " with strip; validate with '@' in s.
# P4: Split CSV line into name, email, phone (like demo_parse_user_record).
# P5: Extract all 10-digit numbers from a paragraph (regex).

def run_classroom_demo() -> None:
    demo_string_literals()
    demo_parse_user_record()
    demo_string_slicing()
    demo_string_methods()
    demo_string_formatting()
    regex_level1()
    regex_level2()
    regex_level3()


if __name__ == "__main__":
    run_classroom_demo()