int_list = [int(num) for num in input().split()]

while True:

    command = input()

    if command == "end":
        break

    command_list = command.split()
    command_word = command_list[0]

    # Exchange part start of code
    if command_word == "exchange":
        exchange_index = int(command_list[1])

        if 0 <= exchange_index < len(int_list):
            first_half = []
            second_half = []

            for index in range(len(int_list)):
                if index <= exchange_index:
                    first_half.append(int_list[index])
                else:
                    second_half.append(int_list[index])

            int_list = second_half + first_half
        else:
            print("Invalid index")
    # Exchange part end of code

    even_list = [num for num in int_list if num % 2 == 0]
    odd_list = [num for num in int_list if num % 2 != 0]

    # Max even/odd start of code
    if command_word == "max":
        if command_list[1] == "even":
            if len(even_list) >= 1:
                max_even_number = max(even_list)
                max_even_index = int_list.index(max_even_number)
                if int_list.count(max_even_number) > 1:
                    for i in range(len(int_list) - 1, -1, -1):
                        if int_list[i] == max_even_number:
                            max_even_index = i
                            break
                print(max_even_index)
            else:
                print("No matches")

        elif command_list[1] == "odd":
            if len(odd_list) >= 1:
                max_odd_number = max(odd_list)
                max_odd_index = int_list.index(max_odd_number)

                if int_list.count(max_odd_number) > 1:
                    for i in range(len(int_list) - 1, -1, -1):
                        if int_list[i] == max_odd_number:
                            max_odd_index = i
                            break
                print(max_odd_index)
            else:
                print("No matches")
    # Max even/odd end of code

    # Min even/odd start of code

    elif command_word == "min":
        if command_list[1] == "even":
            if len(even_list) >= 1:
                min_even_number = min(even_list)
                min_even_index = int_list.index(min_even_number)
                if int_list.count(min_even_number) > 1:
                    for i in range(len(int_list) - 1, -1, -1):
                        if int_list[i] == min_even_number:
                            min_even_index = i
                            break
                print(min_even_index)
            else:
                print("No matches")

        elif command_list[1] == "odd":
            if len(odd_list) >= 1:
                min_odd_number = min(odd_list)
                min_odd_index = int_list.index(min_odd_number)

                if int_list.count(min_odd_number) > 1:
                    for i in range(len(int_list) - 1, -1, -1):
                        if int_list[i] == min_odd_number:
                            min_odd_index = i
                            break
                print(min_odd_index)
            else:
                print("No matches")
    # Min even/odd start of code

    # First even/odd start of code

    elif command_word == "first":
        count = int(command_list[1])
        number_type = command_list[2]
        if len(int_list) >= count > 0:
            if number_type == "even":
                first_even = []
                for num in even_list:
                    first_even.append(num)
                    if len(first_even) == count:
                        break
                print(first_even)
            elif number_type == "odd":
                first_odd = []
                for num in odd_list:
                    first_odd.append(num)
                    if len(first_odd) == count:
                        break
                print(first_odd)
        else:
            print("Invalid count")
    # First even/odd end of code

    # Second even/odd start of code
    elif command_word == "last":
        count = int(command_list[1])
        number_type = command_list[2]
        if 0 < count <= len(int_list):
            if number_type == "even":
                second_even = []
                for i in range(len(even_list) - 1, -1, -1):
                    second_even.append(even_list[i])
                    if len(second_even) == count:
                        break
                print(second_even)
            elif number_type == "odd":
                second_odd = []
                for i in range(len(odd_list) - 1, -1, -1):
                    second_odd.append(odd_list[i])
                    if len(second_odd) == count:
                        break
                print(second_odd)
        else:
            print("Invalid count")
    # Second even/odd end of code
print(int_list)
