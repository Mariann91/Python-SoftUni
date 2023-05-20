items_list = input().split("|")
budget = int(input())

PROFIT_PERCENT = 0.4
TICKET_PRICE = 150

total_profit = 0
sold_price_list = []

for item in items_list:
    item_list = item.split("->")
    price = float(item_list[1])
    profit = 0

    if item_list[0] == "Clothes" and price <= 50 and price <= budget:
        budget -= price
        profit += price * PROFIT_PERCENT
        sold_price = price + profit
        sold_price_list.append(sold_price)

    elif item_list[0] == "Shoes" and price <= 35 and price <= budget:
        budget -= price
        profit += price * PROFIT_PERCENT
        sold_price = price + profit
        sold_price_list.append(sold_price)

    elif item_list[0] == "Accessories" and price <= 20.50 and price <= budget:
        budget -= price
        profit += price * PROFIT_PERCENT
        sold_price = price + profit
        sold_price_list.append(sold_price)

    total_profit += profit

for item in sold_price_list:
    print(f"{item:.2f}", end=" ")

print()
print(f"Profit: {total_profit:.2f}")

total_budget = budget + sum(sold_price_list)

if total_budget >= TICKET_PRICE:
    print("Hello, France!")
else:
    print("Not enough money.")
