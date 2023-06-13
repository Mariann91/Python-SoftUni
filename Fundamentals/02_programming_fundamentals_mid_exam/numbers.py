numbers = [int(num) for num in input().split()]

numbers = sorted(numbers, reverse=True)
average = sum(numbers) / len(numbers)

top_five_average = []
five_counter = 0
for num in numbers:
    if num > average:
        top_five_average.append(num)
        five_counter += 1
        if five_counter == 5:
            break

if len(top_five_average) > 0:
    print(*top_five_average, sep=" ")
else:
    print("No")
