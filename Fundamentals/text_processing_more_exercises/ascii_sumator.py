start = ord(input())
end = ord(input())
string = input()

result = 0
for char in string:
  if start < ord(char) < end:
    result += ord(char)

print(result)
