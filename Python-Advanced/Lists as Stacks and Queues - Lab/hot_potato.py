from collections import deque

names = deque(input().split())
hot_potato_position = int(input()) - 1

while len(names) > 1:
  names.rotate(-hot_potato_position)
  
  print(f"Removed {names.popleft()}")

print(f"Last is {names.popleft()}")
