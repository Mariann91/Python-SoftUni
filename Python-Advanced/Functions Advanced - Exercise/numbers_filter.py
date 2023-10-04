def even_odd_filter(**kwargs):
  dic = {}
  
  for key, values in kwargs.items():

    if key not in dic:
      dic[key] = []
      
    if key == "even":
      dic[key].extend([int(num) for num in values if num % 2 == 0])
    else:
      dic[key].extend([int(num) for num in values if num % 2 != 0])

  sorted_dic = sorted(dic.items(), key=lambda kvp: len(kvp[1]), reverse=True)
    
  return dict(sorted_dic)
  
