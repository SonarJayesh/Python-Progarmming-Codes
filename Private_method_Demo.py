class Person:
    __name = "Jayesh"

    def __hello(self):
        print("Hello Jayesh")

    def welecome(self):
        self.__hello()


person = Person()
print(person.welecome())        
