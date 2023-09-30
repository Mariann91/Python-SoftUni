matrix_rows, matrix_cols = [int(num) for num in input().split()]

matrix = []
start_range = ord("a")
end_range = start_range + matrix_rows

for row in range(start_range, end_range):
    current_row = []
  
    for col in range(matrix_cols):
        current_row.append(f"{chr(row)}{chr(row + col)}{chr(row)}")
      
    matrix.append(current_row)

[print(*row) for row in matrix]
