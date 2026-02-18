# factorail of a given number

num = int(input("Enter a number : "))
factorial = 1

if num < 0:
    print(f"{num} is invalid.")
else:
    for i in range(1, num+1):
        factorial *= i
print(f"Factorial of {num}: ", factorial)