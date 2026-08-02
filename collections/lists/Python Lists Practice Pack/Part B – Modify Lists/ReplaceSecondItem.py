# Replace the second item.

items = []

for i in range(5):
        item = input(f"Enter item{i+1} : ")
        items.append(item)

for index, item in enumerate(items, start=1):
        print(f'{index}. {item}')    


replace = input("\nEnter new second item : ")
items[1] = replace

print("\nUpdated list after replacing second item : ")
for index, item in enumerate(items, start=1):
        print(f'{index}. {item}')   


