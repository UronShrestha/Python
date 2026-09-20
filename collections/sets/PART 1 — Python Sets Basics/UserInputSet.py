# Ask the user for five fruits and store them in a set.

fruits = set()

for i in range(5):
    fruit = input(f"Enter fruit name {i+1} : ").capitalize()
    fruits.add(fruit)

for index, fruit in enumerate(fruits, start=1):
    print(f"\n{index}. {fruit}")