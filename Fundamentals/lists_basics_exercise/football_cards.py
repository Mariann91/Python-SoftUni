red_cards_players = input().split(" ")

a_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for red_card in red_cards_players:
    red_card_list = red_card.split("-")
    card_number = int(red_card_list[1])

    if red_card_list[0] == "A" and card_number in a_team:
        a_team.remove(card_number)
    elif red_card_list[0] == "B" and card_number in b_team:
        b_team.remove(card_number)

    if len(a_team) < 7 or len(b_team) < 7:
        print(f"Team A - {len(a_team)}; Team B - {len(b_team)}\nGame was terminated")
        break
else:
    print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")
