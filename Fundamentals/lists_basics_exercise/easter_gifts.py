gift_list = [gift for gift in input().split()]

command = input()

while command != "No Money":
  command = command.split()
  command_line = command[0]
  command_gift = command[1]

  if command_line == "OutOfStock":
    for index in range(len(gift_list)):
      if gift_list[index] == command_gift:
        gift_list[index] = None       
  elif command_line == "Required":
    replace_index = int(command[2])
    if 0 <= replace_index < len(gift_list):
      gift_list[replace_index] = command_gift
  else:
    gift_list[-1] = command_gift 
  command = input()

[print(gift, end=" ") for gift in gift_list if gift != None]
