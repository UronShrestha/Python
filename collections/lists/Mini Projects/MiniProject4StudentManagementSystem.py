'''
Mini Project – Student Management System
Description

Build a console application that manages students using a list.

Requirements
========== Student Management ==========
1. Add Student
2. View Students
3. Search Student
4. Remove Student
5. Sort Students
6. Count Students
7. Exit
'''

students = []

for i in range(3):
    student = input(f"Enter name of student{i+1} : ")
    students.append(student)

for index, student in enumerate(students, start=1):
    print(f"{index}. {student}")

while True:
    print("\n========== Student Management Menu ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Sort Students")
    print("6. Count Students")
    print("7. Exit")

    choice = input("\nChoose option between 1 to 7 : ")

    if choice == "1":
        while True:
            add_student = input("Enter name of a student : ")
            if add_student == "":
                print("========== Please Enter Student's Name!!! ==========")
                continue

            else:
                print("========== New Student Added Successfully!!! ==========")

                students.append(add_student)
                for index, add_student in enumerate(students, start=1):
                    print(f"{index}. {add_student}")

            break

    # if choice == "2"
    # if choice == "3"
    # if choice == "4"
    # if choice == "5"
    # if choice == "6"
    # if choice == "7"


