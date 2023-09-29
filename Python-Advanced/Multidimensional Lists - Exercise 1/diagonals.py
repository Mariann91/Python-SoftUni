square_matrix_rows = int(input())

primary_diagonal = []
secondary_diagonal = []

for row in range(square_matrix_rows):
    current_row = [int(num) for num in input().split(", ")]
    negative_index = -(row + 1)
    primary_diagonal.append(current_row[row])
    secondary_diagonal.append(current_row[negative_index])

print(f"Primary diagonal: {', '.join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
