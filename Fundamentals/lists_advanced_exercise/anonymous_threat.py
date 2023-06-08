# abc, def, ghi

def merge(input_list, start, end):
    merge_word = ""
    end = min(end, len(input_list) - 1)
    if start > end:
        start -= end
    for index in range(start, end + 1):
        merge_word += input_list[index]

    for index in range(end + 1):
        input_list.pop(0)

    input_list.insert(start, merge_word)
    return input_list


input_words = input().split()

command = input()

while command != "3:1":

    command = command.split()
    start_index = int(command[1])
    end_index = int(command[2])

    new_list = merge(input_words, start_index, end_index)

    command = input()

print(new_list)





















