# Exercise 1 — Copy a Frozenset
"""
Create a frozenset containing:

{"apple", "banana", "cherry"}

Use .copy() to create a copy.

Print:

Original: frozenset(...)
Copy: frozenset(...)
"""

fruits = frozenset(["apple", "banana", "cherry"])
print("\nOriginal :",fruits)


new = fruits.copy()
print("\nCopy : ",new)