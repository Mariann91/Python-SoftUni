people_list = input().split()
kill_position = int(input()) - 1

kill_list = []
kill_counter = 0
while len(people_list) > 0:
    kill_counter += kill_position
    if kill_counter < len(people_list):
        kill_list.append(people_list.pop(kill_counter))
    else:
        while kill_counter >= len(people_list):
            kill_counter -= len(people_list)
        kill_list.append(people_list.pop(kill_counter))

print(f'[{",".join(kill_list)}]')
