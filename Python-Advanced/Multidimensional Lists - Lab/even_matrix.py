matrix_rows = int(input())

matrix = [[int(num) for num in input().split(", ") if int(num) % 2 == 0] for _ in range(matrix_rows)]

# non comprehension solution
# for _ in range(matrix_rows):
#     current_row = [int(num) for num in input().split(", ") if int(num) % 2 == 0]
#     matrix.append(current_row)

print(matrix)
