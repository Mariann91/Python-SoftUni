resource_dic = {}
while True:
  resource = input()

  if resource == "stop":
    break

  quantity = int(input())

  if resource not in resource_dic:
    resource_dic[resource] = quantity
  else:
    resource_dic[resource] += quantity

for resource, quantity in resource_dic.items():
  print(f"{resource} -> {quantity}")
  
