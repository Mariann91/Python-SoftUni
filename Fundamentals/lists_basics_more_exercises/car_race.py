times = input().split()

finish_point = len(times) // 2
left_car_time = 0

for index in range(finish_point):

    left_car_time += int(times[index])
    if int(times[index]) == 0:
        left_car_time *= 0.80

right_car_time = 0

for index in range(len(times) - 1, finish_point, -1):

    right_car_time += int(times[index])
    if int(times[index]) == 0:
        right_car_time *= 0.80

if right_car_time < left_car_time:
    print(f"The winner is right with total time: {right_car_time:.1f}")
else:
    print(f"The winner is left with total time: {left_car_time:.1f}")
