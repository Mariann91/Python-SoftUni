MAX_HP = 100
MAX_MP = 200

heroes_info = {}

interval = int(input())

for _ in range(interval):
    current_hero = input().split()
    hero_name = current_hero[0]
    hp = int(current_hero[1])
    mp = int(current_hero[2])

    heroes_info[hero_name] = [hp, mp]

command_line = input()

while command_line != "End":
    command_args = command_line.split(" - ")
    command = command_args[0]

    if command == "CastSpell":
        name = command_args[1]
        mp_needed = int(command_args[2])
        spell_name = command_args[3]

        if heroes_info[name][1] >= mp_needed:
            heroes_info[name][1] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes_info[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        name = command_args[1]
        damage = int(command_args[2])
        attacker = command_args[3]
        heroes_info[name][0] -= damage

        if heroes_info[name][0] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_info[name][0]} HP left!")
        else:
            heroes_info.pop(name)
            print(f"{name} has been killed by {attacker}!")
    elif command == "Recharge":
        name = command_args[1]
        amount = int(command_args[2])

        if amount + heroes_info[name][1] <= MAX_MP:
            gained_mp = amount
        else:
            gained_mp = MAX_MP - heroes_info[name][1]

        heroes_info[name][1] += gained_mp
        print(f"{name} recharged for {gained_mp} MP!")
    elif command == "Heal":
        name = command_args[1]
        amount = int(command_args[2])

        if amount + heroes_info[name][0] <= MAX_HP:
            gained_hp = amount
        else:
            gained_hp = MAX_HP - heroes_info[name][0]

        heroes_info[name][0] += gained_hp

        print(f"{name} healed for {gained_hp} HP!")

    command_line = input()

for name, values in heroes_info.items():
    print(name)
    print(f"  HP: {values[0]}")
    print(f"  MP: {values[1]}")
