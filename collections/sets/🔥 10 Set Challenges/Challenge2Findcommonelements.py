# Challenge 2

# Find common elements:

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

common_elements = A.intersection(B)

print(f"Common elements : {common_elements}")

# Find elements that appear only in A.
A_Only = A.difference(B)
print(f"A only elements : {A_Only}")

# Find all unique elements from both sets.
A_Only = A.difference(B)
B_Only = B.difference(A)
print(f"A unique elements : {A_Only}")
print(f"B unique elements : {B_Only}")



