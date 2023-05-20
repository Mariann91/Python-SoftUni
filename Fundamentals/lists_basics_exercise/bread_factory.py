events = input().split("|")

MAX_ENERGY = 100
energy, coins = 100, 100

for event in events:
    event_list = event.split("-")
    event_value = int(event_list[1])
    energy_gain = 0

    if event_list[0] == "rest":
        if energy + event_value <= 100:
            energy_gain = event_value
        else:
            energy_gain = MAX_ENERGY - energy
        energy += energy_gain
        print(f"You gained {energy_gain} energy.\nCurrent energy: {energy}.")

    elif event_list[0] == "order":
        if energy >= 30:
            energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if event_value <= coins:
            coins -= event_value
            print(f"You bought {event_list[0]}.")
        else:
            print(f"Closed! Cannot afford {event_list[0]}.")
            break
else:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
