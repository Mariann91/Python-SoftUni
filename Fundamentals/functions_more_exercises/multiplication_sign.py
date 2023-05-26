def multiplication_sign(int_list):
    negative_counter = 0

    for num in int_list:

        if num == 0:
            return "zero"

        if num < 0:
            negative_counter += 1

    if negative_counter == 1 or negative_counter == 3:
        return "negative"

    return "positive"


num_list = [int(input()), int(input()), int(input())]
print(multiplication_sign(num_list))
