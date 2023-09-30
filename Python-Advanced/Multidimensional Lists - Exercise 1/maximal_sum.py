matrix_rows, matrix_cols = [int(num) for num in input().split()]

matrix = [[int(num) for num in input().split()] for _ in range(matrix_rows)]
biggest_3x3_sum = float("-inf")
biggest_3x3_numbers = [0] * 3

for row in range(matrix_rows):

    for col in range(matrix_cols):

        if col + 3 <= matrix_cols and row + 2 < matrix_rows:
            first_pair = matrix[row][col:col + 3]
            second_pair = matrix[row + 1][col:col + 3]
            third_pair = matrix[row + 2][col:col + 3]

            current_pairs_sum = sum(first_pair) + sum(second_pair) + sum(third_pair)

            if current_pairs_sum > biggest_3x3_sum:
                biggest_3x3_sum = current_pairs_sum
                biggest_3x3_numbers[0] = first_pair
                biggest_3x3_numbers[1] = second_pair
                biggest_3x3_numbers[2] = third_pair


print(f"Sum = {biggest_3x3_sum}")
print(*biggest_3x3_numbers[0])
print(*biggest_3x3_numbers[1])
print(*biggest_3x3_numbers[2])
