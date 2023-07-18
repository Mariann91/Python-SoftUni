import re

text = input()

pattern = r"\b_([A-Za-z\d]+)\b"
result = re.findall(pattern, text)

print(','.join(result))
