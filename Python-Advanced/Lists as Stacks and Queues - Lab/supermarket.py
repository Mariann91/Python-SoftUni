from collections import deque

command = input()

queue = deque()

while command != "End":
  
  if command == "Paid":
    for _ in range(len(queue)):
      print(queue.popleft())
  else:
    name = command
    queue.append(name)

  command = input()

count = len(list(queue))

print(f"{count} people remaining.")
