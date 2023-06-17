total_price = 0

parts_price = input()

while parts_price != "special" and parts_price != "regular":
    parts_price = float(parts_price)

    if parts_price < 0:
        print("Invalid price!")
    else:
        total_price += parts_price

    parts_price = input()

taxes = total_price * 0.20
price_with_taxes = total_price + taxes

if parts_price == "special":
    price_with_taxes *= 0.90


if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {price_with_taxes:.2f}$")
