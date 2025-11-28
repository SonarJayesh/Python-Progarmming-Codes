# Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

x = float(input("Enter the Python Marks: "))
marks.update({"python" : x})

x = float(input("Enter the Java Marks:5 "))
marks.update({"java" : x})

x = float(input("Enter the Cpp Marks: "))
marks.update({"cpp" : x})

print(marks)

