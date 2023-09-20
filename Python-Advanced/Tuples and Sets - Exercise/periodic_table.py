elements = set()

for _ in range(int(input())):
  current_elements = input().split()

  for element in current_elements:
    elements.add(element)

print(*elements, sep="\n")
