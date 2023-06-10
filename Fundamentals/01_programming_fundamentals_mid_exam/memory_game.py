def check_cheat(first, second, input_list):
    if 0 <= first < len(input_list) and 0 <= second < len(input_list) and first != second:
        return True
    return False


cards = input().split()

indexes = input()

moves = 0
while indexes != "end":
    index1, index2 = [int(num) for num in indexes.split()]
    moves += 1

    if check_cheat(index1, index2, cards):
        if cards[index1] == cards[index2]:
            removed_card = cards[index1]
            cards.pop(index1)
            cards.remove(removed_card)
            print(f"Congrats! You have found matching elements - {removed_card}!")
        else:
            print("Try again!")
    else:
        middle_index = int(len(cards) // 2)
        bonus_seq = f"-{moves}a"
        for _ in range(2):
            cards.insert(middle_index, bonus_seq)
        print("Invalid input! Adding additional elements to the board")

    if len(cards) == 0:
        print(f"You have won in {moves} turns!")
        break

    indexes = input()
else:
    print("Sorry you lose :(")
    print(*cards, sep=" ")
