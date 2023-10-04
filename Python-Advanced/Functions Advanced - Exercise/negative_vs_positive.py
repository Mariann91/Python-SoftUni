numbers = [int(num) for num in input().split()]

sum_positives = 0
sum_negatives = 0

for num in numbers:
  if num > 0:
    sum_positives += num
  else:
    sum_negatives += num 
    
print(sum_negatives)
print(sum_positives)

if sum_positives > abs(sum_negatives):
  print("The positives are stronger than the negatives")
else:
  print("The negatives are stronger than the positives")
