food_list = [item for item in input().split()]

food_dic = {}
for i in range(0, len(food_list), 2):
  key = food_list[i]
  value = food_list[i + 1]
  
  food_dic[key] = int(value)
  
print(food_dic)  
