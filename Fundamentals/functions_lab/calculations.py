def calculate(operator, n1, n2):
    if operator == "multiply":
        return n1 * n2
    elif operator == "divide":
        return n1 // n2
    elif operator == "add":
        return n1 + n2
    elif operator == "subtract":
        return n1 - n2


operation = input()
num1 = int(input())
num2 = int(input())

print(calculate(operation, num1, num2))
