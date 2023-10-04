def grocery_store(**kwargs):

  sorted_dic = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
  output = "\n".join([f"{key}: {value}" for key, value in dict(sorted_dic).items()])
  
  return output
