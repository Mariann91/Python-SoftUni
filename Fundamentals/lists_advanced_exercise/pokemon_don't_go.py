

pokemons = [int(num) for num in input().split()]

captured_pokemons = []
while len(pokemons) > 0:
    index = int(input())

    if index < 0:
        captured_pokemons.append(pokemons[0])
        pokemons.remove(pokemons[0])
        pokemons.insert(0, pokemons[-1])
    elif index > len(pokemons) - 1:
        captured_pokemons.append(pokemons[-1])
        pokemons.remove(pokemons[-1])
        pokemons.append(pokemons[0])
    else:
        current_pokemon_value = pokemons[index]
        captured_pokemons.append(pokemons[index])
        pokemons.remove(pokemons[index])
        pokemons = [num + current_pokemon_value if num <= current_pokemon_value else num - current_pokemon_value for num in pokemons]

print(sum(captured_pokemons))
