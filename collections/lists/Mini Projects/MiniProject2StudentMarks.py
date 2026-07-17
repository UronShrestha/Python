"""
⭐ Mini Project 2 – Student Marks

Take marks for 5 subjects and:

Store them in a list.
Print all marks.
Print highest mark.
Print lowest mark.
Print average mark.
Print Pass if all marks are at least 40; otherwise print Fail.
"""

student_marks = [] #empty list

# Take marks for 5 subjects
for i in range(5):
    while True:
        try:
            mark = input(f"Enter the mark is subject{i+1} : ")

            if mark == "":
                print("Please enter the mark.")
                continue
            mark = float(mark)

            if mark<0 or mark>100:
                print("Please enter the mark in between 0 to 100.")
                continue
            
            student_marks.append(mark)
            break
            
        except ValueError:
            print("Please enter valid number only from 1 to 100.")

print("\n------All Marks------")
# Print all marks.
index = 1
for all_marks in student_marks:
      print(f"Item{index}. {all_marks}")
      index+=1

# Print lowest mark.
print("\nLowest Mark : ", min(student_marks))

# Print Highest Mark.
print("\nHighest Mark : ", max(student_marks))

# Print average mark.
avg = sum(student_marks)/len(student_marks)
print(f"\nAverage mark : {avg:.2f}")

            
# Print Pass if all marks are at least 40; otherwise print Fail.
print("\n-----RESULT-----")
passed = True
for mark in student_marks:
    if mark<40:
        passed = False
        break
if mark>40:
    print("Result : Passed")
else:
    print("Result : Failed")

# Print Divisions
print("\n-----DIVISION-----")
if avg>=80:
     print("Division: Distinction")
elif avg>=60:
    print("Division : First Division")
elif avg>=50:
    print("Division : Second Division")
elif avg>=40:
    print("Division : Third Division")
else:
    print("Division : Failed\n")



 