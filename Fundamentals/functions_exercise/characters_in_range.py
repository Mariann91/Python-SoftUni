def find_ascii(start, end):
    result = []
    for ascii_value in range(start + 1, end):
        result.append(chr(ascii_value))
    return " ".join(result)


start_char, end_char = ord(input()), ord(input())
print(find_ascii(start_char, end_char))
