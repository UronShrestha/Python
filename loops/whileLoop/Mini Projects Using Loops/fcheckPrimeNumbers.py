# Write a Python program to check whether a given number is a prime number or not.

# A number is called prime if it has exactly two factors: 1 and itself.

# Requirements
# Take an integer input from the user.
# Use a variable is_prime and initialize it as True.
# If the number is less than 2, it is not prime.
# Otherwise, use a for loop to check divisibility from 2 to num - 1.
# If the number is divisible by any value in this range, mark it as not prime and stop the loop.
# Display "Prime" if the number is prime, otherwise display "Not Prime".


number = int(input("Enter a number : "))
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if(is_prime):
    print(f"{number} is prime.")
else:
    print(f"{number} is not prime.")
 

