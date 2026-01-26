#Using a for loop, iterate over a dictionary and print its keys and values.

student = {}

n = int(input("Enter the Number of Student:"))

for i in range(n):
    key  = input("Enter the Key:")
    value = input("Enter the value")
    student[key] = value

for key,value in student.items():
    print(key,":",value)