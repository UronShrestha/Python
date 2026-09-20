# Exercise 2 — Check the Copy
"""
Create:

numbers = frozenset({10, 20, 30, 40})

Create a copy using .copy().

Then check whether the original and copy are equal.

Expected:

Are they equal? True
"""

numbers = frozenset({10, 20, 30, 40})
print(f"Original : {numbers}")
newNumbers = numbers.copy()
print(f"\nCopy : {newNumbers}")
print()
print("Are they Equal? : ", numbers==newNumbers)

# if numbers==newNumbers:
#     print("Are they Equal? : ",True)
# else:
#     print("Are they Equal? : ",False)