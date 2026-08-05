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

# for i in range(3):
#     student = input(f"Enter name of student{i+1} : ")
#     students.append(student)

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

# Add Student
    if choice == "1":
        while True:
            student = input("\nEnter name of a student : ").capitalize()
            if student == "":
                print("========== Please Enter Student's Name!!! ==========")
                continue

            elif student in students:
                 print(f"{student} already exists in the list.")
                 continue

            while True:
                try:
                    mark = float(input("\nEnter mark of a student : ").capitalize())
                    if mark < 0 or mark > 100:
                        print("========== Marks must be between 0 and 100! ==========")
                        continue

                    break
                except ValueError:
                    print("========== Only integers or floats are allowed! ==========")

            print(f"========== New Student '{student}' Added Successfully!!! ==========")
            students.append([student, mark])

            break

# View Students
    elif choice == "2":
        if not students:
            print("\n========== No Students Available! ==========")
        else:
            print("\n+-----+----------------------+-------+")
            print("            LIST OF STUDENTS |")
            print("\n+-----+----------------------+-------+")
            print("| No. | Name                 | Marks |")
            print("+-----+----------------------+-------+")

            for index, student in enumerate(students, start=1):
                print(f"| {index:<3} | {student[0]:<20} | {student[1]:<5} |")

            print("+-----+----------------------+-------+")


#Search Student
        
    elif choice == "3":            
            if len(students) == 0:
                print("\n========== No Students in List!!! ==========")
            else:
                while True:
                    student = input("\nEnter name of a student to search in list : ").capitalize()
                    if student == "":
                        print("Please enter a name.")
                        continue
                    
                    elif student in students:
                        print(f"\n========== Student named {student} is available in list. ==========")
                        print("\n========== List of Student's in the list!!! ==========")
                        for index, student in enumerate(students, start=1):
                            print(f"{index}. {student}")
                    else:
                        print(f"\n========== Student named {student} is not available in list. ==========")
                    break

#Remove Student

    elif choice == "4":
        if len(students) == 0:
            print("\n========== No Students in List!!! ==========")
        else:
            while True:
                student = input("\nEnter name of a student to remove from the list : ").capitalize()
                if student == "":
                     print("Please enter a name!!!")
                     continue
                elif student in students:
                    students.remove(student)
                    print(f"\n========== Student named {student} removed from the List!!! ==========")
                    print("\n========== List of New Students!!! ==========")
                    for index, student in enumerate(students, start=1):
                        print(f"{index}. {student}")
                    break
                    
                else:
                    print(f"\n========== Student named {student} is not in the List!!! ==========")
                    

#Sort Students
    elif choice == "5":
        if len(students) == 0:
            print("\n========== No Students in List!!! ==========")
        else:
            students.sort()
            print("\n========== Sorted List of Students!!! ==========")
            for index, student in enumerate(students, start=1):
                                    print(f"{index}. {student}")
            

#Count Students
    elif choice == "6":
        count = 0
        if len(students) == 0:
            print("\n========== No Students in List!!! ==========")
        else:
            #  print("Number of students : ",len(students))
            for student in students:
             count+=1
        print("\nNumber of students : ",count)
             


    elif choice == "7":
        print("\n========== THANK YOU!!! ==========")
        break

    else:
         print("Invalid Choice!!!")
    # break


