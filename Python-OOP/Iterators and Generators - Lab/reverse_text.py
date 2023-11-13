def reverse_text(string):
  list_string = list(string)

  while list_string:
    yield list_string.pop()
