# Find items that exist in either set but not both.

# Solution
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# result = A.symmetric_difference(B)
result = A^B
print(result)