strings = input().split()

result = ""
for string in strings:
  result += string * len(string)

print(result)
