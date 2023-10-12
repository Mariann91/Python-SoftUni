neighbourhood_rows, neighbourhood_cols = [int(num) for num in input().split()]

neighbourhood = [[el for el in list(input())] for _ in range(neighbourhood_rows)]

moves = {
    "up": lambda x: x - 1,
    "down": lambda x: x + 1,
    "left": lambda x: x - 1,
    "right": lambda x: x + 1,
}

for_loops_break = False

for row in range(neighbourhood_rows):
    for col in range(neighbourhood_cols):

        if neighbourhood[row][col] == "B":
            delivery_boy_row = row
            delivery_boy_col = col

            while True:
                command = input()

                if command == "up" or command == "down":

                    if moves[command](delivery_boy_row) in range(neighbourhood_rows):
                        if neighbourhood[moves[command](delivery_boy_row)][delivery_boy_col] == "*":
                            continue

                        delivery_boy_row = moves[command](delivery_boy_row)

                        if neighbourhood[delivery_boy_row][delivery_boy_col] == "P":
                            neighbourhood[delivery_boy_row][delivery_boy_col] = "R"
                            print("Pizza is collected. 10 minutes for delivery.")

                        elif neighbourhood[delivery_boy_row][delivery_boy_col] == "A":
                            neighbourhood[delivery_boy_row][delivery_boy_col] = "P"
                            print("Pizza is delivered on time! Next order...")
                            for_loops_break = True
                            break

                        elif neighbourhood[delivery_boy_row][delivery_boy_col] != "B":
                            neighbourhood[delivery_boy_row][delivery_boy_col] = "."
                    else:
                        neighbourhood[row][col] = " "
                        print("The delivery is late. Order is canceled.")
                        for_loops_break = True
                        break

                if command == "left" or command == "right":

                    if moves[command](delivery_boy_col) in range(neighbourhood_cols):
                        if neighbourhood[delivery_boy_row][moves[command](delivery_boy_col)] == "*":
                            continue

                        delivery_boy_col = moves[command](delivery_boy_col)

                        if neighbourhood[delivery_boy_row][delivery_boy_col] == "P":
                            neighbourhood[delivery_boy_row][delivery_boy_col] = "R"
                            print("Pizza is collected. 10 minutes for delivery.")

                        elif neighbourhood[delivery_boy_row][delivery_boy_col] == "A":
                            neighbourhood[delivery_boy_row][delivery_boy_col] = "P"
                            print("Pizza is delivered on time! Next order...")
                            for_loops_break = True
                            break

                        elif neighbourhood[delivery_boy_row][delivery_boy_col] != "B":
                            neighbourhood[delivery_boy_row][delivery_boy_col] = "."
                    else:
                        neighbourhood[row][col] = " "
                        print("The delivery is late. Order is canceled.")
                        for_loops_break = True
                        break
                      
        if for_loops_break:
            break
    if for_loops_break:
        break

[print(*row, sep="") for row in neighbourhood]
