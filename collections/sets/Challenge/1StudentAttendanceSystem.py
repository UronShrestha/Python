# 🏆 MINI PROJECT 1 — Student Attendance System

"""
This is the best first Sets project for where you are right now.

Requirements

Create a program that stores students who attended class.

Menu
========== ATTENDANCE SYSTEM ==========

1. Add Student
2. View Students
3. Check Student
4. Remove Student
5. Count Students
6. Exit
"""

students = set()


while True:
    print("\n========== ATTENDANCE SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Student")
    print("4. Remove Student")
    print("5. Count Students")
    print("6. Exit")

    choice = input("\nEnter your choice from 1 - 6 : ")

# 1. Add Student
    if choice == "1":
        while True:
            student = input("\nEnter name of student : ").strip().capitalize()

            if student == "":
                print("========== Please Enter Student's Name!!! ==========")
                continue
            

            if student in students:
                print(f"\n{student} already exists in the list.")
                continue

            # else:
            students.add(student)
            print(f"========== New Student '{student}' Added Successfully!!! ==========")
            break

# 2. View Students
    elif choice == "2":
        if len(students)==0:
            print("No Student had been added yet!!!")
        else:
            print("Sets of students : ")
            for student in students:
                print(student)

# 3. Check Student
    elif choice == "3":
        while True:
            student = input("\nEnter name of student to check : ").strip().capitalize()

            if student=="":
                print("========== Please Enter Student's Name!!! ==========")
                continue
            elif student in students:
                print(f"{student} is present in the set.")
                break
            else:
                print(f"{student} is not present in the set.")
            
# 4. Remove Student
    elif choice == "4":
        while True:
            if len(students) == 0:
                print("========== No Student Available!!! ==========")

            student = input("\nEnter name of student to remove : ").strip().capitalize()

            if student == "":
                print("========== Please Enter Student's Name!!! ==========")
                continue
            elif student not in students:
                print(f"{student} is not in set!!!")
                continue
            else:
                students.remove(student)
                print(f"=========={student} removed successfully!!! ==========")
                print(f"\n========== New Student Set ==========")
                for student in students:
                    print(student)
            break
                

# 5. Count Students

    elif choice == "5":
       if len(students) == 0:
                print(f"\n========== No Students in Set ==========")
           
    #    count_students = 0
    #    for student in students:
    #     count_students+=1

       print("Number of students : ", len(students))
# 6. Exit

    elif choice == "6":
        print("EXIT SUCCESSFULL!!!")
        break
    
         
    else:
        print("INVALID CHOICE!!!")
        continue