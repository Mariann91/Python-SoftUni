from collections import deque

quantity_of_food = int(input())
orders = deque(int(num) for num in input().split())

print(max(orders) if orders else None)

while orders:
    order = orders[0]

    if order <= quantity_of_food:
        quantity_of_food -= order
        orders.popleft()
    else:
        print("Orders left:", *orders, sep=" ")
        break
else:
    print("Orders complete")
