# Write a Python program to simulate a simple ATM system using a menu-driven while loop.
# The program should start with an initial balance of 1000.
# Display the following menu repeatedly until the user chooses to exit:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

balance = 1000

while True:
    print("\n1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("\nChoose : ")

    if(choice == "1"):
        print(f"Your new balance is : {balance:.2f}", )

    elif(choice == "2"):
        amount = float(input("Deposit amount : "))
        balance += amount
        print(f"Your new balance is : {balance:.2f}", )

    elif(choice == "3"):
        amount = float(input("Enter amount to withdraw : "))
        if amount <= balance:
            balance -= amount
            print(f"Your new balance is : {balance:.2f}", )
        else:
            print("Insufficient Amount!")

    elif(choice == "4"):
        print("BYE!")
        break    

    else:
        print("Invalid Choice!")