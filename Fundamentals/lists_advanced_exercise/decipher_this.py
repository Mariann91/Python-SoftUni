secret_message = input().split()
deciphered_words = []

for word in secret_message:

    word_list = [char for char in word]

    first_char = [char for char in word_list if char.isdigit()]
    first_char = int("".join(first_char))
    rest_chars = [char for char in word_list if char.isalpha()]
    rest_chars[0], rest_chars[-1] = rest_chars[-1], rest_chars[0]
    rest_chars.insert(0, chr(first_char))
    deciphered_words.append(rest_chars)

for word in deciphered_words:
    print("".join(word), end=" ")
