class Calculator2(object):

    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.operation = ""

    def add (self):
        return self.number1 + self.number2

    def subtract (self):
        return self.number1 - self.number2

    def multiply (self):
        return self.number1 * self.number2

    def divide (self):
        return self.number1 / self.number2

    def print_text(self):
        print "Welcome! Enter your choice of operation."
        print """
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        """

    def user_input(self):
        operation = raw_input("> ")
        print "Enter number 1: "
        self.number1 = int(raw_input(">"))
        print "Enter number 2: "
        self.number2 = int(raw_input("> "))
        self.operation = operation

    def calculation(self):
        self.print_text()
        self.user_input()

        if self.operation == "1" :
            print self.add()

        elif self.operation == "2" :
            print self.subtract()

        elif self.operation == "3" :
            print self.multiply()

        elif self.operation == "4":
            print self.divide()

        else:
            print "ERROR"


obj = Calculator2()
obj.calculation()
