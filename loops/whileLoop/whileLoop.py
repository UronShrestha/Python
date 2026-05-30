#while loop = executes a block of code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("Please enter your name.")
    name = input("Enter your name:")
print(f"Hello, {name}.")

