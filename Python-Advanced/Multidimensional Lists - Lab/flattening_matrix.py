matrix_rows = int(input())

matrix = []

for _ in range(matrix_rows):
    current_row = [int(num) for num in input().split(", ")]
    matrix.extend(current_row)

print(matrix)
