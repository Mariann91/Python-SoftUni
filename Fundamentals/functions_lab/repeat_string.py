string = input()
multiply_times = int(input())

lambda_string = lambda l_string, l_multiply_times: l_string * l_multiply_times
repeat_string = lambda_string(string, multiply_times)
print(repeat_string)
