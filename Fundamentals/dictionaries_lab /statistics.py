command = input()

product_dic = {}
while command != "statistics":
  key, value = command.split(": ")
  value = int(value)

  if key not in product_dic.keys():
    product_dic[key] = value
  else:
    product_dic[key] += value
  
  command = input()

print(f"Products in stock:")

for key, value in product_dic.items():
  print(f"- {key}: {value}")

count_all_products = len(product_dic)

print(f"Total Products: {count_all_products}")

sum_all_quantities = sum(product_dic.values())

print(f"Total Quantity: {sum_all_quantities}")
