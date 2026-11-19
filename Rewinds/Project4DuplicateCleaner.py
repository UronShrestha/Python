# Project 4 — Duplicate Cleaner
# Difficulty: ⭐⭐
'''
Give the user 10 numbers.
Example:
Numbers:
[1, 2, 2, 3, 4, 4, 5, 5, 6, 6]

Display:
Original:
[1, 2, 2, 3, 4, 4, 5, 5, 6, 6]

Unique:
{1, 2, 3, 4, 5, 6}

Duplicates:
2, 4, 5, 6

Original Count: 10
Unique Count: 6

Requirements
Use:
- List
- Set
- for
- if
- in
Challenge
Try doing it without simply converting the entire list to a set.
'''

original_numbers = []
duplicate_numbers = set()
unique_numbers = set()

for i in range(10):
    while True:
        try: 
            number = int(input(f"Enter number{i+1} : "))
            original_numbers.append(number)
            break
        except ValueError:
            print("Enter valid integer!")

for number in original_numbers:
    if number in unique_numbers:
        duplicate_numbers.add(number)
    else:
        unique_numbers.add(number)

print("Original numbers : ",original_numbers)
print("Duplicate numbers : ",duplicate_numbers)
print("Unique numbers : ",unique_numbers)