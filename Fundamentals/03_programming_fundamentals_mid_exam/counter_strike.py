energy = int(input())

distance = input()

won_batttles = 0
while distance != "End of battle":
  distance = int(distance)

  if distance <= energy:
    energy -= distance
    won_batttles += 1
    if won_batttles % 3 == 0:
      energy += won_batttles
  else:
    print(f"Not enough energy! Game ends with {won_batttles} won battles and {energy} energy")
    break

  distance = input()
  
else:
  print(f"Won battles: {won_batttles}. Energy left: {energy}" )
    
