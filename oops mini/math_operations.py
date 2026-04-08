from utils import BaseUtility

class MathOperations(BaseUtility):

    def __init__(self, a, b):
        self.a = a      # encapsulation
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def display(self):
        print("Math Operations")
        print("Addition:", self.add())
        print("Subtraction:", self.subtract())
        print("Multiplication:", self.multiply())


def calculate_power(x, y):
    return x ** y