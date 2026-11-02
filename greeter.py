"""
Week 9 lab starter — Build Your First Pipeline
SDEV 3320

A tiny, deliberately trivial module so the whole class period goes to the
pipeline mechanics, not to understanding the code being tested.
"""

def greet(name):
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"


def greet_all(names):
    joinedNames = ", ".join(names)
    return f"Hello, {joinedNames}!"