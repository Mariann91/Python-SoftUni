letters = [letter for letter in input()]

letters_dic = {letter: letters.count(letter) for letter in letters if letter != " "}

for char, occurrences in letters_dic.items():
  print(f"{char} -> {occurrences}")
  
