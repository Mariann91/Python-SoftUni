interval = int(input())

max_score = float("-inf")
for _ in range(interval):
  weight = int(input())
  time_needed = int(input())
  quality = int(input())

  score = (weight / time_needed) ** quality
  if score > max_score:
    max_score = score
    result = f"{weight} : {time_needed} = {int(max_score)} ({quality})"

print(result)
