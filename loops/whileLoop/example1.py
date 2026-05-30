age = int(input("Enter your age: "))

while age <= 0:
    print("Please enter a valid age.")
    age = int(input("Enter your age again: "))
print(f"You are {age} years old.")