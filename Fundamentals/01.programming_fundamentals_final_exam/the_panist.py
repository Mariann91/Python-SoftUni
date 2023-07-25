pieces_info = {}

interval = int(input())

for _ in range(interval):
  piece, composer, key = input().split("|")

  pieces_info[piece] = [composer, key]

while True:
  command_line = input()

  if command_line == "Stop":
    break

  line = command_line.split("|")
  command = line[0]
  
  if command == "Add":
    piece = line[1]
    composer = line[2]
    key = line[3]

    if piece not in pieces_info:
      pieces_info[piece] = [composer, key]
      print(f"{piece} by {composer} in {key} added to the collection!")
    else:
      print(f"{piece} is already in the collection!")
  elif command == "Remove":
    piece = line[1]
    if piece in pieces_info:
      pieces_info.pop(piece)
      print(f"Successfully removed {piece}!")
    else:
      print(f"Invalid operation! {piece} does not exist in the collection.")

  elif command == "ChangeKey":
    piece = line[1]
    new_key = line[2]

    if piece in pieces_info:
      pieces_info[piece][1] = new_key
      print(f"Changed the key of {piece} to {new_key}!")
    else:
      print(f"Invalid operation! {piece} does not exist in the collection.")

for item, values in pieces_info.items():
  print(f"{item} -> Composer: {values[0]}, Key: {values[1]}")
