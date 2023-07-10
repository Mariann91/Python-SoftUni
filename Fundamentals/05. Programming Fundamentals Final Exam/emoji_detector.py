import re

text = input()

digit_pattern = r"\d"
pattern = r"::[A-Z]+[a-z]+[a-z]+::|[(*)][(*)][A-Z]+[a-z]+[(*)][(*)]"

result = re.findall(pattern, text)
digits = re.findall(digit_pattern, text)

threshold = 1
for digit in digits:
  threshold *= int(digit)

print(f"Cool threshold: {threshold}")
print(f"{len(result)} emojis found in the text. The cool ones are:")


for emoji in result:
  ascii_sum = 0
  for char in emoji:
    ascii_sum += ord(char)

  if ascii_sum > threshold:
    print(emoji)
