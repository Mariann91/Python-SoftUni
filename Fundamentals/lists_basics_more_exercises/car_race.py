times_list = [int(num) for num in input().split()]
finish_line = len(times_list) // 2 + 1

left_car_time = 0
for index in range(0, finish_line - 1):
    left_car_time += times_list[index]
    if times_list[index] == 0:
        left_car_time *= 0.80

right_car_time = 0
for index in range(len(times_list) - 1, finish_line - 1, -1):
    right_car_time += times_list[index]
    if times_list[index] == 0:
        right_car_time *= 0.80
if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")
