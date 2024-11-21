class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_details(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")
    
    def start(self):
        print(f"{self.make} {self.model} is now started!")
    
    def stop(self):
        print(f"{self.make} {self.model} has stopped.")

my_car = Car("Toyota", "Corolla", 2020)
my_car.display_details()
my_car.start()
my_car.stop()