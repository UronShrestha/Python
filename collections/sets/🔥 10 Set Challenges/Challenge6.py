# Challenge 6

'''
Ask the user to enter 10 names.

Store them in a set.

Print the number of unique names.
'''

names = set()
count = 0
for i in range(10):
    name = input(f"Enter name {i+1} : ").title().capitalize()
    names.add(name)
print("All names in set : ",names)
print("Number of unique names in set : ", len(names))



    


