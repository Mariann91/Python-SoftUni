import time

def exec_time(function):

  def wrapper(*args):

    start_time = time.time()
    
    function(*args)
    
    end_time = time.time()

    return end_time - start_time

  return wrapper
