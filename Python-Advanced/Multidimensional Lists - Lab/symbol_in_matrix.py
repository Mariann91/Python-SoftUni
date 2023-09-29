matrix_rows = int(input())

matrix = []

for _ in range(matrix_rows):
    current_row = list(input())
    matrix.append(current_row)

symbol_to_find = input()

for row in range(len(matrix)):
    if symbol_to_find in matrix[row]:
        col = matrix[row].index(symbol_to_find)
        print((row, col))
        break
else:
    print(f"{symbol_to_find} does not occur in the matrix")
