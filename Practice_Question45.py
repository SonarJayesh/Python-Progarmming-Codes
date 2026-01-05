"""
Qs. Define a Employee class with attributes role, department & salary. This class also show has a showDetails() method.
Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.
"""

class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary


    def showDetails(self):
        print("Role=",self.role)
        print("Department=",self.department)
        print("Salary=",self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT",50000)



engineer1 = Engineer("Jayesh",21)    
engineer1.showDetails()

