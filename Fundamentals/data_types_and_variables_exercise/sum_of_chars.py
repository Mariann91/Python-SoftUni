interval = int(input())

sum_letters = 0
for _ in range(interval):
  sum_letters += ord(input())

print(f"The sum equals: {sum_letters}")
