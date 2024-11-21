class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print(f"{self.make} {self.model} car created!")

    def __del__(self):
        print(f"{self.make} {self.model} car is being destroyed!")

my_car = Car("Toyota", "Corolla")
del my_car