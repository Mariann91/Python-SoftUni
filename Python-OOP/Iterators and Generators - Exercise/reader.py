def read_next(*args):
  
  for el in args:
    
    for part in el:
      yield part
      
