interval = int(input())

free_chairs = 0
flag = True
for index in range(1, interval + 1):
    chair_info = input().split()
    available_chairs = len(chair_info[0])
    needed_chairs = int(chair_info[1])

    if available_chairs < needed_chairs:
        print(f"{needed_chairs - available_chairs} more chairs needed in room {index}")
        flag = False
    else:
        free_chairs += available_chairs - needed_chairs

if flag:
    print(f"Game On, {free_chairs} free chairs left")
