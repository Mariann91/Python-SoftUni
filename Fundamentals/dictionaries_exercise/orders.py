product_dic_prices = {}
product_dic_quantity = {}

current_product = input()

while current_product != "buy":
  product, price, quantity = current_product.split()
  price = float(price)
  quantity = int(quantity)

  if product in product_dic_prices:
    product_dic_quantity[product] += quantity

  else:
      product_dic_quantity[product] = quantity
  
  product_dic_prices[product] = price

  current_product = input()

for product in product_dic_prices:
  price = product_dic_prices[product]
  quantity = product_dic_quantity[product]
  total_price = price * quantity
  print(f"{product} -> {total_price:.2f}")
  
  
