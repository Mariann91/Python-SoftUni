hearts = [int(num) for num in input().split("@")]

jump_len = input()

current_index = 0
while jump_len != "Love!":
    jump_len = jump_len.split()
    index = int(jump_len[1])

    current_index += index

    if current_index >= len(hearts):
        current_index = 0

    if hearts[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        hearts[current_index] -= 2
        if hearts[current_index] <= 0:
            hearts[current_index] = 0
            print(f"Place {current_index} has Valentine's day.")

    jump_len = input()

print(f"Cupid's last position was {current_index}.")

if hearts.count(0) == len(hearts):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(hearts) - hearts.count(0)} places.")
