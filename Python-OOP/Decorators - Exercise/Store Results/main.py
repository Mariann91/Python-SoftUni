def store_results(function):
  def wrapper(*args):

    result = function(*args)

    f = open('result.txt', 'a')
    f.write(f"Function '{function.__name__}' was called. Result: {result}\n")
    f.close()

    return
