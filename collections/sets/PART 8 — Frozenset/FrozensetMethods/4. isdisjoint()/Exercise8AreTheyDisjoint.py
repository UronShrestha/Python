# Exercise 8 — Are They Disjoint?
# isdisjoint() returns True when two sets have nothing in common.

a = frozenset({1, 2, 3})
b = frozenset({4, 5, 6})

A = frozenset({1, 2, 3})
B = frozenset({3, 4, 5})

# Check whether they are disjoint.

# Expected:

# True

print(f"Are a and b Disjoint? : {a.isdisjoint(b)}")
print(f"Are A and B Disjoint? : {A.isdisjoint(B)}")