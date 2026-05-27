# Write a Python program to check whether a given word is a palindrome or not.

# A word is called a palindrome if it reads the same forwards and backwards.

# Requirements
# Take a word as input from the user.
# Reverse the word using a loop (do not use slicing).
# Compare the original word with the reversed word.
# Display "Palindrome" if both are the same, otherwise display "Not Palindrome".


string = input("Enter a string : ")
rev = ""

for char in string:
    rev = char + rev

if string == rev:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")




