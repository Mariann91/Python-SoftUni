# start_list = input().split()
#
# command = input()
#
# while command != "3:1":
#     command_args = command.split()
#     command_word = command_args[0]
#
#     if command_word == "merge":
#         start_index = int(command_args[1])
#         end_index = int(command_args[2])
#
#         new_list = []
#         string = ""
#         for i in range(len(start_list)):
#             if start_index <= i <= end_index:
#                 string += start_list[i]
#             else:
#                 if string not in new_list:
#                     new_list.append(string)
#                 new_list.append(start_list[i])
#     else:
#         index = int(command_args[1])
#         parts = int(command_args[2])
#
#     command = input()
#
# print("".join(start_list))

test = ["abcdef", "ghi", "jkl"]
index = 0
parts = 3

seg_len = len(test[0])
seg_list = [""] * parts

print(max(len(test)))








