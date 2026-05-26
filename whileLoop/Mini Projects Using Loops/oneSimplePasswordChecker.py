correct_password = "Password"

while True:
    pwd = input("Enter the password : ")
    if pwd == correct_password:
        print("Access Granted!")
        break
    else:
        print("Wrong Password!") 

# correct_password = input("Create new password : ")
# pwd = input("\nEnter the password : ")

# while pwd != correct_password:
#     print("\nPassword Incorrect!")
#     pwd = input("Enter the password again : ")

# print("Access Granted!")