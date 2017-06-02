class Calculator(object):

    def add (self, a, b):
        return a + b
## w/out init we have to adopt outside parameters
    def subtract (self, a, b):
        return a - b
    def multiply (self, a, b):
        return a * b
    def divide (self, a, b):
        return a / b

result = Calculator()
print result.add(4, 5)

class Calculator2(object):

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2 

    def add (self):
        return self.number1 + self.number2

    def subtract (self):
        return self.number1 - self.number2

    def multiply (self):
        return self.number1 * self.number2

    def divide (self):
        return self.number1 / self.number2

result2 = Calculator2(3, 9)
print result2.add()
