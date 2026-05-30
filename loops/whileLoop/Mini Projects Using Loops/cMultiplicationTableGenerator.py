# Write a Python program to generate the multiplication table of a number entered by the user.

# The program should:
# Ask the user to enter an integer number.
# Use a for loop to display the multiplication table from 1 to 10.

number = int(input("Enter the number : "))

print(f"The multiplication of {number} are :")

for i in range(1,11):
    print(f"{number} * {i} : {number * i}")
