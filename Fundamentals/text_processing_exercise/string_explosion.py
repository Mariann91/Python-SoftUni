sequence = input()

chars_to_delete = 0
new_string = ""

for i in range(len(sequence)):
  
  if sequence[i] == ">":
    
    chars_to_delete += int(sequence[i + 1])
    new_string += sequence[i]
    
  elif chars_to_delete > 0:
    chars_to_delete -= 1
    
  else:
    new_string += sequence[i]
    
print(new_string)
