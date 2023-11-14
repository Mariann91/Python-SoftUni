from itertools import permutations 

def possible_permutations(custom_list):
  perm = permutations(custom_list) 

  for item in perm:
    yield list(item)
    
