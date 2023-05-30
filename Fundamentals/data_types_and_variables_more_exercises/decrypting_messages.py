key_value = int(input())
interval = int(input())

output = ""
for _ in range(interval):
    char = input()

    output += chr(ord(char) + key_value)
print(output)
