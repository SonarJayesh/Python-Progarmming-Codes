class EmpDemo():
    def __init__(self, eID,eName):
        
        self.eID = eID
        self.eName = eName

        print(f"Employee ID: {eID} Employee Name: {eName}")

    def Welcome(self):
        print("Welcome Python User", self.eName)
        
    def getName(self):
        return self.eName
        
empDemo = EmpDemo(111,"Jayesh")     
empDemo.Welcome()   
print(empDemo.getName())