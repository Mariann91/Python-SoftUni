from collections import deque


def list_manipulator(numbers, *args):
    numbers = deque(numbers)
    command = args[0]
    position = args[1]
    args_numbers = []

    if len(args) > 2:
        args_numbers = list(args[2::])

    if command + " " + position == "add beginning":
        [numbers.insert(index, args_numbers[index]) for index in range(len(args_numbers))] if args_numbers else ""

    elif command + " " + position == "add end":
        [numbers.append(num) for num in args_numbers] if args_numbers else ""

    elif command + " " + position == "remove beginning":
        [numbers.popleft() for _ in range(args_numbers[0])] if args_numbers else numbers.popleft()
      
    elif command + " " + position == "remove end":
        [numbers.pop() for _ in range(args_numbers[0])] if args_numbers else numbers.pop()

    return list(numbers)
