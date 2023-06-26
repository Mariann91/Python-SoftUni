string = input()

letters = ""
digits = ""
special_chars = ""

for char in string:
  if char.isalpha():
    letters += char
  elif char.isdigit():
    digits += char
  else:
    special_chars += char

print(digits)
print(letters)
print(special_chars)
