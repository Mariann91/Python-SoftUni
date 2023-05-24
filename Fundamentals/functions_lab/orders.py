def calculate(item, quantity):
    total_price = 0
    if item == "coffee":
        total_price = 1.50 * quantity
    elif item == "water":
        total_price = 1.00 * quantity
    if item == "coke":
        total_price = 1.40 * quantity
    if item == "snacks":
        total_price = 2.00 * quantity
    return total_price


product = input()
count = int(input())

print(f"{calculate(product, count):.2f}")
