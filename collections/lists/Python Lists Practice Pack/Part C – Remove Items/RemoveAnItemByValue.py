# Remove an item by value.

items = []

for i in range(5):
        item = input(f"Enter item{i+1} : ")
        items.append(item)

for index, item in enumerate(items, start=1):
        print(f'{index}. {item}')    


remove = input("\nInsert new item at index 2 : ")
items.remove(remove)

print(f"\nUpdated list after removing {remove} : ")
for index, item in enumerate(items, start=1):
        print(f'{index}. {item}')   


