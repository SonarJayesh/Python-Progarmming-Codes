#Create a Python class Employee with attributes like name, id, and department. Add methods to display employee details.

class Employee:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

    def dispay(self):
        print("Name: ",self.name)
        print("id: ",self.id)
        print("Department: ",self.department)

name = input("Enter the Employee Name: ")
id = int(input("Enter the Employee Id: "))
department =input("Enter the Employee Department: ")

e = Employee(name, id, department)

e.dispay()