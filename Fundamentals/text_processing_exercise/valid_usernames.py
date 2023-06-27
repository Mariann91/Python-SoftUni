names = input().split(", ")

valid_words = []

for name in names:
  word = ""
  
  if 3 <= len(name) <= 16:
    
    for letter in name:
      
      if letter.isalnum() or letter == "_" or letter == "-":
        word += letter
      else:
        break
        
    else:
      valid_words.append(word)
      
print(*valid_words, sep="\n")
