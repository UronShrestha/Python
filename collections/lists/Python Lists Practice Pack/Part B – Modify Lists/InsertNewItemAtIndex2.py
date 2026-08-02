# Insert a new item at index 2.


items = []

for i in range(5):
        item = input(f"Enter item{i+1} : ")
        items.append(item)

for index, item in enumerate(items, start=1):
        print(f'{index}. {item}')    


replace = input("\nInsert new item at index 2 : ")
items.insert(1, replace)

print("\nUpdated list after replacing new item at index 2 : ")
for index, item in enumerate(items, start=1):
        print(f'{index}. {item}')   


