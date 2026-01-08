class Car:
    color = "Blue"
    @staticmethod
    def start():
        print("Car is Started....!")

    def stop():
        print("Car is Stopped....!")

class toyotaCar(Car):

    def __init__(self,name):
        self.name = name
                

car1 = toyotaCar("fortuner")
car2 = toyotaCar("prius")

print(car1.start())
print(car1.color)