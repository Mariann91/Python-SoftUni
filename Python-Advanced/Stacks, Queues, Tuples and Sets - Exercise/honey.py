from collections import deque

bees = deque([str(el) if not el.isdigit() and len(el) == 1 else int(el) for el in input().split()])
nectars = deque([str(el) if not el.isdigit() and len(el) == 1 else int(el) for el in input().split()])
symbols = deque([el for el in input().split()])

total_honey = 0

while bees and nectars:

  if bees[0] <= nectars[-1]:
    bee = bees.popleft()
    symbol = symbols.popleft()
    nectar = nectars.pop()

    if symbol == "/" and nectar == 0:
      continue
    
    gained_honey = eval(f"{bee}{symbol}{nectar}")
    total_honey += abs(gained_honey)
  else:
    nectars.pop()

print(f"Total honey made: {total_honey}")

if bees:
  print(f"Bees left: {', '.join([str(el) for el in bees])}")

if nectars:
  print(f"Necatar left: {', '.join([str(el) for el in nectars])}")
