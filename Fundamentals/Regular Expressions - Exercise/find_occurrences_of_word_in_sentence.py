import re 

text = input().lower()
word_to_count = input().lower()

result = re.findall(rf"\b{word_to_count}\b", text)
print(len(result))
