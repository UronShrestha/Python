"""Project 5 — Student Attendance System
Difficulty: ⭐⭐
This is one you've already been working toward, so now build it from scratch without looking at your previous code.
========== ATTENDANCE SYSTEM ==========

1. Add Student
2. Remove Student
3. Check Student
4. View Students
5. Count Students
6. Exit

Use:
students = set()


Example
Enter choice: 1
Enter student name: Alice

Alice added successfully.

If Alice already exists:
Alice is already present.

Requirements
Use:
- Set
- add()
- remove() or discard()
- in
- for
- len()
- while
- if / elif / else
Bonus
Don't allow empty names."""

students = set()

while True:
    print("========== ATTENDANCE SYSTEM ==========")
    print("\n========== MENU ==========")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Check Student")
    print("4. View Students")
    print("5. Count Students")
    print("6. Exit")

    choice = input("Enter your choice from 1 to 6 : ")

    # print("1. Add Student")

    if choice == "1":
        while True:
            student = (
                input("Enter name of a student to add into set : ").strip().title()
            )
            if student == "":
                print("Please enter name of a student.")
                continue
            elif student in students:
                print(f"{student} already in present.")
                continue
            else:
                print(f"{student} added successfully.")
                students.add(student)
                break

    # print("2. Remove Student")
    elif choice == "2":
        while True:
            if len(students) == 0:
                print("NO STUDENTS IN SET")
                break

            student = input("Enter name of a student to remove : ").strip().title()

            if student == "":
                print("Please enter name of a student.")
                continue
            elif student in students:
                students.remove(student)
                print(f"{student} removed successfully!.")
                break
            else:
                print(f"{student} not in list.")

            # elif student not in students:
            #      print(f"{student} not in list.")

    # print("3. Check Student")
    elif choice == "3":
        while True:
            if len(students) == 0:
                print("NO STUDENTS IN SET")
                break

            student = input("Enter name of a student to check : ").strip().title()

            if student == "":
                print("Please enter name to check.")
                continue
            elif student in students:
                print(f"{student} is present in list.")
                break
            else:
                print(f"{student} is not present in list.")

    # print("4. View Students")
    elif choice == "4":
        if len(students) == 0:
            print("No Students in List!")
        else:
            for index, student in enumerate(students, start=1):
                print(f"{index} : {student}")

    #  print("5. Count Students")
    elif choice == "5":
        print("No. of students in list : ", len(students))

    #  print("6. Exit")
    elif choice == "6":
        print("THANK YOU FOR VISITING!")
        break

    else:
        print("Invalid input!")
        continue


# for index, item in enumerate(shopping_list, start=1):
#                  print(f"|{index}     | {item}       |")
