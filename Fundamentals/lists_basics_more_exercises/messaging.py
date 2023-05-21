index_list = input().split()
string_list = input()

string_list = [letter for letter in string_list]
string_max_index = len(string_list)

output = ""

for index in index_list:
    index = [int(num) for num in index]
    current_index = sum(index)

    if string_max_index > current_index:
        output += string_list[current_index]
        string_list.remove(string_list[current_index])
    else:
        new_index = current_index - string_max_index
        output += string_list[new_index]
        string_list.remove(string_list[new_index])

print(output)
