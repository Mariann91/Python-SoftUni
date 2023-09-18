from collections import deque

stack = deque(list(input()))
stack.reverse()

print("".join(stack))
