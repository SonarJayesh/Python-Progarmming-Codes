class A:
    def showA(self):
        print("This is Show A")    

class B(A):
    def showB(self):
        print("This is Show B")
    
class C(B):
    def showC(self):
        print("This is Show C")   


c = C()
c.showC()
c.showA()
c.showB()

b = B()
b.showA()
b.showB()