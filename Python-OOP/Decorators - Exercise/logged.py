def logged(function):

  def wrapper(*args):
    return f"you called {function.__name__}({', '.join(map(repr, args))})\nit returned {function(*args)}"

  return wrapper
  
