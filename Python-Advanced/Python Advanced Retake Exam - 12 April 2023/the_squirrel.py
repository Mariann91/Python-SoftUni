field_size = int(input())
commands = input().split(", ")

field = []
hazelnuts_count = 0
squirrel_row = 0
squirrel_col = 0

valid_range = range(field_size)

directions = {
    "up": lambda x, y: [x - 1, y],
    "down": lambda x, y: [x + 1, y],
    "left": lambda x, y: [x, y - 1],
    "right": lambda x, y: [x, y + 1],
}

for row in range(field_size):
    field.append([el for el in list(input())])

    for col in range(field_size):
        if field[row][col] == "s":
            squirrel_row = row
            squirrel_col = col

for command in commands:
    squirrel_row, squirrel_col = directions[command](squirrel_row, squirrel_col)

    if squirrel_row in valid_range and squirrel_col in valid_range:

        if field[squirrel_row][squirrel_col] == "h":
            hazelnuts_count += 1
            field[squirrel_row][squirrel_col] = "*"

            if hazelnuts_count == 3:
                print("Good job! You have collected all hazelnuts!")
                break

        elif field[squirrel_row][squirrel_col] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break
    else:
        print("The squirrel is out of the field.")
        break
else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_count}")
