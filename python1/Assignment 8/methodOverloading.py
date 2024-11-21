class MathOperations:
    def add(self, a=0, b=0, c=0):
        return a + b + c

math_op = MathOperations()

print(math_op.add(5, 10)) 
print(math_op.add(5, 10, 15)) 
print(math_op.add(5))          
