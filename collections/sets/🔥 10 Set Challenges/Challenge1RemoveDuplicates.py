# Challenge 1

# Given:

# numbers = [1, 2, 3, 3, 4, 5, 5, 6]

# Remove duplicates without using a set comprehension.

'''numbers = [1, 2, 3, 3, 4, 5, 5, 6]
num = set(numbers)
print(num)'''

original_numbers_list = [1, 2, 3, 3, 4, 5, 5, 6]
new_numbers_list = []

for item in original_numbers_list:
    if item not in new_numbers_list:
        new_numbers_list.append(item)
print(new_numbers_list)
