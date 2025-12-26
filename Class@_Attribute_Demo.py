class Person:
    name = "anonomus"
    
    @classmethod
    def changeName(cls,name):
        cls.name = name


person = Person()
person.changeName("Jayesh Sonar") 
print(person.name)
print(Person.name)       