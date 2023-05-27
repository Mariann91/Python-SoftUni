from math import ceil

numbers = [int(num) for num in input().split(", ")]

max_number = max(numbers)
groups = ceil(max_number / 10)

all_groups = []
boundary = 10
for _ in range(groups):
    current_group_list = (list(filter(lambda x: x <= boundary, numbers)))
    numbers = [num for num in numbers if num not in current_group_list]
    all_groups.append(current_group_list)
    boundary += 10

for group in range(1, groups + 1):
    print(f"Group of {group}0's: {all_groups[group - 1]}")
