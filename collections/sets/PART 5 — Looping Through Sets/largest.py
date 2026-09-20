'''Find the Largest Number

Don't use max().'''

# Solution

numbers = {10, 5, 25, 8, 15}

largest = None

for number in numbers:
    if largest is None or number > largest:
        largest = number

print("Largest : ", largest)