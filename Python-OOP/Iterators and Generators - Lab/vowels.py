from collections import deque


class vowels:
  def __init__(self, text: str) -> None:
    self.text = text
    self.vowels_in_text = deque(char for char in self.text if char in ['a' , 'e', 'i', 'o', 'u', 'y', 'Y', 'A', 'E', 'I', 'O', 'U'])

  def __iter__(self):
    return self

  def __next__(self):

    if not self.vowels_in_text:
      raise StopIteration

    return self.vowels_in_text.popleft()
    
