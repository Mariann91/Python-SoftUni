stack = []
n = int(input())

for _ in range(n):
  query = input().split()
  query_type = query[0]

  if query_type == "1":
    number = int(query[1])
    stack.append(number)

  if len(stack) > 0:
    if query_type == "2":
      stack.pop()
    elif query_type == "3":
      print(max(stack))
    elif query_type == "4":
      print(min(stack))
 
new_stack = []

for _ in range(len(stack)):
  new_stack.append(stack.pop())

print(*new_stack, sep=", ")
