array = [int(num) for num in input().split()]

command = input()

while command != "end":
    command = command.split()
    command_word = command[0]

    if command_word == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        array[index1], array[index2] = array[index2], array[index1]

    elif command_word == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        result = array[index1] * array[index2]
        array[index1] = result

    elif command_word == "decrease":
        array = [num - 1 for num in array]

    command = input()
