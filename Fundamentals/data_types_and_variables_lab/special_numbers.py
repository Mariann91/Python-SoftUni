number = int(input())

for num in range(1, number + 1):

  sum_num = 0
  for index, digit in enumerate(str(num)):
    sum_num += int(digit)

  print(f"{num} -> {sum_num == 5 or sum_num == 7 or sum_num == 11}")
  
