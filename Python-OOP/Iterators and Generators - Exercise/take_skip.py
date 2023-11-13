class take_skip:
  def __init__(self, step: int, count: int) -> None: 
    self.step = step 
    self.count = count
    self.result = 0 - self.step

  def __iter__(self):
    return self

  def __next__(self):

    if self.count == 0:
      raise StopIteration

    self.count -= 1
    self.result += self.step

    return self.result
