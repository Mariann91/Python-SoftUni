from collections import deque

ranges_info = {
    "Darth Vader Ducky": range(0, 61),
    "Thor Ducky": range(61, 121),
    "Big Blue Rubber Ducky": range(121, 181),
    "Small Yellow Rubber Ducky": range(181, 241),
}

count_rubber_ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

times_per_task = deque([int(num) for num in input().split()])
numbers_of_task = [int(num) for num in input().split()]

while times_per_task and numbers_of_task:
    current_time = times_per_task.popleft()
    current_task = numbers_of_task.pop()

    result = current_time * current_task

    for item, value in ranges_info.items():
        if result in ranges_info[item]:
            count_rubber_ducks[item] += 1
            break
    else:
        current_task -= 2
        numbers_of_task.append(current_task)
        times_per_task.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for item, value in count_rubber_ducks.items():
    print(f"{item}: {value}")
  
