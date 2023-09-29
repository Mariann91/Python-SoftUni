matrix_rows, matrix_cows = [int(num) for num in input().split(", ")]

col_sums = matrix_cows * [0]

for _ in range(matrix_rows):
    current_row = [int(num) for num in input().split()]

    for index in range(len(current_row)):
        col_sums[index] += current_row[index]

print(*col_sums, sep="\n")
