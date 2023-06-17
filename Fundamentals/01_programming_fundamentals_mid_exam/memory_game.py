def check_cheat(input_index1, input_index2, input_list):
    if input_index1 != input_index2 and 0 <= input_index1 < len(input_list) and 0 <= input_index2 < len(input_list):
        return False
    return True


cards = input().split()

moves = 0
while len(cards) > 0:
    indexes = input()

    if indexes == "end":
        print("Sorry you lose :(\n", *cards, sep=" ")
        break

    indexes = indexes.split()
    index1 = int(indexes[0])
    index2 = int(indexes[1])
    moves += 1

    if check_cheat(index1, index2, cards):
        cards_middle_index = len(cards) // 2
        element_to_add = f"-{moves}a"
        for _ in range(2):
            cards.insert(cards_middle_index, element_to_add)

        print("Invalid input! Adding additional elements to the board")
    else:
        card1 = cards[index1]
        card2 = cards[index2]

        if card1 == card2:
            for _ in range(2):
                cards.remove(card1)
            print(f"Congrats! You have found matching elements - {card1}!")
        else:
            print("Try again!")
else:
    print(f"You have won in {moves} turns!")
