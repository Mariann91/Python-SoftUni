matrix_rows, matrix_cols = [int(num) for num in input().split()]

matrix = [[x for x in input().split()] for _ in range(matrix_rows)]

while True:
    line = input()

    if line == "END":
        break

    command_line = line.split()

    if "swap" not in command_line:
        print("Invalid input!")
        continue

    if len(command_line) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(index) for index in command_line[1::]]

    if row1 < 0 or row1 > matrix_rows or row2 < 0 or row2 > matrix_rows:
        print("Invalid input!")
        continue

    if col1 < 0 or col1 > matrix_cols or col2 < 0 or col2 > matrix_cols:
        print("Invalid input!")
        continue

    save_value = matrix[row1][col1]
    matrix[row1][col1] = matrix[row2][col2]
    matrix[row2][col2] = save_value

    [print(*row) for row in matrix]
