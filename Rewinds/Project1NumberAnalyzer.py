# Project 1 — Number Analyzer
# Difficulty: ⭐
'''
Create a program that asks the user to enter 10 numbers.

The program should display:

========== NUMBER ANALYZER ==========

Numbers: [10, 5, 8, 3, 10, 7, 2, 8, 9, 4]

Total: 66
Largest: 10
Smallest: 2
Even: 6
Odd: 4
Unique numbers: 8
Requirements

Use:

List
Set
for loop
if
len()
sum()
Bonus

Find the largest and smallest without using max() or min().
'''

numbers = []

for i in range(10):
    while True:
        number = int(input(f"Enter number {i+1} : "))
        if number == "":
            print("Input is Empty!")
            continue
        numbers.append(number)
        break


print(f"\n{numbers}")

print("\n========== NUMBER ANALYZER ==========")

number_set = set(numbers)

#Total
total = sum(numbers)
# number = int(number)

# for number in numbers:
#     total+=number
print("\nTotal : ", total)

#Largest
largest = numbers[0]

for number in number_set:
    if number > largest:
        largest = number

print("Largest : ", largest)


# Smallest
smallest = numbers[0]

for number in numbers:
    if number<smallest:
        smallest = number
print("Smallest : ", smallest )

#count even
count_even = 0
count_odd = 0
for number in numbers:
    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Even Numbers : ",count_even)
print("Odd Numbers : ",count_odd)

unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print("Unique numbers : ", unique)


