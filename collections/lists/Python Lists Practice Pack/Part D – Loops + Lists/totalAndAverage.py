"""
Take 10 numbers.

Find :
    Total
    Average                 
"""

numbers = []

print("\nTaking first 10 numbers : ")

for i in range(10):
    while True:

        try:
                num = float(input(f"\nEnter num{i+1} : "))
                numbers.append(num)
                break

        except ValueError:
                print("Only numbers and floats are allowed!")

total = sum(numbers)
avg = total/len(numbers)

print("\nSum : ",total)
print("\nAverage : ",avg)