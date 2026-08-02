# Create a new list containing only even numbers from another list.

numbers = []

# Take 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("\nNumbers : ",numbers)

even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)

print("\nEven Numbers : ",even)
