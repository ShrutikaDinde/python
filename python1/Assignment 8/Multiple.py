class Father:
    def father_method(self):
        print("Father class method")

class Mother:
    def mother_method(self):
        print("Mother class method")

class Child(Father, Mother):
    def child_method(self):
        print("Child class method")

c = Child()
c.father_method() 
c.mother_method() 
c.child_method() 
