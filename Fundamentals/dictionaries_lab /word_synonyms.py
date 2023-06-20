words_count = int(input())

words_dic = {}
for _ in range(words_count):
  word = input()
  synonym = input()

  if word not in words_dic:
    words_dic[word] = [synonym]
  else:
    words_dic[word].append(synonym)

for key, value in words_dic.items():
  synonyms = ", ".join(value)
  print(f"{key} - {synonyms}")
  
