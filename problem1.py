#  simple calculator 

# Here i used pyhton as programming language where the program is written using oops concept [CLASS].
# There the user can give two inputs and can give required operation to be performed.
# The user can give symbols (+,-,*,/) or can give inpu such as (add,subtract,multiply,divide) in any cases.

class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.strip().lower()   # here i used lowercase, strip spaces to avoid the error of cases

    def calculate(self):
        if self.operation in ["add", "+"]:
            return self.a + self.b
        elif self.operation in ["subtract", "-"]:
            return self.a - self.b
        elif self.operation in ["multiply", "*"]:
            return self.a * self.b
        elif self.operation in ["divide", "/"]:
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation. Use add/subtract/multiply/divide or + - * /"
try:
    a = float(input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))
    operation = input("Enter operation (add, subtract, multiply, divide OR +, -, *, /): ")

    calc = Calculator(a, b, operation)
    result = calc.calculate()
    print(f"Result: {result}")

except ValueError:
    print("Invalid input! Please enter numeric values for a and b.")
