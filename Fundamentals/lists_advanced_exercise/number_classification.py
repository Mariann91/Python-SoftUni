numbers = [int(num) for num in input().split(", ")]

positive = [num for num in numbers if num >= 0]
negative = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

all_lists = [positive, negative, even, odd]

numbers = [[str(num) for num in sublist] for sublist in all_lists]

print(f"Positive: {', '.join(numbers[0])}\nNegative: {', '.join(numbers[1])}"
      f"\nEven: {', '.join(numbers[2])}\nOdd: {', '.join(numbers[3])}")
