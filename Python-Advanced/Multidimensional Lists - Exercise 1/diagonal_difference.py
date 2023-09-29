matrix_rows = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(matrix_rows)]
primary = [matrix[i][i] for i in range(matrix_rows)]
secondary = [matrix[i][-(i + 1)] for i in range(matrix_rows)]

print(abs(sum(primary) - sum(secondary)))
