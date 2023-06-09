def check_index(index, input_list):
  if 0 <= index < len(input_list):
    return True 
  return False


def reduce_increase_value(index, input_list):
  target_value = input_list[index]

  for i in range(len(input_list)):
    if input_list[i] > target_value and input_list[i] not in shot_targets:
      input_list[i] -= target_value
      
    elif input_list[i] <= target_value and input_list[i] not in shot_targets:
      input_list[i] += target_value
  return input_list
  

targets = [int(num) for num in input().split()]

shot_targets_count = 0

shot_targets = []
while True:
  current_index = input()

  if current_index == "End":
    print(f"Shot targets: {shot_targets_count} -> ", end="")
    print(*targets, sep=" ")
    break

  current_index = int(current_index)

  if check_index(current_index, targets):
    if targets[current_index] != -1:
      targets = reduce_increase_value(current_index, targets)
      targets[current_index] = -1
      shot_targets.append(targets[current_index])
      shot_targets_count += 1
      
