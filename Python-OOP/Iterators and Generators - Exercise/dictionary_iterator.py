class dictionary_iter:
  def __init__(self, dictionary):
    self.dictionary = dictionary

  def __iter__(self):
    return self

  def __next__(self):

    if not self.dictionary:
      raise StopIteration

    key = next(iter(self.dictionary))
    value = self.dictionary[key]

    self.dictionary.pop(key)

    return (key, value)
