from collections import deque

monsters_armor =  deque([int(num) for num in input().split(",")])
soldier_striking_impact =  deque([int(num) for num in input().split(",")])
monsters_killed = 0

while monsters_armor and soldier_striking_impact:
  current_monster = monsters_armor.popleft()
  current_striking_impact = soldier_striking_impact.pop()
  
  if current_monster <= current_striking_impact:
    current_striking_impact -= current_monster
    monsters_killed += 1
    
      
    if soldier_striking_impact:
      soldier_striking_impact[-1] += current_striking_impact
    else:
        soldier_striking_impact.append(current_striking_impact) if current_striking_impact else None
  else:
    current_monster -= current_striking_impact
    monsters_armor.append(current_monster)
    
if not monsters_armor:
  print("All monsters have been killed!")
  
if not soldier_striking_impact:
  print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")
