def check_item(item, item_list):
    if item in item_list:
        return True
    return False


product_list = input().split("!")

command = input()

while command != "Go Shopping!":
    command = command.split()
    command_word = command[0]

    if command_word == "Urgent":
        item_to_add = command[1]
        if not check_item(item_to_add, product_list):
            product_list.insert(0, item_to_add)

    elif command_word == "Unnecessary":
        item_to_remove = command[1]
        if check_item(item_to_remove, product_list):
            product_list.remove(item_to_remove)
    elif command_word == "Correct":
        old_item = command[1]
        new_item = command[2]
        if check_item(old_item, product_list):
            old_item_index = product_list.index(old_item)
            product_list[old_item_index] = new_item

    elif command_word == "Rearrange":
        rearrange_item = command[1]
        if check_item(rearrange_item, product_list):
            rearrange_item_index = product_list.index(rearrange_item)
            product_list.append(product_list.pop(rearrange_item_index))

    command = input()

print(", ".join(product_list))
