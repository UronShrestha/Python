# Challenge 7

# Take two lists of student names and find students who are enrolled in both

list_A = []
list_B = []

for i in range(5):
    studentA = input(f"Enter name of student {i+1} : ").strip().title()
    list_A.append(studentA)

print("\n")

for i in range(5):
    studentB = input(f"Enter name of student {i+1} : ").strip().title()
    list_B.append(studentB)

print("\nStudents in List A : ", list_A)
print("\nStudents in List B : ", list_B)

new_A = set(list_A)
new_B = set(list_B)

both = new_A.intersection(new_B)
print("\nStudents who are enrolled in both : ", both)

if new_A.isdisjoint(new_B):
    print("sets have nothing in common.")
else:
    print("sets have something in common.")