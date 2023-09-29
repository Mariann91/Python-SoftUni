matrix_rows = int(input())

primary_diagonal_sum = 0

for matrix_row in range(matrix_rows):
    current_row = [int(num) for num in input().split()]
    primary_diagonal_sum += current_row[matrix_row]

print(primary_diagonal_sum)
