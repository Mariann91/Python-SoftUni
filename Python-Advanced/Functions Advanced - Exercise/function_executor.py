def func_executor(*args):
  output = []

  for item in args:
    item_function = item[0]
    item_function_parameters = item[1]
    output.append(f"{item_function.__name__} - {item_function(*item_function_parameters)}")
  
  return "\n".join(output)
