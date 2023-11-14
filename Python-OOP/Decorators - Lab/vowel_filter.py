def vowel_filter(function):

    def wrapper():
        result = [char for char in function() if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]

        return result

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
  
