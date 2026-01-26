#Write a Python program to demonstrate method overriding in inheritance.

class Parent:
    def show(self):
        print("This is Parent Class")

class Child(Parent):
    def show(self):
        print("This is Child Class")


obj = Child()
obj.show()
