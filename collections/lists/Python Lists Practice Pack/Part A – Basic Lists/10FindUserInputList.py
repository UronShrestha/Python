'''Ask the user for a fruit.

If it exists

Available

Otherwise

Not Available'''

fruits = []

for i in range(5):
    fruit = input(f"Enter fruit{i+1} : ")
    fruits.append(fruit)

print("The fruits entered by user : ")
for fruit in fruits:
    print(fruit)

while True:
    user_fruit = input("Enter fruit : ")
    if user_fruit in fruits:
        print(f"{user_fruit} is available in the list.")
    else:
        print(f"{user_fruit} is not available in the list.")
    break