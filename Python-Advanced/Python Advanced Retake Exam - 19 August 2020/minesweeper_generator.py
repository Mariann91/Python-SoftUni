size = int(input())
game_field = [[0 for _ in range(size)] for _ in range(size)]

directions = (
  (-1, 0), # up
  (0, 1), # right
  (1, 0), # down
  (0, -1), # left
  (-1, -1), # up-left
  (-1, 1), # up-right
  (1, -1), # down-left
  (1, 1) # down-right
)
  
for _ in range(int(input())):
  
  first, second = input().split(", ")
  first = first.replace("(", "")
  second = second.replace(")", "")

  game_field[int(first)][int(second)] = "*"


for row in range(size):
  for col in range(size):

    if game_field[row][col] == 0:

      for direction in directions:
        
        if (row + direction[0]) in range(size) and (col + direction[1]) in range(size):
          
          if game_field[row + direction[0]][col + direction[1]] == "*":
            game_field[row][col] += 1

[print(*row) for row in game_field]
