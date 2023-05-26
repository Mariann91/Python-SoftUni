def multiply(n1, n2):
    return n1 * n2


def find_factorial(numbers):
    first_multiply_flag = False

    current_result = 0
    for i in range(len(numbers) - 1, 0, -1):

        if not first_multiply_flag:
            current_result = multiply(numbers[i], numbers[i - 1])
            numbers.remove(numbers[i])
            numbers.remove(numbers[i - 1])
            first_multiply_flag = True
        else:
            current_result = multiply(current_result, numbers[0])
            numbers.remove(numbers[0])

    return current_result


def calculate_result(numbers1, numbers2):
    factorial_num1 = find_factorial(numbers1)
    factorial_num2 = find_factorial(numbers2)

    return f"{factorial_num1 / factorial_num2:.2f}"


num1_list = [num for num in range(int(input()), 0, -1)]
num2_list = [num for num in range(int(input()), 0, -1)]

print(calculate_result(num1_list, num2_list))
