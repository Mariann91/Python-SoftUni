from collections import deque

matrix_rows, matrix_cols = [int(num) for num in input().split()]

matrix = [["" for _ in range(matrix_cols)] for _ in range(matrix_rows)]

snake = deque(input())
snake_copy = snake.copy()

for row in range(matrix_rows):

    for col in range(matrix_cols):

        if not snake_copy:
            snake_copy = snake.copy()

        if row % 2 == 0:
            matrix[row][col] = snake_copy.popleft()
        else:
            matrix[row][-(col + 1)] = snake_copy.popleft()

[print(''.join(row)) for row in matrix]
