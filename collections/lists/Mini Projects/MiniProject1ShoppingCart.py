'''
Create a program that:

Starts with an empty list.
Asks the user to enter 5 items.
Stores them in the list.
Prints all items with numbering.
Prints the total number of items.
'''
cart = [] #empty list

#asks the user to enter 5 items
for i in range(5):
    while True:
            item = input(f"Enter the item{i+1} : ")
            if item == "":
                  print("Please enter the item name.")
            else:
                  cart.append(item)
                  break

# Prints all items with numbering.
print("\n-----CART ITEMS-----")
index = 1
for items in cart:
      print(f"Item{index}. {items}")
      index+=1

# Prints the total number of items.
print(f"\nTotal number or items in cart : {len(cart)}")
            
            