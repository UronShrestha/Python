# Exercise 3 — Find Different Elements
"""
a = frozenset({1, 2, 3, 4, 5})
b = frozenset({4, 5, 6, 7})

Find elements that exist in a but not in b.

Expected:

frozenset({1, 2, 3})
"""

a = frozenset({1, 2, 3, 4, 5})
b = frozenset({4, 5, 6, 7})

# diff = a.difference(b)
diff = a-b
print(diff)

student_a = frozenset({"Python", "Java", "C++", "JavaScript"})
student_b = frozenset({"Python", "Java", "PHP", "Laravel"})

# Find the languages that only Student A knows.