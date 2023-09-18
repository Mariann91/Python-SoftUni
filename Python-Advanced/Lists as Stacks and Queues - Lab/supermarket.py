from collections import deque

queue = deque()
command = input()

while command != "End":

  if command == "Paid":
    [print(queue.popleft()) for _ in range(len(queue))]
      
  else:
    name = command
    queue.append(name)

  command = input()

count = len(queue)

print(f"{count} people remaining.")
