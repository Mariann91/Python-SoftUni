people_list = input().split()
kill_position = int(input()) - 1

kill_counter = 0
killed_list = []
while len(people_list) > 0:
    kill_counter += kill_position

    if kill_counter < len(people_list):
        killed_list.append(people_list[kill_counter])
        people_list.remove(people_list[kill_counter])
    else:
        while kill_counter >= len(people_list):
            kill_counter -= len(people_list)

        killed_list.append(people_list[kill_counter])
        people_list.remove(people_list[kill_counter])

print(f"[{','.join(killed_list)}]")
