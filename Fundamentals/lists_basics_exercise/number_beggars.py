income_list = input().split(", ")
beggars_count = int(input())

beggars_list = [0] * beggars_count

beggars_index = 0
for index in range(len(income_list)):
    if beggars_index >= len(beggars_list):
        beggars_index = 0

    beggars_list[beggars_index] += int(income_list[index])
    beggars_index += 1

print(beggars_list)
