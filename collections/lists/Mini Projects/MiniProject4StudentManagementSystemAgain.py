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

# function to display students
def show_students():
    if len(students) == 0:
        print("\n========== No Students in List!!! ==========")
    else:
        print("\n========== Students ==========")
        for index, student in enumerate(students, start=1):
            print(f"{index}. {student}")

# function for "No Students"
def has_students():
    if len(students) == 0:
        print("\n========== No Students in List!!! ==========")
        return False
    return True

# Create add_student()
def add_student():
    while True:
        student = input("\nEnter student's name: ").strip().title()

        if student == "":
            print("========== Please enter a student's name! ==========")
            continue

        students.append(student)

        print(f"\n========== '{student}' added successfully! ==========")

        break

# View Students
def view_students():
    show_students()

# Search Student
def search_student():

    if not has_students():
        return

    while True:

        student = input("\nEnter student's name to search: ").strip().title()

        if student in students:
            print(f"\n'{student}' is available.")
            break
        else:
            print(f"\n'{student}' is not in the list. Try again.")

# Remove Student
def remove_student():

    if not has_students():
        return

    while True:

        student = input("\nEnter student's name to remove: ").strip().title()

        if student in students:

            students.remove(student)

            print(f"\n'{student}' removed successfully.")

            show_students()

            break

        else:

            print(f"\n'{student}' not found. Try again.")


# Sort Students
def sort_students():

    if not has_students():
        return

    students.sort()

    print("\nStudents sorted successfully.")

    show_students()

# Count Students
def count_students():

    if not has_students():
        return

    print(f"\nTotal Students : {len(students)}")

# menu
def show_menu():
    print("\n========== Student Management ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Sort Students")
    print("6. Count Students")
    print("7. Exit")

# Remove Student
while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        remove_student()

    elif choice == "5":
        sort_students()

    elif choice == "6":
        count_students()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid choice!")
