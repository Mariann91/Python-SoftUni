items = input().split(", ")

command = input()

while command != "Craft!":
  command = command.split(" - ")
  command_word = command[0]
  command_item = command[1]

  if command_word == "Collect" and command_item not in items:
    items.append(command_item)

  elif command_word == "Drop" and command_item in items:
    items.remove(command_item)

  elif command_word == "Combine Items":
    command_item = command_item.split(":")
    old_item = command_item[0]
    new_item = command_item[1]
    if old_item in items:
      old_item_index = items.index(old_item)
      items.insert(old_item_index + 1, new_item)
  elif command_word == "Renew" and command_item in items:
    items.remove(command_item)
    items.append(command_item)

  command = input()

print(", ".join(items))
