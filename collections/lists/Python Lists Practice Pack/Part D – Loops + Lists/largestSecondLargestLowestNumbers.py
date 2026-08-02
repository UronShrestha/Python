'''
Find the largest number without using max()
Find the smallest number without using min()
Find the second largest number.
'''

nums = []

for i in range(5):
    num = int(input(f"Enter number{i+1} : "))
    nums.append(num)
print(nums)

largest = nums[0]
smallest = nums[0]

for num in nums:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num 

second_largest = None
for num in nums:
    if num != largest:
        if second_largest is None or num > second_largest:
            second_largest = num


print("\nLargest number:", largest)
print("Second Largest number:", smallest)
print("Smallest number:", smallest)