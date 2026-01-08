class Student:
    def __init__(self,java,python,dataStructure):
        self.java = java
        self.python = python
        self.dataStructure = dataStructure

    @property
    def percentage(self):
        return str((self.java+self.python+self.dataStructure) /3)+"%"

student = Student(97,88,72)
print(student.percentage)     
student.java = 88
print(student.java)  
print(student.percentage) 