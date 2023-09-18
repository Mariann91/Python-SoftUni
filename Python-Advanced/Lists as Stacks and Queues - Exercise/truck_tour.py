from collections import deque

pumps_info = deque([[int(num) for num in input().split()] for _ in range(int(input()))])
pumps_info_copy = pumps_info.copy()
tank = 0
index = 0

while pumps_info_copy:
    fuel, distance = pumps_info_copy.popleft()
    tank += fuel

    if tank >= distance:
        tank -= distance
    else:
        pumps_info.rotate(-1)
        pumps_info_copy = pumps_info.copy()
        tank = 0
        index += 1

print(index)
