from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, current_pokemon: Pokemon) -> str:

        if current_pokemon not in self.pokemons:
            self.pokemons.append(current_pokemon)

            return f"Caught {current_pokemon.name} with health {current_pokemon.health}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:

        for item in self.pokemons:

            if item.name == pokemon_name:
                self.pokemons.remove(item)

                return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        output = f"Pokemon Trainer {self.name}" + \
                 f"\nPokemon count {len(self.pokemons)}"

        for item in self.pokemons:
            output += "\n- " + item.pokemon_details()

        return output
      
