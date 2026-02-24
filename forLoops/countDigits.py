# wap to count digits

num = input("Enter digits : ")
count = 0

for digit in str(num):
    count+=1
print("The count of given digit is : ", count)