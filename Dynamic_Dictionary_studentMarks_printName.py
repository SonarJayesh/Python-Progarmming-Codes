#Create a dictionary of students marks and print only the names of students scoring above 80.

student = {}
n = int(input("Enter the Number of Students:"))

for i in range(n):
    name = input("Enter the Name: ")
    marks = int(input("Enter the Marks:"))
    student[name] = marks

print("Student Scorring above 80:")
for name, marks in student.items():
    if marks > 80:
        print(name)    