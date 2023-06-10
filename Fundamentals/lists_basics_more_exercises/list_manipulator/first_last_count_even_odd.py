def check_count(count, input_list):
    if 0 <= count <= len(input_list):
        return True
    return False


def first_count_even(count, input_list):
    even_counter = 0
    count_even_list = []
    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            even_counter += 1
            count_even_list.append(input_list[i])
            if even_counter == count:
                break
    return count_even_list


def first_count_odd(count, input_list):
    odd_counter = 0
    count_odd_list = []
    for i in range(len(input_list)):
        if input_list[i] % 2 != 0:
            odd_counter += 1
            count_odd_list.append(input_list[i])
            if odd_counter == count:
                break
    return count_odd_list


def last_count_even(count, input_list):
    even_counter = 0
    count_even_list = []
    for i in range(len(input_list) - 1, - 1, - 1):
        if input_list[i] % 2 == 0:
            even_counter += 1
            count_even_list.append(input_list[i])
            if even_counter == count:
                break
    return count_even_list


def last_count_odd(count, input_list):
    odd_counter = 0
    count_odd_list = []
    for i in range(len(input_list) - 1, - 1, -1):
        if input_list[i] % 2 != 0:
            odd_counter += 1
            count_odd_list.append(input_list[i])
            if odd_counter == count:
                break
    return count_odd_list
