food_list = [item for item in input().split()]

food_dic = {}
for i in range(0, len(food_list), 2):
  key = food_list[i]
  value = food_list[i + 1]
  
  food_dic[key] = int(value)
  
searched_products = [item for item in input().split()]

for product in searched_products:
  if product in food_dic.keys():
    print(f"We have {food_dic[product]} of {product} left")
  else:
      print(f"Sorry, we don't have {product}")
    
