# Exercise 11 — Basic Subset
"""
a = frozenset({1, 2})
b = frozenset({1, 2, 3, 4})

Check whether a is a subset of b.

Use:issubset()
"""

a = frozenset({1, 2})
b = frozenset({1, 2, 3, 4})
print(a.issubset(b))

# Subset Using <=

A = frozenset({1, 2})
B = frozenset({1, 2, 3, 4})
print(A<=B) #allows equality
print(A<B) #requires a proper subset

