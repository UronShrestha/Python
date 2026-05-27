# Write a Python program to count the number of even and odd numbers in a list.

# Use the following list in your program:

# numbers = [1, 2, 3, 4, 5, 6]
# Requirements:
# Create two variables named even and odd and initialize them to 0.
# Use a for loop to traverse through the list.
# Check whether each number is even or odd using the modulus (%) operator.
# Increase the corresponding counter.
# Display the total number of even and odd numbers.

numbers = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even+=1
    else:
        odd+=1

print("The number of even numbers is list : ", even)
print("The number of odd numbers is list : ", odd)

