inventory = input().split("|")

command = input()

while command != "Yohoho!":
  command = command.split()
  command_word = command[0]

  if command_word == "Loot":
    for i in range(1, len(command)):
      
      if command[i] not in inventory:
        inventory.insert(0, command[i])
        
  elif command_word == "Drop":
    drop_index = int(command[1])
    if 0 <= drop_index < len(inventory):
      inventory.append(inventory.pop(drop_index))

  elif command_word == "Steal":
    items_to_steal = int(command[1])

    stollen_items = []
    for i in range(items_to_steal):
      if len(inventory) == 0:
        break 
      stollen_items.insert(0, inventory.pop(-1))

    print(", ".join(stollen_items))
        
  command = input()
  
if len(inventory) > 0:
  sum_len = 0
  for item in inventory:
    sum_len += len(item)
  average = sum_len / len(inventory)
  print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
  print("Failed treasure hunt.")
