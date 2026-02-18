# Program to reverse a string

string = input("Enter a string : ")
reverse = ""

for char in string:
    reverse = char + reverse
print(f"The reverse of '{string}' : ",reverse)
    

