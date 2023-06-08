rooms = input().split("|")
MAX_HEALTH = 100

health = 100
bitcoins = 0
room_number = 0

for room in rooms:
  
  room_number += 1
  room = room.split()
  command = room[0]
  number = int(room[1])

  if command == "potion":
    
    if health + number <= MAX_HEALTH:
      health += number
    else:
      number = MAX_HEALTH - health
      health += number
    print(f"You healed for {number} hp.")
    print(f"Current health: {health} hp.")

  elif command == "chest":
    bitcoins += number
    print(f"You found {number} bitcoins.")

  else:
    health -= number
    if health > 0:
      print(f"You slayed {command}.")
    else:
      print(f"You died! Killed by {command}.")
      print(f"Best room: {room_number}")
      break
else:
  print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
