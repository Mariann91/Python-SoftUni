def increase_decrease(input_list, value):
    for i in range(len(input_list)):
        if input_list[i] <= value:
            input_list[i] += value
        else:
            input_list[i] -= value

    return input_list


pokemons = [int(num) for num in input().split()]

removed_pokemons = []
while len(pokemons) > 0:
    current_index = int(input())

    if current_index < 0:
        value_to_compare = pokemons[0]
        removed_pokemons.append(pokemons.pop(0))
        pokemons.insert(0, pokemons[-1])

    elif current_index >= len(pokemons):
        value_to_compare = pokemons[-1]
        removed_pokemons.append(pokemons.pop(-1))
        pokemons.append(pokemons[0])

    else:
        value_to_compare = pokemons[current_index]
        removed_pokemons.append(pokemons.pop(current_index))

    pokemons = increase_decrease(pokemons, value_to_compare)

print(sum(removed_pokemons))
