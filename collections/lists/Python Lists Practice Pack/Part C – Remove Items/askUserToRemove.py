"""
Ask the user which fruit to remove.

If it exists remove it.

Otherwise print

Item not found
"""


fruits = []

for i in range(5):
        fruit = input(f"Enter item{i+1} : ").capitalize()
        fruits.append(fruit)
print("\nBefore : ")
for index, item in enumerate(fruits, start=1):
        print(f'{index}. {item}')    


while True:
        remove = input("\nEnter item's name to remove : ").capitalize()
        if remove in fruits:
                fruits.remove(remove)
                print(f"{remove} removed successfully!")
                break

        else:
                print(f"{remove} is not found in list!")

print("\nAfter : ")
for index, item in enumerate(fruits, start=1):
        print(f'{index}. {item}')  
        





















# while True:
#     remove_fruit = input("\nEnter name of fruit to be removed : ")

#     if remove_fruit in fruits:
#         fruits.remove(remove_fruit)
#         print(f"{remove_fruit} removed successfully!")
#         break
#     else:
#         print(f"\n{remove_fruit} not found!")

#         print("\nCurrent Fruits:")
#         for index, fruit in enumerate(fruits, start=1):
#                 print(f"{index}. {fruit}")

# print("\nUpdated List:")
# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}. {fruit}")
        
        

