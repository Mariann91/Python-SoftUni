def even_numbers(function):

    def wrapper(numbers):
        
        result = function(numbers)

        return [num for num in result if num % 2 == 0]

    return wrapper
  
