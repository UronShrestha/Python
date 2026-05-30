# Program to reverse a string

string = input("Enter a string to reverse : ")
reverse = ""

for char in string:
    reverse = char + reverse
print(reverse)
