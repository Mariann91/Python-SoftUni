from collections import deque

water_quantity = int(input())
queue = deque()

command = input()

while command != "Start":
  name = command 
  queue.append(name)

  command = input()

second_command = input()

while second_command != "End":
  command_line = second_command.split()
  first_part = command_line[0]

  if first_part.isdigit():
    person_name = queue.popleft()
    
    wanted_litters_of_water = int(first_part)
    if wanted_litters_of_water <= water_quantity:
      water_quantity -= wanted_litters_of_water
      
      print(f"{person_name} got water")
    else:
      print(f"{person_name} must wait")

  else:
    refilled_litters = int(command_line[1])
    water_quantity += refilled_litters

  second_command = input()

print(f"{water_quantity} liters left")
