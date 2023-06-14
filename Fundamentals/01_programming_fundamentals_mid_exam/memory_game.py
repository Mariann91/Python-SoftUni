def check_for_cheat(input_index1, input_index2, input_list):
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
  if check_for_cheat(index1, index2, cards):
    middle_index = len(cards) // 2
    for _ in range(2):
      cards.insert(middle_index, f"-{moves}a")

    print("Invalid input! Adding additional elements to the board")

  else:
    if cards[index1] == cards[index2]:
      item_to_remove = cards[index1]
      cards.pop(index1)
      cards.remove(item_to_remove)
      
      print(f"Congrats! You have found matching elements - {item_to_remove}!")
    else:
      print("Try again!")

else:
  print(f"You have won in {moves} turns!")
