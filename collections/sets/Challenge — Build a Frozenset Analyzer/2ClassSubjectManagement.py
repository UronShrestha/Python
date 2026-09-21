# 🏆 MINI PROJECT 2 — Class Subject Management
'''
This one teaches you Set Operations, which are extremely useful.

Imagine two classes:

python_students = {"Alice", "Bob", "John", "David"}
java_students = {"John", "David", "Mike", "Sarah"}

Create a program that displays:

1. Students studying Python
2. Students studying Java
3. Students studying both
4. Students only studying Python
5. Students only studying Java
6. All students
7. Number of students

Your program should use:

union()
intersection()
difference()
'''

python_students = {"Alice", "Bob", "John", "David"}
java_students = {"John", "David", "Mike", "Sarah"}

'''python_students = set()
java_students = set()

for i in range(5):
        python = input(f"Student Name {i+1} for Python class : ")
        python_students.add(python)
        continue

    

print("\n")
for j in range(5):
         java = input(f"Student Name {j+1} Java class : ")
         java_students.add(java)
         continue
'''


while True:
    print("\n========== Class Subject Management ==========")
    print("1. Students studying Python")
    print("2. Students studying Java")
    print("3. Students studying both")
    print("4. Students only studying Python")
    print("5. Students only studying Java")
    print("6. All students")
    print("7. Number of students")
    print("8. Exit")

    choice = input("\nEnter your choice 1-8 : ")

# 1. Students studying Python
    if choice == "1":
        print("\nStudents in Python calss : ")
        for python in python_students:
            print(python)
            

# 2. Students studying Java       
    elif choice == "2":
        print("\nStudents in Java calss : ")
        for java in java_students:
                print(java)
                
        
# 3. Students studying both
    elif choice == "3":
        print("\nStudents studying both : ")
        print(python_students.intersection(java_students))

# 4. Students only studying Python
    elif choice == "4":
          print("\nStudents only studying Python : ")
          print(python_students.difference(java_students))

# 5. Students only studying Java
    elif choice == "5":
         print("\nStudents only studying Java : ")
         print(java_students.difference(python_students))

# 6. All students
    elif choice == "6":
          print("\nStudents studying both Python and Java : ")
          print(java_students.union(python_students))

# 7. Number of students
    elif choice == "7":
         all_students = java_students.union(python_students)
         print("\nNumber of students : ",len(all_students))

# Exit
    elif choice == "8":
         print("Good Bye!!!")
         break

    else:
           print("Invalid Choice!!!")
            
      
   

