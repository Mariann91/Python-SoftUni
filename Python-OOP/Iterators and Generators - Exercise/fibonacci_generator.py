from collections import deque


def fibonacci():
  numbers = deque([0, 1])
  numbers_copy = numbers.copy()

  while numbers:
    yield numbers.popleft()

  while True:
    index = len(numbers_copy) - 1

    current_number = numbers_copy[index] + numbers_copy[index - 1]
    
    yield current_number

    numbers_copy.append(current_number)
    
