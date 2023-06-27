message = input()
encrypted_word = ""

for char in message:
  encrypted_word += chr(ord(char) + 3)

print(encrypted_word)
                         
