def find_max_even(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]

    if len(even_numbers) >= 1:
        max_num = max(even_numbers)
        for i in range(len(input_list) - 1, -1, -1):
            if input_list[i] == max_num:
                return i
    return "No matches"


def find_max_odd(input_list):
    odd_numbers = [num for num in input_list if num % 2 != 0]

    if len(odd_numbers) >= 1:
        max_num = max(odd_numbers)
        for i in range(len(input_list) - 1, -1, -1):
            if input_list[i] == max_num:
                return i
    return "No matches"


def find_min_even(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]

    if len(even_numbers) >= 1:
        min_num = min(even_numbers)
        for i in range(len(input_list) - 1, -1, -1):
            if input_list[i] == min_num:
                return i
    return "No matches"


def find_min_odd(input_list):
    odd_numbers = [num for num in input_list if num % 2 != 0]

    if len(odd_numbers) >= 1:
        min_num = min(odd_numbers)
        for i in range(len(input_list) - 1, -1, -1):
            if input_list[i] == min_num:
                return i
    return "No matches"
