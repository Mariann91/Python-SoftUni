decoration_dic = {
  "Ornament Set": [2, 5],
  "Tree Skirt": [5, 3],
  "Tree Garland": [3, 10],
  "Tree Lights": [15, 17],
}

decoration_count = int(input())
days_until_christmas = int(input())

total_cost, total_spirit = 0, 0
for day in range(1, days_until_christmas + 1):

  if day % 11 == 0:
    decoration_count += 2

  if day % 10 == 0:
    total_spirit -= 20
    total_cost += decoration_dic["Tree Skirt"][0] + decoration_dic["Tree Garland"][0] + decoration_dic["Tree Lights"][0]
    if day == days_until_christmas:
      total_spirit -= 30

  if day % 5 == 0:
    total_cost += decoration_dic["Tree Lights"][0] * decoration_count
    total_spirit += decoration_dic["Tree Lights"][1] 
    if day % 3 == 0:
      total_spirit += 30

  if day % 3 == 0:
    total_cost += (decoration_dic["Tree Skirt"][0] + decoration_dic["Tree Garland"][0]) * decoration_count
    total_spirit += decoration_dic["Tree Skirt"][1] + decoration_dic["Tree Garland"][1]
  
  if day % 2 == 0:
    total_cost += decoration_dic["Ornament Set"][0] * decoration_count
    total_spirit += decoration_dic["Ornament Set"][1]

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
