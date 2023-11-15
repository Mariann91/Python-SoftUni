def type_check(decorater_type):
  
  def decorater(function):
    
    def wrapper(*args):
      args_type = type(*args)

      if args_type != decorater_type:
        return "Bad Type"

      return function(*args)

    return wrapper
    
  return decorater
