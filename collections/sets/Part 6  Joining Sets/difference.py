# Find items that exist in A but not B.

# Solution

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A | B
intersection = A & B
resultA = A - B
resultB = B - A

print("A U B : ",union)
print("A intersection B : ",intersection)
print("A - B : ",resultA)
print("B - A : ",resultB)