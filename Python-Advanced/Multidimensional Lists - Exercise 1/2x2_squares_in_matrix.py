matrix_rows, matrix_cols = [int(num) for num in input().split()]

matrix = [input().split() for _ in range(matrix_rows)]
equal_cells = 0

for row in range(matrix_rows):

    for col in range(matrix_cols):

        if col + 1 < matrix_cols and row + 1 < matrix_rows:
            first = matrix[row][col]
            second = matrix[row][col + 1]
            third = matrix[row + 1][col]
            fourth = matrix[row + 1][col + 1]

            if first == second and second == third and third == fourth:
                equal_cells += 1

print(equal_cells)
