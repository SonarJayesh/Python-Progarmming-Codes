#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.

class Student():
    def __init__(self,sName,sMarks):
        self.sName = sName
        self.sMarks = sMarks

    def getAvg(self):
        sum = 0
        for val in self.sMarks:
            sum += val
        print("Hi",self.sName,"Your Average Score is: ",sum/3)

student = Student("Jayesh_Sonar",[82,76,95])       
student.getAvg()

student.sName="Ishwar" # Change Attribute Name
student.getAvg()