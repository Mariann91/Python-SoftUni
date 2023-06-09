def check_index(command_index, input_list):
    if 0 <= command_index < len(input_list):
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
        start = index - value
        end = index + value

        if 0 <= start < index < end < len(targets):
            for i in range(start, end + 1):
                targets.pop(start)
        else:
            print("Strike missed!")

    command = input()

print(*targets, sep="|")
