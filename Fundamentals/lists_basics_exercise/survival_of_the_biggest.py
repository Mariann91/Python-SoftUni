integer_list = input().split()
numbers_to_remove = int(input())

integer_list = [int(num) for num in integer_list]

for _ in range(numbers_to_remove):
    integer_list.remove(min(integer_list))
print(*integer_list, sep=", ")
