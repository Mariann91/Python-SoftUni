def even_parameters(function):

  def wrapper(*args):

    for num in args:
      if not isinstance(num, int) or num % 2 != 0:
        return "Please use only even numbers!"

    return function(*args)

  return wrapper
