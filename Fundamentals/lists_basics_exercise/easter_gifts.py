gift_list = input().split()

while True:
    command = input()

    if command == "No Money":
        gift_list = [item for item in gift_list if item is not None]
        print(" ".join(gift_list))
        break

    command_list = command.split()

    if command_list[0] == "OutOfStock":
        for index in range(len(gift_list)):
            if gift_list[index] == command_list[1]:
                gift_list[index] = None

    elif command_list[0] == "Required" and 0 <= int(command_list[2]) < len(gift_list):
        gift_list[int(command_list[2])] = command_list[1]

    elif command_list[0] == "JustInCase":
        gift_list[-1] = command_list[1]

gift_list = [item for item in gift_list if item is not None]
