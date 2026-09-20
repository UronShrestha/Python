# Check an Item Red in set of colors

colors = set()

for i in range(5):
    while True:
        color = input(f"Enter color name {i+1} : ").capitalize()
        if color == '':
            print("No name entered!")
            continue
        else:
            colors.add(color)
        break
print(colors)

while True:
    color = input("Enter name of color to find : ").capitalize()
    if color == "":
        print("Please Enter a Color Name!")
    elif color in colors:
        print(f"{color} exists in set.")
        break
    else:
        print(f"{color} does not exist in set.")

