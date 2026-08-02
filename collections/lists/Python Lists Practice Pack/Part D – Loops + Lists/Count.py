"""Count

Even numbers
Odd numbers"""

numbers = []

print("\nTaking first 10 numbers : ")

for i in range(10):
    while True:

        try:
                num = int(input(f"Enter num{i+1} : "))
                numbers.append(num)
                break

        except ValueError:
                print("Only numbers are allowed!")

even_count = 0
odd_count = 0

for num in numbers:
      if num % 2 == 0:
            even_count+=1
      else:
            odd_count+=1

print("\nEven : ",even_count)
print("\nOdd : ",odd_count)