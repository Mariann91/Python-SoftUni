collection_data = {}

interval = int(input())

for _ in range(interval):
  commands = input().split("|")
  command_word = commands[0]
  piece = commands[1]

  if command_word == "Add":
    composer = commands[2]
    key = commands[3]
      
    if not collection_data:
      print(True)
      collection_data = {
      piece: {composer: key,   
      }
    }
    
    else:
      if piece in collection_data:
        print(f"{piece} is already in the collection!")
      else:
        print(f"{piece} by {composer} in {key} added to the collection!")
  print(collection_data)
