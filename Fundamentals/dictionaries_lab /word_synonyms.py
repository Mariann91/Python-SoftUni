words_info = {}

interval = int(input())

for _ in range(interval):
  word = input()
  synonym = input()

  if word not in words_info:
    words_info[word] = []
  words_info[word].append(synonym)  

for word, synonyms in words_info.items():
  print(f"{word} - {', '.join(synonyms)}")
  
