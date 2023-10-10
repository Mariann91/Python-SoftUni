from collections import deque
from functools import reduce

line = deque([str(el) if not el.isdigit() and len(el) == 1 else int(el) for el in input().split()])

numbers = []
result = 0

while line:
    line_element = line.popleft()

    if isinstance(line_element, int):
        numbers.append(line_element)
    else:
        output = ""

        if line_element == "+":
            result = reduce(lambda a, b: a + b, numbers)
            output = f'{" + ".join([str(el) for el in numbers])} = {result}'

        elif line_element == "-":
            result = reduce(lambda a, b: a - b, numbers)
            output = f'{" - ".join([str(el) for el in numbers])} = {result}'

        elif line_element == "*":
            result = reduce(lambda a, b: a * b, numbers)
            output = f'{" * ".join([str(el) for el in numbers])} = {result}'

        elif line_element == "/":
            result = int(reduce(lambda a, b: a / b, numbers))
            output = f'{" / ".join([str(el) for el in numbers])} = {result}'

        numbers.clear()
        numbers.append(result)

print(result)
