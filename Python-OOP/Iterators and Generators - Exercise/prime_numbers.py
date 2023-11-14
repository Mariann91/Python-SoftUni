from collections import deque

def get_primes(integer_list):
  deque_integer = deque(integer_list)

  while deque_integer:
    integer = deque_integer.popleft()

    if integer > 1:
      for i in range(2, integer):
         if (integer % i) == 0:
             break
      else:
         yield integer
