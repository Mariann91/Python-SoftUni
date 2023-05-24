def add_and_subtract(n1, n2, n3):
    def sum_numbers():
        return n1 + n2

    def subtract():
        return sum_numbers() - n3

    return subtract()


num1, num2, num3 = int(input()), int(input()), int(input())
print(add_and_subtract(num1, num2, num3))
