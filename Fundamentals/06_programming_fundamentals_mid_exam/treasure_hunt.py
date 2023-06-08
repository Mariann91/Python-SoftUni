def loot(chest, order):
    for i in range(1, len(order)):
        if order[i] not in chest:
            chest.insert(0, order[i])
    return chest


def drop(position, chest):
    item_to_remove_and_append = chest[position]
    chest.pop(position)
    chest.append(item_to_remove_and_append)
    return chest


def steal(count, chest):
    count = min(count, len(chest))
    removed_items = []
    for i in range(1, count + 1):
        i = - i
        removed_items.insert(i, chest[i])

    for _ in range(count):
        chest.pop(-1)

    return removed_items


def calculate_treasure_gain(chest):
    if len(chest) > 0:
        sum_len = 0
        for item in chest:
            sum_len += len(item)

        return f"Average treasure gain: {sum_len / len(chest):.2f} pirate credits."

    else:

        return "Failed treasure hunt."


chest_items = input().split("|")

command = input()

while command != "Yohoho!":
    command = command.split()
    command_word = command[0]

    if command_word == "Loot":
        chest_items = loot(chest_items, command)

    elif command_word == "Drop":
        drop_index = int(command[1])
        if -len(chest_items) <= drop_index < len(chest_items):
            chest_items = drop(drop_index, chest_items)
        else:
            continue

    elif command_word == "Steal":
        items_count = int(command[1])
        stolen_items = steal(items_count, chest_items)
        print(", ".join(stolen_items))

    command = input()

print(calculate_treasure_gain(chest_items))
