people_list = input().split()
killed_position = int(input())

killed_list = []
counter, index = 0, 0
while len(people_list) > 0:
    counter += 1

    if counter % killed_position == 0:
        killed_list.append(people_list.pop(index))
    else:
        index += 1

    if len(people_list) <= index:
        index = 0

print(f"[{','.join(killed_list)}]")
