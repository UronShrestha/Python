# 🟡 Project 3 — Student Marks Analyzer
# Difficulty: ⭐⭐

subjects = []
marks = []
grades = []
failed_subjects = []

for i in range(5):
    while True:
        subject = input(f"Enter name of subject{i+1} : ").strip().capitalize()
        if subject == "":
            print("No input given!")
            continue
        elif subject in subjects:
            print(f"{subject} is already in list.")
        else:
            subjects.append(subject)
            break

    while True:
        mark = input(f"Enter mark for {subject} : ")
        if mark == "":
            print("No input given!")
            continue
        
        try:
            mark = float(mark)
        except ValueError:
            print("Mark can be only of int or float data type!")
            continue

        if mark < 0 or mark > 100:
            print("Mark can only be in between 1 to 100!")
        else:
            marks.append(mark)
            break

# Then display:

print("\n========== RESULT ==========")
print("Marks : ", marks)
print("Total : ", sum(marks))
print("Average : ", sum(marks)/len(marks))
print("Highest: ",max(marks))
print("Lowest: ",min(marks))

for i in range(5):
    if marks[i] > 90 :
        grade = "A+"
    elif marks[i] > 80 :
        grade = "A"
    elif marks[i] > 70:
        grade = "B+"
    elif marks[i] > 60:
        grade = "B"
    elif marks[i] > 50:
        grade = "C+"
    elif marks[i] > 40:
        grade = "C"
    else:
        grade = "F"

    grades.append(grade)

    if grade == "F":
        failed_subjects.append(subjects[i])


if len(failed_subjects)>0:
    print("Result : Failed")
    print("Failed Subjects : ")

    for subject in failed_subjects:
        print(f"- {subject}")
else:
    average = sum(marks)/len(marks)
    if average > 90 :
        gpa = "A+"
    elif average > 80 :
        gpa = "A"
    elif average > 70:
        gpa = "B+"
    elif average > 60:
        gpa = "B"
    elif average > 50:
        gpa = "C+"
    elif average > 40:
        gpa = "C"
    else:
        gpa = "F"    
    print("Result : Passed")
    print("Grade : ", gpa)
