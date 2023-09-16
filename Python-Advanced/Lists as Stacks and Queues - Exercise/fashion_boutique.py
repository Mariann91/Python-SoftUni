from collections import deque

clothes = deque([int(num) for num in input().split()])
rack_limit = int(input())

clothes_sum = 0
racks = 0

while clothes:
    current_clothes_count = clothes.pop()
    clothes_sum += current_clothes_count

    if clothes_sum == rack_limit:
        racks += 1
        clothes_sum = 0

    if clothes_sum > rack_limit:
        racks += 1
        clothes_sum = current_clothes_count

    if not clothes and clothes_sum > 0:
        racks += 1

print(racks)
