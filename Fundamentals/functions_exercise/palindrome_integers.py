def palindrome_check(int_list):
    for num in int_list:
        num = [num for num in num]
        num_list_coppy = num.copy()
        num_list_coppy.reverse()
        if num == num_list_coppy:
            print(True)
        else:
            print(False)


integer_list = [num for num in input().split(", ")]
palindrome_check(integer_list)
