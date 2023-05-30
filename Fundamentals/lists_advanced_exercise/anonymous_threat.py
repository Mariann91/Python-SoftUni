# start_string = input().split()
#
# command = input()
#
# while command != "3:1":
#     command_args = command.split()
#     command_line = command_args[0]
#     index = int(command_args[1])
#     end_line = int(command_args[2])
#
#     if command_line == "merge":
#         merge_word = ""
#         new_list = []
#
#         for i in range(len(start_string)):
#
#             if index <= i <= end_line:
#                 merge_word += start_string[i]
#             else:
#                 new_list.append(start_string[i])
#
#         new_list.insert(index, merge_word)
#         start_string = new_list
#
#     command = input()


example = ["abcdef", "ghi", "jkl"]

chars_per_item = len(example) / 3

print(chars_per_item)

for i in range(3):
    example.insert(0, "")

print(example)

















