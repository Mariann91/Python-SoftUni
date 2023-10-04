def even_odd(*args):

  command = args[-1]
  numbers = args[:len(args) - 1]

  calculate = {
    "even": [int(num) for num in numbers if num % 2 == 0],
    "odd": [int(num) for num in numbers if num % 2 != 0]
  }
  
  return calculate[command]
  
