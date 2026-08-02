# Take five names from the user and store them in a list.
# Print the list.

nums = []

for x in range(5):
    while True:
        try:
            num = int(input(f"Enter number{x+1} : "))
            nums.append(num)
            break
        except ValueError:
            print("Invalid input! Only integers allowed.")
        
print(nums)