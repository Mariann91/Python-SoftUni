def check_index(input_index, input_list):
    if 0 <= input_index < len(input_list):
        return True
    return False


def exchange(input_index, input_list):
    first_list = []
    second_list = []

    for i in range(len(input_list)):
        if i <= input_index:
            first_list.append(input_list[i])
        else:
            second_list.append(input_list[i])
    return second_list + first_list
