def check_index(ship, index):
    if 0 <= index < len(ship):
        return True
    else:
        return False


pirate_ship_status = [int(num) for num in input().split(">")]
war_ship_status = [int(num) for num in input().split(">")]
sec_max_health = int(input())

command = input()

break_flag = False
while command != "Retire":
    command = command.split()
    command_word = command[0]

    if command_word == "Fire":
        warship_section = int(command[1])
        damage_dealt = int(command[2])

        if check_index(war_ship_status, warship_section):
            war_ship_status[warship_section] -= damage_dealt
            if war_ship_status[warship_section] <= 0:
                print("You won! The enemy ship has sunken.")
                break

    elif command_word == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage_dealt = int(command[3])
        if check_index(pirate_ship_status, start_index) and check_index(pirate_ship_status, end_index):
            for i in range(start_index, end_index + 1):
                pirate_ship_status[i] -= damage_dealt
                if pirate_ship_status[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    break_flag = True
                    break
            if break_flag:
                break

    elif command_word == "Repair":
        section = int(command[1])
        gained_health = int(command[2])

        if check_index(pirate_ship_status, section):
            if pirate_ship_status[section] + gained_health <= sec_max_health:
                pirate_ship_status[section] += gained_health
            else:
                gained_health = sec_max_health - pirate_ship_status[section]
                pirate_ship_status[section] += gained_health

    elif command_word == "Status":
        repair_limit = sec_max_health * 0.20

        section_counter = 0
        for i in range(len(pirate_ship_status)):
            if pirate_ship_status[i] < repair_limit:
                section_counter += 1
        print(f"{section_counter} sections need repair.")

    command = input()

else:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(war_ship_status)}")

