class Student():

    studID = "notDefines"
    studName = "notDefines"

    def __init__(self):
        
        self.studID = 101
        self.studName = "jayesh"

student =Student()
print(student.studID,student.studName)

print(Student.studID,Student.studName)