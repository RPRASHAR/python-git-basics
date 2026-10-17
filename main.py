class MathFunction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    
    def substraction(self):
        return self.a - self.b

obj = MathFunction(10, 5)
print(obj.addition())
print(obj.substraction())