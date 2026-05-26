correct_password = "Password"

# while True:
#     pwd = input("Enter the password : ")
#     if pwd == correct_password:
#         print("Welcome!")
#         break
#     else:
#         print("Wrong Password!") 

pwd = input("\nEnter the password : ")

while pwd != correct_password:
    print("\nPassword Incorrect!")
    pwd = input("Enter the password again : ")

print("Access Granted!")