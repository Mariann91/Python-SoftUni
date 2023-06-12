MAX_HEALTH = 100

rooms = input().split("|")

health, bitcoins = 100, 0
room_count = 0
for room in rooms:
  room_count += 1
  room = room.split()

  command_word = room[0]
  value = int(room[1])

  if command_word == "potion":
    if health + value > 100:
      value = MAX_HEALTH - health

    health += value
    print(f"You healed for {value} hp.")
    print(f"Current health: {health} hp.")

  elif command_word == "chest":
    bitcoins += value
    print(f"You found {value} bitcoins.")

  else:
    health -= value
    if health <= 0:
      print(f"You died! Killed by {command_word}." )
      print(f"Best room: {room_count}")
      break
    else:
      print(f"You slayed {command_word}.")
else:
  print("You've made it!")
  print(f"Bitcoins: {bitcoins}")
  print(f"Health: {health}")
