'''Positive numbers

Negative numbers

into two different lists.
'''

numbers = []

# Take 7 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

positive = []
negative = []

for num in numbers:
    if num > 0:
        positive.append(num)

    if num < 0:
        negative.append(num)

print("Positive : ", positive)
print("Negative : ",negative)