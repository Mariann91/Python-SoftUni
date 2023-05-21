int_list = input().split(", ")

for index in range(len(int_list)):

    if int_list[index] == "0":
        int_list.remove(int_list[index])
        int_list.append("0")

int_list = [int(num) for num in int_list]
print(int_list)
