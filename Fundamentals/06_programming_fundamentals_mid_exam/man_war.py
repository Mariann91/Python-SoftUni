def check_index(index, input_list):
  if 0 <= index < len(input_list):
    return True
  return False
  

pirate_sections = [int(num) for num in input().split(">")]
warship_sections = [int(num) for num in input().split(">")]
section_max_health = int(input())

command = input()

draw_flag = True
while command != "Retire":
  command = command.split()
  command_word = command[0]

  if command_word == "Fire":
    attacked_warship_section = int(command[1])
    damage = int(command[2])
    
    if check_index(attacked_warship_section, warship_sections):
      warship_section = int(command[1])
      damage = int(command[2])
      warship_sections[warship_section] -= damage
    
      if warship_sections[warship_section] <= 0:
        print("You won! The enemy ship has sunken.")
        draw_flag = False
        break

  elif command_word == "Defend":
    start_point = int(command[1])
    end_point = int(command[2])
    damage = int(command[3])

    if check_index(start_point, pirate_sections) and check_index(end_point, pirate_sections):
      for i in range(start_point, end_point + 1):
        pirate_sections[i] -= damage
        if pirate_sections[i] <= 0:
          print("You lost! The pirate ship has sunken.")
          draw_flag = False
          break
  elif command_word == "Repair":
    repair_index = int(command[1])
    health = int(command[2])

    if check_index(repair_index, pirate_sections):
      if pirate_sections[repair_index] + health > section_max_health:
        health = section_max_health - pirate_sections[repair_index]
      pirate_sections[repair_index] += health

  elif command_word == "Status":
    bellow_max_counter = 0
    twenty_percent = section_max_health * 0.20
    for i in range(len(pirate_sections)):
      if pirate_sections[i] < twenty_percent:
        bellow_max_counter += 1
    print(f"{bellow_max_counter} sections need repair.")
    
  command = input()

if draw_flag:
  print(f"Pirate ship status: {sum(pirate_sections)}")
  print(f"Warship status: {sum(warship_sections)}")
