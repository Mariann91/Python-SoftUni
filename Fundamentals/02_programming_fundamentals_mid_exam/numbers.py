numbers = [int(num) for num in input().split()]

average = sum(numbers) // len(numbers)

above_average = [num for num in numbers if num > average]
sorted_above_average = sorted(above_average, reverse=True)

top5_average = []
for i in range(len(sorted_above_average)):

    if i < 5:
        top5_average.append(sorted_above_average[i])
    else:
        break

if len(top5_average) == 0:
    print("No")
else:
    print(*top5_average, sep=" ")
