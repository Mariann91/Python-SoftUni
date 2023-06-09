def check_index(index, input_list):
  if 0 <= index < len(input_list):
    return True
  return False


def check_zero_hearts(index, input_list):
  if input_list[index] == 0:
    return True
  return False


def check_result(input_list):
  if input_list.count(0) == len(input_list):
    return True
  return False


def count(input_list):
  not_zeros = [num for num in input_list if num != 0]
  return len(not_zeros)

hearts = [int(num) for num in input().split("@")]

jump = input()

current_index = 0
while jump != "Love!":
  jump = jump.split()
  jump_len = int(jump[1])
  current_index += jump_len

  if check_index(current_index, hearts):
    if check_zero_hearts(current_index, hearts):
      print(f"Place {current_index} already had Valentine's day.")
    else:
      hearts[current_index] -= 2
      if check_zero_hearts(current_index, hearts):
        print(f"Place {current_index} has Valentine's day.")
  else:
    current_index = 0
    if check_zero_hearts(current_index, hearts):
      print(f"Place {current_index} already had Valentine's day.")
    else:
      hearts[current_index] -= 2
      if check_zero_hearts(current_index, hearts):
        print(f"Place {current_index} has Valentine's day.") 

  jump = input()

print(f"Cupid's last position was {current_index}.")

if check_result(hearts):
  print("Mission was successful.")
else:
  print(f"Cupid has failed {count(hearts)} places.")
  
