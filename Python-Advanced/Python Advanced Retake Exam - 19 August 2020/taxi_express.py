from collections import deque

customers = deque(int(x) for x in input().split(", "))
taxis = deque(int(x) for x in input().split(", "))

total_time = 0

while customers and taxis:

    customer = customers.popleft()
    taxi = taxis.pop()

    if taxi >= customer:
        total_time += customer
    else:
        customers.appendleft(customer)

if not customers:
    print(f"""All customers were driven to their destinations
Total time: {total_time} minutes""")

if not taxis and customers:
    print(f"""Not all customers were driven to their destinations
Customers left: {', '.join(str(el) for el in customers)}""")
