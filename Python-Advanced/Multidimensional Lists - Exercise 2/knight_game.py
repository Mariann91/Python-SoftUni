size = int(input())  # matrix square size
matrix = [[square for square in list(input())] for _ in range(size)]  # creating matrix

# knights possible moves
positions = (
    (-2, -1),  # up 2 left 1
    (-2, 1),  # up 2 right 1
    (-1, -2),  # up 1 left 2
    (-1, 2),  # up 1 right 2
    (2, 1),  # down 2 right 1
    (2, -1),  # down 2 left 1
    (1, -2),  # down 1 left 2
    (1, 2),  # down 1 right 2
)

removed_knights = 0
valid_range = range(0, size)

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for position in positions:
                    position_row = row + position[0]
                    position_col = col + position[1]

                    if position_row in valid_range and position_col in valid_range and \
                            matrix[position_row][position_col] == "K":
                        attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks_pos = [row, col]

    if knight_with_most_attacks_pos:
        matrix[knight_with_most_attacks_pos[0]][knight_with_most_attacks_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
