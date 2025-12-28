class Parent:
    def parent(self):
        print("Parent Class")

class Child1(Parent):
    def child1(self):
        print("Child1 Class") 

class Child2(Parent):
    def child2(self):
        print("Child2 Class") 


child1 = Child1()                     
child2 = Child2()   

child1.parent()
child2.parent()

