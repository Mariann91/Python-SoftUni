vowels_to_remove = [ 'a', 'o', 'u', 'e', 'i']
print("".join([letter for letter in input() if letter not in vowels_to_remove]))
