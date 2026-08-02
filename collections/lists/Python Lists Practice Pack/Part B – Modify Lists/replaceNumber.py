'''Replace every even number with 0.
Example:
    Before
    1 2 3 4 5

    After
    1 0 3 0 5
'''


items = []

for i in range(5):
        item = int(input(f"Enter item{i+1} : "))
        items.append(item)

print("\nBefore : ")
for index, item in enumerate(items, start=1):
        print(f'{index}. {item}')    


for item in range(len(items)):
        if items[item] % 2 == 0:
                items[item] = 0

print("\nAfter : ")
print(items)




# numbers = []

# for i in range(5):
#         num = int(input(f"Enter number{i+1} : "))
#         numbers.append(num)

# print("\nBefore:")
# for index, num in enumerate(numbers, start=1):
#     print(f"{index}. {num}")

# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i] = 0

# print("\nAfter:")
# print(numbers)

