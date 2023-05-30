first = input()
second = input()

[print(second[:index + 1] + first[index + 1:]) for index in range(len(first)) if first[index] != second[index]]
