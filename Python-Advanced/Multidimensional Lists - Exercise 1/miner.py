matrix_size = int(input())
commands = input().split()
matrix = []
miner_cordinates = []
coal_cordinates = []

directions = {
    "right": lambda x: [x[0], x[1] + 1],
    "left": lambda x: [x[0], x[1] - 1],
    "up": lambda x: [x[0] - 1, x[1]],
    "down": lambda x: [x[0] + 1, x[1]],
}


for row in range(matrix_size):
    matrix.append(input().split())
    
    for col in range(matrix_size):
        
        if matrix[row][col] == "s":
            miner_cordinates.extend([row, col])
        elif matrix[row][col] == "c":
            coal_cordinates.append([row, col])

for command in commands:
    
    current_cordinate = directions[command](miner_cordinates)
    matrix_row = current_cordinate[0]
    matrix_col = current_cordinate[1]
    
    if matrix_row not in range(matrix_size) or matrix_col not in range(matrix_size):
        continue
    
    miner_cordinates = current_cordinate
    
    if matrix[matrix_row][matrix_col] == "e":
        print(f"Game over! ({matrix_row}, {matrix_col})")
        
        break
    
    if matrix[matrix_row][matrix_col] == "c":
        matrix[matrix_row][matrix_col] = "*"
        coal_cordinates.remove([matrix_row, matrix_col])
        
        if not coal_cordinates:
            print(f"You collected all coal! ({matrix_row}, {matrix_col})")
            break
    miner_cordinates = current_cordinate
else:
    print(f"{len(coal_cordinates)} pieces of coal left. ({matrix_row}, {matrix_col})")
