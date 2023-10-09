first_sequence = {int(num) for num in input().split()}
second_sequence = {int(num)  for num in input().split()}

for _ in range(int(input())):
  command_line = input().split()
  command = command_line[0]
  command_target = command_line[1]

  if command == "Add":
    command_sequence = set(int(num) for num in command_line[2::])
    
    if command_target == "First":
      first_sequence.update(command_sequence)
    else:
      second_sequence.update(command_sequence)
    
  elif command == "Remove":
    command_sequence = set(int(num) for num in command_line[2::])

    if command_target == "First":
      first_sequence = {el for el in first_sequence if el not in command_sequence}
    else:
      second_sequence = {el for el in second_sequence if el not in command_sequence}

  else:
    if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
      print(True)
    else:
      print(False)

sorted_first_sequence = sorted(first_sequence)
sorted_second_sequence = sorted(second_sequence)
print(", ".join(str(el) for el in sorted_first_sequence))
print(", ".join(str(el) for el in sorted_second_sequence))
