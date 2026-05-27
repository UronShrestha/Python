# Write a Python program to find and display the common elements between two lists.

# Use the following lists in your program:

# A = [1, 2, 3, 4]
# B = [3, 4, 5, 6]
# Requirements
# Use a for loop to traverse through list A.
# Check whether each element of A exists in list B.
# If the element is found in both lists, display it using print().


A = [1, 2, 3, 4]
B = [3, 4, 5, 6]


for a in A:
    if a in B:
        print(a)
