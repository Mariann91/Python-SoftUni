energy = int(input())

won_battles = 0
while True:
  
  needed_energy = input()
  if needed_energy == "End of battle":
    print(f"Won battles: {won_battles}. Energy left: {energy}" )
    break
    
  needed_energy = int(needed_energy)

  if needed_energy <= energy:
    won_battles += 1
    energy -= needed_energy
    if won_battles % 3 == 0:
      energy += won_battles
  else:
    print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
    break
    
