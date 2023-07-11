import re
line = input()
regex = r'\+359(\s|-)2\1\d{3}\1\d{4}\b'
text = re.finditer(regex, line)
matches = []

for i in text:
    matches.append(i.group())
    
print(', '.join(matches))
