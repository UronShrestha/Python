# WAP to find the largest number

number = input("Enter numbers : ")

largest = number[0]

for x in number:
    if x > largest:
        largest = x
    
print("the largest number is : ", largest)