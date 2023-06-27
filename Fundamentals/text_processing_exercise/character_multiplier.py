def calculate_difference(word_difference, word):
  left_sum = 0
  for i in range(1, word_difference + 1):
    left_sum += ord(word[-i])

  return left_sum
    
words = input().split()

first_word = words[0]
second_word = words[1]
min_len = min(len(first_word), len(second_word))

result = 0
for index in range(min_len):
  result += ord(first_word[index]) * ord(second_word[index])

difference = 0
if len(first_word) > len(second_word):
  difference = len(first_word) - len(second_word)
  result += calculate_difference(difference, first_word)

elif len(first_word) < len(second_word):
  difference = len(second_word) - len(first_word)
  result += calculate_difference(difference, second_word)

print(result)
