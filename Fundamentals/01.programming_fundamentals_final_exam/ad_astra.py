import re

pattern = r"(\||#)([A-Z][a-z]+|[A-Z][a-z]+ [A-Z][a-z]+)\1(\d{2}\/\d{2}\/\d{2})\1([0-9]+)\1"

text = input()

result = re.findall(pattern, text)

total_calories = 0
for food in result:
  total_calories += int(food[-1])
print(f"You have food to last you for: {total_calories // 2000} days!")

for food in result:
  print(f"Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[3]}")
  
