targets_info = {}

current_target = input()

while current_target != "Sail":
  line = current_target.split("||")
  city = line[0]
  population = int(line[1])
  gold = int(line[2])

  if city not in targets_info:
    targets_info[city] = [population, gold]
  else:
    targets_info[city][0] += population
    targets_info[city][1] += gold
  current_target = input()

action = input()

while action != "End":
  action_line = action.split("=>")
  action_word = action_line[0]
  town = action_line[1]

  if action_word == "Plunder":
    people = int(action_line[2])
    gold = int(action_line[3])

    targets_info[town][0] -= people
    targets_info[town][1] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    if targets_info[town][0] <= 0 or targets_info[town][1] <= 0:
      targets_info.pop(town)
      print(f"{town} has been wiped off the map!")
  
  elif action_word == "Prosper":
    gold = int(action_line[2])

    if gold > 0:
      targets_info[town][1] += gold
      print(f"{gold} gold added to the city treasury. {town} now has {targets_info[town][1]} gold.")
    else:
      print("Gold added cannot be a negative number!")
  
  action = input()

if len(targets_info) > 0:
  print(f"Ahoy, Captain! There are {len(targets_info)} wealthy settlements to go to:")
  for town in targets_info:
    print(f"{town} -> Population: {targets_info[town][0]} citizens, Gold: {targets_info[town][1]} kg")
else:
  print("Ahoy, Captain! All targets have been plundered and destroyed!")
