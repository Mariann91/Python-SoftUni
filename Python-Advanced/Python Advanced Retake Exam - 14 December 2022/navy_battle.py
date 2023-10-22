field_size = int(input())

field = []
submarine_row = 0
submarine_col = 0
lives = 3
cruisers = 3

directions = {
    "up": lambda x, y: [x - 1, y],
    "down": lambda x, y: [x + 1, y],
    "left": lambda x, y: [x, y - 1],
    "right": lambda x, y: [x, y + 1],
}

for row in range(field_size):
    field.append([el for el in list(input())])
  
    for col in range(field_size):
        if field[row][col] == "S":
            submarine_row, submarine_col = row, col
            field[submarine_row][submarine_col] = "-"

while True:
    command = input()

    submarine_row, submarine_col = directions[command](submarine_row, submarine_col)

    if field[submarine_row][submarine_col] == "*":
        lives -= 1

        if lives == 0:
            field[submarine_row][submarine_col] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_row}, {submarine_col}]!")
            break

    elif field[submarine_row][submarine_col] == "C":
        cruisers -= 1

        if cruisers == 0:
            field[submarine_row][submarine_col] = "S"
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    field[submarine_row][submarine_col] = "-"

[print(*row, sep="") for row in field]
