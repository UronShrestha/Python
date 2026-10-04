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
Computer: 78

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

# Ask the user for marks of 5 subjects.
subjects = []
marks = []
grades = []
failed_subjects = []

for i in range(5):
    while True:
        subject = input(f"Enter name for subject{i+1} : ").strip().title()
        if subject == "":
            print("No Subject Added!")
            continue
        elif subject in subjects:
            print(f"{subject} already added!")
            continue
        else:
            subjects.append(subject)
        break

    
#Enter marks:
# Python: 85
# Math: 72
# English: 64
# Science: 91
# Computer: 78

    while True:
        mark = input(f"Enter marks for {subject} : ").strip()
        # mark = float(mark)
        if mark == "":
            print("No Marks Added!")
            continue
        try:
            mark = float(mark)
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        if mark > 100 or mark <0:
            print("Mark can be in between 0.00 to 100.00")
            continue
        else:
            marks.append(mark)
            break    

# Then display:

# ========== RESULT ==========

# Marks: [85, 72, 64, 91, 78]

# Total: 390
# Average: 78.0
# Highest: 91
# Lowest: 64

# Result: PASS
# Grade: A
# Rules

# A student fails if any subject is below 40.

# Grade:

# 90+  → A+
# 80+  → A
# 70+  → B
# 60+  → C
# 50+  → D
# Below 50 → F

print()
print("\n========== RESULT ==========")
for i in range(5):
    if marks[i]>=90:
        grade = "A+"
    elif marks[i]>=80:
        grade = "A"
    elif marks[i] >= 70:
        grade = "B"
    elif marks[i] >= 60:
        grade = "C"
    elif marks[i]>= 50:
        grade = "D"
    else:
        grade = "F"

    grades.append(grade)

    if grade == "F":
        failed_subjects.append(subjects[i])
    

    print(f"{i+1}.{subjects[i]} : {marks[i]} - {grades[i]}")
print("\nTotal : ", sum(marks))
print("Average : ", sum(marks)/len(marks))
print("Highest : ",max(marks))
print("Lowest : ",min(marks))

if len(failed_subjects)>0:
    print("Result : Failed!" )
    print("\nFailed subjects : ")

    for subject in failed_subjects:
        print(f"- {subject}")
else:
    print("Result : Passed!" )
