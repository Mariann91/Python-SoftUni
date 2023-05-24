num_list = [int(num) for num in input().split()]
even_list = list(filter(lambda x: x % 2 == 0, num_list))
print(even_list)
