# Take five numbers from the user.

# Print them one by one using a for loop.

nums = []

for x in range(5):
    while True:
        try:
            num = int(input(f"Enter number{x+1} : "))
            nums.append(num)
            break
        except ValueError:
            print("Invalid input! Only integers allowed.")


print("\nPrinting one by one using a for loop : ")

for num in nums: 
    print(num)