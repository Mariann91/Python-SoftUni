index_list = [num for num in input().split()]
string_list = [letter for letter in input()]

output_word = ""
for index in index_list:
    current_index_list = [int(num) for num in index]
    current_index = sum(current_index_list)

    if current_index < len(string_list):
        output_word += string_list[current_index]
        string_list.remove(string_list[current_index])
    else:
        new_index = current_index - len(string_list)
        output_word += string_list[new_index]
        string_list.remove(string_list[new_index])
print(output_word)
