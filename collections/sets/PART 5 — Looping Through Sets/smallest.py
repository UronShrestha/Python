'''Find the Smallest Number

Don't use min().'''

# Solution

numbers = {10, 5, 25, 8, 15}

smallest = None

for number in numbers:
    if smallest is None or number < smallest:
        smallest = number

print("Smallest Number : ", smallest)

