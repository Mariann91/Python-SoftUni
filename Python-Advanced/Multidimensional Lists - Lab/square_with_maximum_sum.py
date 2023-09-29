matrix_rows, matrix_cols = [int(num) for num in input().split(", ")]

matrix = [[int(num) for num in input().split(", ")] for _ in range(matrix_rows)]

square_biggest_sum_numbers = [[], []]
square_biggest_sum = float("-inf")

for row in range(matrix_rows):

    for col in range(matrix_cols):

        if col + 1 < matrix_cols and row + 1 < matrix_rows:
            first_pair = [matrix[row][col], matrix[row][col + 1]]
            second_pair = [matrix[row + 1][col], matrix[row + 1][col + 1]]

            current_pairs_sum = sum(first_pair) + sum(second_pair)

            if current_pairs_sum > square_biggest_sum:
                square_biggest_sum = current_pairs_sum
                square_biggest_sum_numbers[0] = first_pair
                square_biggest_sum_numbers[1] = second_pair


for pair in square_biggest_sum_numbers:
    print(*pair, sep=" ")
    
print(square_biggest_sum)
