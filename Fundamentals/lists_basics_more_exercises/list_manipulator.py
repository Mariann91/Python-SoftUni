def exchange(number_list, idx):
    first_half, second_half = [], []

    for i in range(len(number_list)):
        if i <= idx:
            first_half.append(number_list[i])
        else:
            second_half.append(number_list[i])

    return second_half + first_half


def find_even(num):
    if num % 2 == 0:
        return True


def find_odd(num):
    if num % 2 != 0:
        return True



int_list = [int(num) for num in input().split()]


int_list = exchange(int_list, 2)

odd_list = list(filter(find_odd, int_list))


