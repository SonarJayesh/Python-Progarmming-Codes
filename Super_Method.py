class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car Started...!")

    @staticmethod
    def stop():
        print("Car Stopped....!")

class ToyotaCar(Car):
    def __init__(self,name, type):
        super().__init__(type)
        self.name = name
        super().start()
        

toyotaCar = ToyotaCar("Ola","Electric")
print(toyotaCar.type)