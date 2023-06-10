part_price = input()

total_price = 0
while part_price != "special" and part_price != "regular":
    part_price = float(part_price)

    if part_price < 0:
        print("Invalid price!")
    else:
        total_price += part_price

    part_price = input()

taxes = total_price * 0.20
price_with_taxes = total_price + taxes

if part_price == "special":
    price_with_taxes -= price_with_taxes * 0.10

if total_price > 0:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {price_with_taxes:.2f}$")
else:
    print("Invalid order!")
