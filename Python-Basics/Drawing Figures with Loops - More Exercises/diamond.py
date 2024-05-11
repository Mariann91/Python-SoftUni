from math import ceil


def print_first_line():
    print(left_right * "-", end="")
    print(init_stars_count * "*", end="")
    print(left_right * "-", end="")


def print_n_lines():
    print(left_right * "-", end="")
    print("*", end="")
    print(middle_dashes * "-", end="")
    print("*", end="")
    print(left_right * "-", end="")


def print_middle_line():
    print("*", end="")
    print(middle_dashes * "-", end="")
    print("*", end="")


n = int(input())
init_stars_count = 1

if n % 2 == 0:
    init_stars_count = 2

middle_dashes = init_stars_count
left_right = int((n - 1) / 2)
middle = ceil(n / 2)

for i in range(middle):

    if i == 0:
        print_first_line()
    else:
        if left_right > 0:
            print_n_lines()
        else:
            print_middle_line()

        middle_dashes += 2

    left_right -= 1
    print()

left_right = 0
middle_dashes -= 2

for i in range(middle, 1, - 1):
    left_right += 1
    middle_dashes -= 2

    if i != 2:
        print_n_lines()
    else:
        print_first_line()
    print()
