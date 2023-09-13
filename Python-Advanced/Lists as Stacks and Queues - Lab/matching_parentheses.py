string = input()

stack = []

for index in range(len(string)):
  current_char = string[index]

  if current_char == "(":
    stack.append(index)
    
  elif current_char == ")":
    
    start_index = stack.pop()
    segment_to_print = string[start_index : index + 1]
    
    print(segment_to_print)
    
