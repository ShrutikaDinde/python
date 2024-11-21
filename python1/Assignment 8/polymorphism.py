class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")

class Cat(Animal):
    def sound(self):
        print("The cat meows")

def animal_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()
animal_sound(dog)
animal_sound(cat)  
