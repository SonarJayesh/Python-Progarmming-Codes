class Father:
    def father(self):
        print("Father Class")

class Mother:
    def mother(self):
        print("Mother Class")

class Child(Father,Mother):
    def child(self):
        print("Child Class")

child = Child()
child.child()
child.father()
child.mother()

mother = Mother()
mother.mother()
