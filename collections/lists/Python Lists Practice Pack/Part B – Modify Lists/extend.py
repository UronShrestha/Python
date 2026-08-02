# Add three new items using extend().

items = []

for i in range(5):
        item = input(f"Enter item{i+1} : ")
        items.append(item)

for index, item in enumerate(items, start=1):
        print(f'{index}. {item}')    

for replace in range(3):
    replace = input("\nAdd three new items : ")
    items.extend(replace)

print("\nUpdated list after adding three new items : ")
for index, item in enumerate(items, start=1):
        print(f'{index}. {item}')   


