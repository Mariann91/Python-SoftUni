rows, cols = [int(num) for num in input().split()]
matrix = []
player_cordinates = []
bunnies_cordinates = []

directions = {
    "L": lambda x: [x[0], x[1] - 1],
    "R": lambda x: [x[0], x[1] + 1],
    "U": lambda x: [x[0] - 1, x[1]],
    "D": lambda x: [x[0] + 1, x[1]],
}

for row in range(rows):
    matrix.append(list(input()))
    
    for col in range(cols):
        
        if matrix[row][col] == "P":
            player_cordinates.extend([row, col])
            matrix[row][col] = "."
            
        elif matrix[row][col] == "B":
            bunnies_cordinates.append([row, col])
            
for command in list(input()):
    
    current_cordinates = directions[command](player_cordinates)
    current_row = current_cordinates[0]
    current_col = current_cordinates[1]
    
    new_bunny_cordinates = []
    
    for bunny_cordinates in bunnies_cordinates:
        
        for direction in directions:
            
            moved_bunny_cordinates = directions[direction](bunny_cordinates)
            
            if moved_bunny_cordinates[0] not in range(rows) or \
            moved_bunny_cordinates[1] not in range(cols):
                continue
        
            matrix[moved_bunny_cordinates[0]][moved_bunny_cordinates[1]] = "B"
            new_bunny_cordinates.append(moved_bunny_cordinates)
          
    bunnies_cordinates.extend(new_bunny_cordinates)
    
    if current_row not in range(rows) or current_col not in range(cols):
        [print("".join(row)) for row in matrix]	
        print(f"won: {player_cordinates[0]} {player_cordinates[1]}")
        break

    if matrix[current_row][current_col] == "B":
        [print("".join(row)) for row in matrix]	
        print(f"dead: {current_row} {current_col}")
        
        break

    player_cordinates = current_cordinates
 
