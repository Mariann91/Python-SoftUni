from exchange import check_index, exchange
from max_min_even_odd import find_max_even, find_max_odd, find_min_even, find_min_odd
from first_last_count_even_odd import check_count, first_count_even, first_count_odd, last_count_even, last_count_odd

numbers = [int(num) for num in input().split()]

command = input()

while command != "end":
    command = command.split()
    command_word = command[0]

    if command_word == "exchange":
        index = int(command[1])

        if check_index(index, numbers):
            numbers = exchange(index, numbers)
        else:
            print("Invalid index")

    elif command_word == "max" and command[1] == "even":
        print(find_max_even(numbers))

    elif command_word == "max" and command[1] == "odd":
        print(find_max_odd(numbers))

    elif command_word == "min" and command[1] == "even":
        print(find_min_even(numbers))

    elif command_word == "min" and command[1] == "odd":
        print(find_min_odd(numbers))

    elif command_word == "first" or command_word == "last":
        count = int(command[1])
        num_type = command[2]

        if check_count(count, numbers):

            if command_word == "first" and num_type == "even":
                print(first_count_even(count, numbers))

            elif command_word == "first" and num_type == "odd":
                print(first_count_odd(count, numbers))

            elif command_word == "last" and num_type == "even":
                print(last_count_even(count, numbers))

            elif command_word == "last" and num_type == "odd":
                print(last_count_odd(count, numbers))

        else:
            print("Invalid count")

    command = input()

print(numbers)
