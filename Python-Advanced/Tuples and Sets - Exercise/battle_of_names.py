odd_set = set()
even_set = set()

n = int(input())

for round in range(1, n + 1):
  name = input()

  name_score = sum([ord(char) for char in name]) // round

  if name_score % 2 == 0:
    even_set.add(name_score)
  else:
    odd_set.add(name_score)

if sum(even_set) == sum(odd_set):
  union = even_set | odd_set
  print(*union, sep=", ")
elif sum(even_set) < sum(odd_set):
  print(*odd_set, sep=", ")
else:
  print(*odd_set.symmetric_difference(even_set), sep=", ")
  
