interval = int(input())

name = ""
age = ""
for _ in range(interval):

  current_sequence = input().split()
  for word in current_sequence:

    if "@" in word and "|" in word:
      start_index = word.index("@")
      end_index = word.index("|")
      name = word[start_index + 1:end_index]

    elif "#" in word and "*" in word:
      start_index = word.index("#")
      end_index = word.index("*")
      age = word[start_index + 1:end_index]
  
  print(f"{name} is {age} years old.")
  
