def tags(tag):
  
  def decorater(function):

    def wrapper(*args):

      return f"<{tag}>{function(*args)}</{tag}>"

    return wrapper

  return decorater
