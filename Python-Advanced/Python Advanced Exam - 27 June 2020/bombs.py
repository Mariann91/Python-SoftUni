from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

datura_bombs, cherry_bombs, smoke_decoy_bombs = 0, 0, 0 
success = False

while bomb_effects and bomb_casings:

  if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
    success = True
    break
  
  bomb_effect = bomb_effects.popleft()
  bomb_casing = bomb_casings.pop()
  result = bomb_effect + bomb_casing

  if result == 40:
    datura_bombs += 1
  elif result == 60:
    cherry_bombs += 1
  elif result == 120:
    smoke_decoy_bombs += 1
  else:
    bomb_effects.appendleft(bomb_effect)
    bomb_casings.append(bomb_casing - 5)
    
if success:
  print("Bene! You have successfully filled the bomb pouch!")
else:
  print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
  print(f"Bomb Effects: {', '.join(str(el) for el in bomb_effects)}")
else:
  print("Bomb Effects: empty")

if bomb_casings:
  print(f"Bomb Casings: {', '.join(str(el) for el in bomb_casings)}")
else:
  print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")
