#python compound interest calculator

principle = 0
time = 0
rate = 0

while principle <= 0:
    principle = float(input("Enter the principle: "))
    if principle <= 0:
        print("Principle can't be less than or equal to 0.")
# print(f"Principle is Nrs.{principle}")

while time <= 0:
    time = int(input("Enter the time: "))
    if time <= 0:
        print("Time can't be less than or equal to 0.")
# print(f"Time is {time} years.")

while rate <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to 0.")
# print(f"Rate is {rate}%")


interest = principle * pow((1 + (rate/100)), time)

print(f'Your compound interest is Nrs. {interest:.2f}')