class Grandparent:
    def grandparent_method(self):
        print("Grandparent class method")

class Parent(Grandparent):
    def parent_method(self):
        print("Parent class method")

class Child(Parent): 
    def child_method(self):
        print("Child class method")

c = Child()
c.grandparent_method()
c.parent_method()     
c.child_method()    