matrix_rows = int(input())
matrix = [[int(num) for num in input().split()]for _ in range(matrix_rows)]

valid_range = range(0, matrix_rows)

while True:
    line = input()

    if line == "END":
        [print(*row) for row in matrix]
        break

    command, row, col, value = [int(part) if part.isdigit() else part for part in line.split()]

    if row not in valid_range or col not in valid_range:
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value
      
