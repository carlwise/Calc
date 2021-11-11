"""
calc_class.py

A simple calculator written using Python, using classes.
"""


class Keyboard():

    def get_input(self, prompt):
        return input(prompt)

class Screen():

    def print(self, label, value):
        print(f"{label}: {value}")

class Memory():
    
    def write(self, line):
        f = open("results", "a")
        template = f"{line}\n"
        f.write(template)
        f.close()

class Handler():

    def handle(self, expression):
        operator = None
        operand_1 = None
        operand_2 = None
        error = None
        try:
            tokens = expression.split(" ")
            operator = tokens[1]
            operand_1 = int(tokens[0])
            operand_2 = int(tokens[2])
        except Exception as exception:
            error = "Invalid expression"
            
        return operator, operand_1, operand_2, error

class BasicCalculator():

    vendor = "Python"
    model = "basic"

    # BasicCalculator HAS A Keyboard
    keyboard = Keyboard()

    # BasicCalculator HAS A Screen
    screen = Screen()

    # BasicCalculator HAS A Memory
    memory = Memory()

    # BasicCalculator HAS A Handler
    handler = Handler()

    def get_expression(self):
        return self.keyboard.get_input("Expression: ")

    def evaluate_expression(self, expression):
        operator, operand_1, operand_2, error = self.handler.handle(expression)
        if error:
            self.screen.print("Error", error)
            self.memory.write({"error": error})
            exit(1)
        else:
            return operator, operand_1, operand_2

    def print(self, operator, operand_1, operand_2, result):
        self.screen.print("Operator", operator)
        self.screen.print("Operand 1", operand_1)
        self.screen.print("Operand 2", operand_2)
        self.screen.print("Result", result)

    def write(self, operator, operand_1, operand_2, result):
        operation = {
            "operator": operator,
            "operand_1": operand_1,
            "operand_2": operand_2,
            "result": result
        }
        self.memory.write(operation)

    def calculate(self, operator, operand_1, operand_2):
        if operator == "+":
            result = self.sum(operand_1, operand_2)
        elif operator == "-":
            result = self.subtract(operand_1, operand_2)
        elif operator == "*":
            result = self.multiply(operand_1, operand_2)
        elif operator == "/":
            result = self.divide(operand_1, operand_2)
        else:
            self.screen.print("Error", "invalid operator")
            self.memory.write({"error": "invalid operator"})
            exit(1)
        self.print(operator, operand_1, operand_2, result)
        self.write(operator, operand_1, operand_2, result)

    def sum(self, operand_1, operand_2):
        return operand_1 + operand_2
    
    def subtract(self, operand_1, operand_2):
        return operand_1 - operand_2

    def multiply(self, operand_1, operand_2):
        return operand_1 * operand_2

    def divide(self, operand_1, operand_2):
        if operand_2 == 0:
            self.screen.print("Error", "can not divide by zero")
            self.memory.write({"error": "can not divide by zero"})
            exit()
        else:
            return int(operand_1 / operand_2)

# PowerCalculator IS A BasicCalculator
class PowerCalculator(BasicCalculator):

    model = "power"

    def calculate(self, operator, operand_1, operand_2):
        if operator == "^" or operator == "**":
            result = self.power(operand_1, operand_2)
            self.print(operator, operand_1, operand_2, result)
            self.write(operator, operand_1, operand_2, result)
        elif operator == "%":
            result = self.modulus(operand_1, operand_2)
            self.print(operator, operand_1, operand_2, result)
            self.write(operator, operand_1, operand_2, result)
        else:
            super().calculate(operator, operand_1, operand_2)

    def power(self, operand_1, operand_2):
        return operand_1 ** operand_2

    def modulus(self, operand_1, operand_2):
        return operand_1 % operand_2

if __name__ == "__main__":

    # Create a new calculator
    #calculator = BasicCalculator()
    calculator = PowerCalculator()

    # Get the expression from keyboard
    expression = calculator.get_expression()

    # Evaluate the expression
    operator, operand_1, operand_2 = calculator.evaluate_expression(expression)

    # Calculate
    calculator.calculate(operator, operand_1, operand_2)
