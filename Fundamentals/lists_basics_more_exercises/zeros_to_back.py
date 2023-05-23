int_list = [int(num) for num in input().split(", ")]

zeros_counter = int_list.count(0)
int_list = [num for num in int_list if num != 0]

for _ in range(zeros_counter):
    int_list.append(0)
print(int_list)
