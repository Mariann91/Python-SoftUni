def find_burrow_positions(input_field_size, input_field):

    burrow_loops_break = False
    burrow_positions = []

    for field_row in range(input_field_size):

        for field_col in range(input_field_size):

            if input_field[field_row][field_col] == "B":
                burrow_positions.append([field_row, field_col])

                if len(burrow_positions) == 2:
                    burrow_loops_break = True
                    break

        if burrow_loops_break:
            break

    return burrow_positions


def find_snake_out_burrow_position(positions, snake_row, snake_col):

    for pos in positions:

        if pos == [snake_row, snake_col]:
            positions.remove([snake_row, snake_col])
            break

    return positions[0]


def move_snake(input_command, snake_row, snake_col):

    move = {
        "up": lambda x: x - 1,
        "down": lambda x: x + 1,
        "right": lambda x: x + 1,
        "left": lambda x: x - 1,
    }

    if input_command == "up" or input_command == "down":
        snake_row = move[input_command](snake_row)
    else:
        snake_col = move[input_command](snake_col)

    return snake_row, snake_col


game_over = False
food_counter = 0

field_size = int(input())
field = [[el for el in list(input())] for _ in range(field_size)]

for row in range(field_size):

    for col in range(field_size):

        if field[row][col] == "S":
            field[row][col] = "."
            current_snake_row = row
            current_snake_col = col

            while food_counter < 10:
                command = input()

                current_snake_row, current_snake_col = move_snake(command, current_snake_row, current_snake_col)

                if current_snake_row in range(field_size) and current_snake_col in range(field_size):

                    if field[current_snake_row][current_snake_col] == "B":

                        field[current_snake_row][current_snake_col] = "."
                        field_burrow_positions = find_burrow_positions(input_field=field, input_field_size=field_size)

                        current_snake_row, current_snake_col = find_snake_out_burrow_position\
                            (positions=field_burrow_positions, snake_row=current_snake_row, snake_col=current_snake_col)

                    elif field[current_snake_row][current_snake_col] == "*":
                        food_counter += 1

                    field[current_snake_row][current_snake_col] = "."

                else:
                    game_over = True

                    print("Game over!")
                    print(f"Food eaten: {food_counter}")
                    break

            else:
                field[current_snake_row][current_snake_col] = "S"
                game_over = True

                print("You won! You fed the snake.")
                print(f"Food eaten: {food_counter}")
                break

        if game_over:
            break

    if game_over:
        break

[print(*row, sep="") for row in field]
