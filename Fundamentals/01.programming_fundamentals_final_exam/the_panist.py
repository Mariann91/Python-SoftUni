collection_data = {}

interval = int(input())

for _ in range(interval):
  piece, composer, key = input().split("|")
  
  if not collection_data:
    collection_data = {
      piece : {
        composer : key
      }
    }

  else:
    current_information = {
      piece : {
        composer : key
      }
    }

    collection_data.update(current_information)

commands = input()

while commands != "Stop":
  commands = commands.split("|")
  command_word = commands[0]
  command_piece = commands[1]

  if command_word == "Add":
    command_composer = commands[2]
    command_key = commands[3]
    
    if command_piece in collection_data:
      print(f"{command_piece} is already in the collection!")
    else:
      added_info = {
        command_piece: {
          command_composer: command_key,
        }
      }
      collection_data.update(added_info)
      print(f"{command_piece} by {command_composer} in {command_key} added to the collection!")

  elif command_word == "Remove":

    if command_piece in collection_data:   
      collection_data.pop(command_piece)
      print(f"Successfully removed {command_piece}!")
    else:
      print(f"Invalid operation! {command_piece} does not exist in the collection.")

  elif command_word == "ChangeKey":
    command_new_key = commands[2]
    old_key = ''.join([value for value in collection_data[command_piece].values()])

    if command_piece in collection_data:
      for key, value in collection_data[command_piece].items():
        if collection_data[command_piece][key] == old_key:
          collection_data[command_piece][key] = command_new_key
          break
      print(f"Changed the key of {command_piece} to {command_new_key}!")
    else:
      print(f"Invalid operation! {command_piece} does not exist in the collection.")
