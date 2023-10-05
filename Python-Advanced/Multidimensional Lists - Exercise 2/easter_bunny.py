def calculate_up(matrix_row, matrix_col, matrix_size):
  current_row = matrix_row - 1
  up_score = 0
  up_cordinates = []
      
  while current_row in range(matrix_size):
    if matrix[current_row][matrix_col] == "X":
      break
        
    up_score += matrix[current_row][matrix_col]
    up_cordinates.append([current_row, matrix_col])
    current_row -=1
  return "up", up_score, up_cordinates

def calculate_down(matrix_row, matrix_col, matrix_size):
  current_row = matrix_row + 1
  down_score = 0
  down_cordinates = []
      
  while current_row in range(matrix_size):
    if matrix[current_row][matrix_col] == "X":
      break
        
    down_score += matrix[current_row][matrix_col]
    down_cordinates.append([current_row, matrix_col])
    current_row +=1
    
  return "down", down_score, down_cordinates

def calculate_right(matrix_row, matrix_col, matrix_size):
  current_col = matrix_col + 1
  right_score = 0
  right_cordinates = []
      
  while current_col in range(matrix_size):
    if matrix[matrix_row][current_col] == "X":
      break
        
    right_score += matrix[matrix_row][current_col]
    right_cordinates.append([matrix_row, current_col])
    current_col +=1
    
  return "right", right_score, right_cordinates

def calculate_left(matrix_row, matrix_col, matrix_size):
  current_col = matrix_col - 1
  left_score = 0
  left_cordinates = []
      
  while current_col in range(matrix_size):
    if matrix[matrix_row][current_col] == "X":
      break
        
    left_score += matrix[matrix_row][current_col]
    left_cordinates.append([matrix_row, current_col])
    current_col -=1
    
  return "left", left_score, left_cordinates

size = int(input())
matrix = [[int(el) if el.isdigit() else el for el in input().split()] for _ in range(size)]

max_score_info = ()

for row in range(size):
  for col in range(size):

    if matrix[row][col] == "B":
      
      up_info = calculate_up(matrix_row=row, matrix_col=col, matrix_size=size)
      down_info = calculate_down(matrix_row=row, matrix_col=col, matrix_size=size)
      right_info = calculate_right(matrix_row=row, matrix_col=col, matrix_size=size)
      left_info = calculate_left(matrix_row=row, matrix_col=col, matrix_size=size)

      summary = (up_info, down_info, left_info, right_info)
      max_score = 0
      for item in summary:
        if item[1] > max_score:
          max_score = item[1] 
          max_score_info = item

print(max_score_info[0])
print(*max_score_info[2], sep="\n")
print(max_score_info[1])
