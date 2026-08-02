# Print every item with numbering.

# Example

# 1. Apple
# 2. Mango
# 3. Banana

fruits = ["Apple", "Mango", "Banana"]
print("\nPrint every item with numbering : ")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")