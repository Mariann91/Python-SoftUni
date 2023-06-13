def check_index(checked_index, checked_list):
    if 0 <= checked_index < len(checked_list):
        return True
    return False


targets = [int(num) for num in input().split()]

command = input()

while command != "End":
    command = command.split()
    command_word = command[0]
    index = int(command[1])
    value = int(command[2])

    if command_word == "Shoot" and check_index(index, targets):
        targets[index] -= value
        if targets[index] <= 0:
            targets.pop(index)

    elif command_word == "Add":
        if check_index(index, targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command_word == "Strike":
        start_point = index - value
        end_point = index + value

        if check_index(start_point, targets) and check_index(end_point, targets) and check_index(index, targets):
            for i in range(start_point, end_point + 1):
                targets.remove(targets[start_point])
        else:
            print("Strike missed!")

    command = input()

print(*targets, sep="|")
