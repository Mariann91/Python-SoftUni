n = int(input())

matrix = []

def return_line(char, length):
    line = []
    
    for i in range(length):
        
        if i == 0:
        
            line.append(f"{char}")
        elif i == length - 1:
            line.append(f"{char}")
        else:
            line.append(f"-")
    
    return line

for i in range(n):
    start_end_char = "|"
    
    if i == 0 or i == n - 1:
        start_end_char = "+"
    
    matrix.append(return_line(start_end_char, n))

[print(" ".join(row)) for row in matrix]
