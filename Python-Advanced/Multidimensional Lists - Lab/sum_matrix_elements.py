matrix = []
sum_matrix = 0

matrix_rows, matrix_cols = [int(num) for num in input().split(", ")]

for matrix_row in range(matrix_rows):
    matrix.append([])
    current_row = [int(num) for num in input().split(", ")]
    sum_matrix += sum(current_row)
    matrix[matrix_row] = current_row

print(sum_matrix)
print(matrix)
