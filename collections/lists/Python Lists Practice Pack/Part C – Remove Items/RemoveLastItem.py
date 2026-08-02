# Remove last item.

items = []

for i in range(5):
        item = input(f"Enter item{i+1} : ")
        items.append(item)
print("\nBefore : ")
for index, item in enumerate(items, start=1):
        print(f'{index}. {item}')    


print(f"\nUpdated list after removing '{items[-1]}' : ")
items.pop()
for index, item in enumerate(items, start=1):
        print(f'{index}. {item}')   

 
