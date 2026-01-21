#Create a dictionary of students' marks and print only the names of students scoring above 80.

marks = {
    "Ritesh" : 75,
    "Jayesh" : 85,
    "Shubham" : 82,
    "Umesh" : 78
}
for name, score in marks.items():
    if score > 80:
        print(name)