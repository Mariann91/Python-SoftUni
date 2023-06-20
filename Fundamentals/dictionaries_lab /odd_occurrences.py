words = [word.lower() for word in input().split()]

words_dic = {key: 0 for key in words}

for word in words:
  words_dic[word] += 1
  
for key, value in words_dic.items():
  if value % 2 != 0:
    print(key, end= " ")
    
