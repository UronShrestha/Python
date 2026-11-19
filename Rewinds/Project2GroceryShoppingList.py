# 🟢 Project 2 — Grocery Shopping List
# Difficulty: ⭐
'''
Create a shopping-list program.

========== SHOPPING LIST ==========

1. Add Item
2. Remove Item
3. View Items
4. Search Item
5. Sort Items
6. Count Items
7. Exit

Example:

Enter choice: 1
Enter item: Milk

Milk added successfully.
Requirements

Use:

List
while
if / elif
append()
remove()
sort()
in
len()
Bonus

Don't allow duplicate items.

This is where you can start thinking:

Should I use a list or a set?
'''

shopping_list = []



while True : 
    print("\n========== Menu ==========")

    print("1. Add Item")
    print("2. View Item")
    print("3. Remove Item")
    print("4. Search Item")
    print("5. Sort Items")
    print("6. Count Items")
    print("7. Exit")

    choice = input("\nEnter choice from 1-7 : ")
    # choice = int(choice)
    if choice == "":
        print("Please enter number from 1-7")
        continue

# 1. Add Item
    elif choice == "1":
        while True:
            item = input("Enter an item to add to the shopping list : ").strip().title()
            if item == "":
                print("Input cannot be empty!")
                continue
            elif item in shopping_list:
                print(f"========== {item} already in list! ==========")
            else:
                shopping_list.append(item)
                print(f"========== {item} added successfully! ==========")
                break

# 2. View Item
    elif choice == "2":
        if len(shopping_list) == 0:
            print(f"========== No Items! ==========")

        
        else:
                print(f"========== Items! ==========")
                print(f"\n|Index | Item      |")

                for index, item in enumerate(shopping_list, start=1):
                 print(f"|{index}     | {item}       |")

# 3. Remove Items
    elif choice == "3":
        while True:
            if len(shopping_list) == 0:
                print(f"========== No Items! ==========")
            
            else:
                item = input("Enter name of item to remove : ").strip().title()
                if item == "":
                    print("Input cannot be empty!")
                    continue
                elif item not in shopping_list:
                    print(f"========== {item} is not in list. ==========")
                    continue
                else:
                    shopping_list.remove(item)
                    print(f"========== {item} removed successfully! ==========")
            break

# 4. Search Item
    elif choice == "4":
        while True:
            if len(shopping_list) == 0:
                print(f"========== No Items! ==========")
                    
            else:
                item = input("Enter name of item to search : ").strip().title()
                if item == "":
                    print("Input cannot be empty!")
                    continue
                elif item in shopping_list:
                    print(f"========== {item} is available in list! ==========")
                else:
                    print(f"========== {item} is not available in list! ==========")
            break
                
# 5. Sort Items             
    elif choice == "5":
        while True:
            if len(shopping_list) == 0:
                print(f"========== No Items! ==========")
                            
            else:
                shopping_list.sort()
                print(f"\n|Index | Item      |")
                
                for index, item in enumerate(shopping_list, start=1):
                              print(f"|{index}     | {item}       |")
            break

# 6. Count Items
    elif choice == "6":
        print("Number of item is shopping list : ", len(shopping_list))
# 7. Exit
    elif choice == "7":
        print(f"========== Good Bye! ==========")
        break

#Invalid Input
    else:
        print("Invalid Input")
    

    