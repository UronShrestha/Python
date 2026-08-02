'''
Remove duplicate values.

    Example:

    Before:
    1 2 2 3 4 4 5

    After:
    1 2 3 4 5
'''

numbers = []

# Take 7 numbers
for i in range(7):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nBefore:")
print(numbers)

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("\nAfter:")
print(unique_numbers)