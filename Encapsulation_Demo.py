#Encapsulation Demo Code
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False

    def start(self):
        self.cluch = True
        self.acc = True    

        print("Car Started....")

car = Car()
car.start()        