from collections import deque

stack = deque(input().split())
stack.reverse()

print(" ".join(stack))
