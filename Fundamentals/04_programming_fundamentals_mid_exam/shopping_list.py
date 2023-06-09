def does_it_exists(item, item_list):
  if item in item_list:
    return True
  return False

input_list = input().split("!")

command = input()

while command != "Go Shopping!":
  command = command.split()
  command_word = command[0]

  if command_word == "Urgent" and not does_it_exists(command[1], input_list):
    input_list.insert(0, command[1])

  elif command_word == "Unnecessary" and does_it_exists(command[1], input_list):
    input_list.remove(command[1])

  elif command_word == "Correct":
    old_item = command[1]
    new_item = command[2]
    if does_it_exists(old_item, input_list):
      old_item_index = input_list.index(old_item)
      input_list[old_item_index] = new_item

  elif command_word == "Rearrange" and does_it_exists(command[1], input_list):
    input_list.remove(command[1])
    input_list.append(command[1])
    
  command = input()

print(", ".join(input_list))
