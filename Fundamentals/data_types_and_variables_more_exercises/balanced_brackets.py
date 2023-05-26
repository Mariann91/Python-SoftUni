char_count = int(input())

brackets = []
for _ in range(char_count):
    characters = input()

    if characters == "(" or characters == ")":
        brackets.append(characters)

balanced_counter = 0
for index in range(1, len(brackets) + 1):
    if index % 2 != 0 and brackets[index - 1] == "(":
        balanced_counter += 1
    elif index % 2 == 0 and brackets[index - 1] == ")":
        balanced_counter += 1

if len(brackets) == balanced_counter:
    print("BALANCED")
else:
    print("UNBALANCED")



