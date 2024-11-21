class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

person1 = Person("Alice", 30)
person1.display_details()
person1.celebrate_birthday()
person1.display_details()