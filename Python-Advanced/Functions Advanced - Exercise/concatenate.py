def concatenate(*args, **kwargs):
  output = ""

  for el in args:
    output += el

  for key, value in kwargs.items():
    if key in output:
      output = output.replace(key, value)
      
  return output
  
