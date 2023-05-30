word = input().lower()

words_to_count = ["sand", "water", "fish", "sun"]
total_count = 0
for item in words_to_count:
    total_count += word.count(item)
print(total_count)
