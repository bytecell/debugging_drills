import pdb

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value

    def divide(self, value):
        self.result /= value

calc = Calculator()

calc.add(10)
calc.divide(0)

print("Final Result:", calc.result)
