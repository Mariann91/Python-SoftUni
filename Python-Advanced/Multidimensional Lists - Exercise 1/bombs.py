rows = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(rows)]

bombs_cordinates = [ [int(num) for num in item.split(",")] for item in input().split()]

directions = {
    "up": lambda x: [x[0] - 1, x[1]],
    "down": lambda x: [x[0] + 1, x[1]],
    "left": lambda x: [x[0], x[1] - 1],
    "right": lambda x: [x[0], x[1] + 1],
    "up_right": lambda x: [x[0] - 1, x[1] + 1],
    "up_left": lambda x: [x[0] - 1, x[1] - 1],
    "down_right": lambda x: [x[0] + 1, x[1] + 1],
    "down_left": lambda x: [x[0] + 1, x[1] - 1],
}

while bombs_cordinates:
    current_cordinate = bombs_cordinates.pop(0)
    
    if matrix[current_cordinate[0]][current_cordinate[1]] <= 0:
        continue
    
    value_to_subtract = matrix[current_cordinate[0]][current_cordinate[1]]
    matrix[current_cordinate[0]][current_cordinate[1]] = 0
    
    for direction in directions:
        position = directions[direction](current_cordinate)
        
        if position[0] not in range(rows) or position[1] not in range(rows):
            continue
            
        if matrix[position[0]][position[1]] > 0:
        
            matrix[position[0]][position[1]] -= value_to_subtract

sum_active_numbers = 0
active_numbers_count = 0

for row in matrix:
    
    for col in row:
        
        if col > 0:
            sum_active_numbers += col
            active_numbers_count += 1
            
print(f"Alive cells: {active_numbers_count}")  
print(f"Sum: {sum_active_numbers}")

[print(*row) for row in matrix]
