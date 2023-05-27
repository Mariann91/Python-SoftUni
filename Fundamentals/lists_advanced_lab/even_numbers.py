numbers = input().split(", ")

print([index for index in range(len(numbers)) if int(numbers[index]) % 2 == 0])
