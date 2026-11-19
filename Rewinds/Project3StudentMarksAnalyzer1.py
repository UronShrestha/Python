# Project 3 — Student Marks Analyzer
# Difficulty: ⭐⭐
'''
Ask the user for marks of 5 subjects.

Example:

Enter marks:

Python: 85
Math: 72
English: 64
Science: 91
Computer: 78 '''

subjects = []
marks = []
grades = []
failedSubjects = []

print("")
for i in range(5):
    while True: 
        subject = input(f"Enter name of subject{i+1} : ").strip().title()
        if subject == "":
            print("Please enter name of subject!")
            continue
        elif subject in subjects:
            print(f"{subject} is already in list of subjects!")
            continue
        else:
            subjects.append(subject)
        break

    while True:    
        mark = input(f"Enter mark of {subject} : ")
        if mark == "":
            print("Please enter mark!")
            continue
        try:
            mark = float(mark)
        except ValueError:
            print("Marks can be only integers!")

        if mark < 0 or mark > 100:
            print("Marks can be only in between 0 and 100!") 
            continue
        else:
            marks.append(mark)
        break

print("")

'''
Then display:

========== RESULT ==========

Marks: [85, 72, 64, 91, 78]

Total: 390
Average: 78.0
Highest: 91
Lowest: 64

Result: PASS
Grade: A
Rules

'''

print("========== RESULT ==========")

for i in range(len(subjects)):
    if marks[i]>=90:
        grade = "A+"
    elif marks[i]>=80:
        grade = "A"
    elif marks[i]>=70:
        grade = "B"
    elif marks[i]>=60:
        grade = "C"
    elif marks[i]>=50:
        grade = "D"
    else:
        grade = "F"

    grades.append(grade)

    if grade == "F":
        failedSubjects.append(subjects[i])


for subject, mark, grade in zip(subjects, marks, grades):
    print(f"{subject} : {mark:g} - {grade}")

print("\nTotal : ", sum(marks))
print("Average : ", sum(marks)/len(marks))
print("Highest : ", max(marks))
print("Lowest : ", min(marks))

if len(failedSubjects) > 0:
    print("Result : FAILED")
    print("\nFailed Subjects : ")

    for failedSubjects, mark, grade in zip(failedSubjects, marks, grades):
        print(f"{failedSubjects} : {mark:g} - {grade}")
else:
        print("Result : Passed")


'''

A student fails if any subject is below 40.

Grade:

90+  → A+
80+  → A
70+  → B
60+  → C
50+  → D
Below 50 → F
Bonus

Display failed subjects.

Example:

Failed Subjects:
Math
Science

This project combines lists + loops + conditions + calculations.'''