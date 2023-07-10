activation_key = input()

command = input()

while command != "Generate":
  command = command.split(">>>")
  command_word = command[0]

  if command_word == "Contains":
    substring = command[1]

    if substring in activation_key:
      print(f"{activation_key} contains {substring}")
    else:
      print("Substring not found!")

  elif command_word == "Flip":
    case = command[1]
    start_index = int(command[2])
    end_index = int(command[3])

    for i in range(start_index, end_index):
      if case == "Upper":
       activation_key = activation_key.replace(activation_key[i], activation_key[i].upper())
        
      elif case == "Lower":
        activation_key = activation_key.replace(activation_key[i], activation_key[i].lower())

    print(activation_key)

  elif command_word == "Slice":
    start_index = int(command[1])
    end_index = int(command[2])
    activation_key = [letter for letter in activation_key]

    for i in range(start_index, end_index):
      del activation_key[start_index]

    activation_key = "".join(activation_key)
    print(activation_key)
  
  command = input()

print(f"Your activation key is: {activation_key}")
