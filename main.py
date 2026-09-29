class Calculator:
    def add(self, a, b):
        return (a+b)

    def sub(self, a, b):
        return (a-b)

    def mul(self, a, b):
        return (a*b)

calc = Calculator()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", calc.add(a, b))
print("Subtraction:", calc.sub(a, b))
print("Multiplication:", calc.mul(a, b))
