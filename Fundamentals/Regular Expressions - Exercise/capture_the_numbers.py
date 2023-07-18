import re

matches = []
while True:
    text = input()

    if not text:
        break

    pattern = r"\d+"

    result = re.findall(pattern, text)
    matches.extend(result)

print(' '.join(matches))
