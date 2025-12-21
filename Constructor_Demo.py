class Employee():
    def __init__(self,empID,empName):
        

        self.empID = empID
        self.empName = empName
        print(f"EmpId={self.empID} Name = {self.empName}")
        

employee = Employee(101,"Jayesh")
employee2 = Employee(102,"Ishwar")
