cupboard_rows, cupboard_cols = [int(num) for num in input().split(",")]

cupboard_area = [[el for el in list(input())] for _ in range(cupboard_rows)]
cheeses_count = sum([row.count("C") for row in cupboard_area])

for_loops_break = False

for row in range(cupboard_rows):
  for col in range(cupboard_cols):

    if cupboard_area[row][col] == "M":
      mouse_row = row
      mouse_col = col

      cupboard_area[mouse_row][mouse_col] = "*"
      
      directions = {
        "up": lambda x: x - 1,
        "down": lambda x: x + 1,
        "left": lambda x: x - 1,
        "right": lambda x: x + 1,
      }

      reverse_directions = {
        "up": lambda x: x + 1,
        "down": lambda x: x - 1,
        "left": lambda x: x + 1,
        "right": lambda x: x - 1,
      }

      while True:
        
        command = input()

        if command == "danger":
          print("Mouse will come back later!")
          cupboard_area[mouse_row][mouse_col] = "M"
          for_loops_break = True
          break
        
        if command == "up" or command == "down":
          mouse_row = directions[command](mouse_row)
          
          if mouse_row not in range(cupboard_rows):
            mouse_row = reverse_directions[command](mouse_row)
            cupboard_area[mouse_row][mouse_col] = "M"
            print("No more cheese for tonight!")
            for_loops_break = True
            break

          if cupboard_area[mouse_row][mouse_col] == "@":
            mouse_row = reverse_directions[command](mouse_row)
            continue
            
          elif cupboard_area[mouse_row][mouse_col] == "T":
            print("Mouse is trapped!")
            cupboard_area[mouse_row][mouse_col] = "M"
            for_loops_break = True
            break
            
          elif cupboard_area[mouse_row][mouse_col] == "C":
            cupboard_area[mouse_row][mouse_col] = "*"
            cheeses_count -= 1

            if cheeses_count == 0:
              cupboard_area[mouse_row][mouse_col] = "M"
              print("Happy mouse! All the cheese is eaten, good night!")
              for_loops_break = True
              break
          
        elif command == "left" or command == "right":
          mouse_col = directions[command](mouse_col)

          if mouse_col not in range(cupboard_cols):
             mouse_col = reverse_directions[command](mouse_col)
             cupboard_area[mouse_row][mouse_col] = "M"
             print("No more cheese for tonight!")
             for_loops_break = True
             break

          if cupboard_area[mouse_row][mouse_col] == "@":
            mouse_col = reverse_directions[command](mouse_col)
            continue
            
          elif cupboard_area[mouse_row][mouse_col] == "T":
            print("Mouse is trapped!")
            cupboard_area[mouse_row][mouse_col] = "M"
            for_loops_break = True
            break

          elif cupboard_area[mouse_row][mouse_col] == "C":
            cupboard_area[mouse_row][mouse_col] = "*"
            cheeses_count -= 1

            if cheeses_count == 0:
              cupboard_area[mouse_row][mouse_col] = "M"
              print("Happy mouse! All the cheese is eaten, good night!")
              for_loops_break = True
              break
          
    if for_loops_break:
      break
  if for_loops_break:
    break
[print(*row, sep="") for row in cupboard_area]
