targets = [int(num) for num in input().split()]

shoot_index = input()
shoot_targets = 0
while shoot_index != "End":
  shoot_index = int(shoot_index)
  
  if 0 <= shoot_index < len(targets):
    current_target = targets[shoot_index]
    targets[shoot_index] = -1
    shoot_targets += 1

    for i in range(len(targets)):
      if targets[i] > current_target and targets[i] != targets[shoot_index]:
        targets[i] -= current_target
      elif targets[i] <= current_target and targets[i] != targets[shoot_index]:
        targets[i] += current_target 

  shoot_index = input()

print(f"Shot targets: {shoot_targets} -> ", *targets, sep=" ")
      
