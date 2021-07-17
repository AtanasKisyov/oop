class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, current_pokemon):
        for p in self.pokemons:
            if p.name == current_pokemon.name:
                return "This pokemon is already caught"
        self.pokemons.append(current_pokemon)
        return f"Caught {current_pokemon.name} with health {current_pokemon.health}"

    def release_pokemon(self, pokemon_name):
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        string_to_return = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for p in self.pokemons:
            string_to_return += f"- {p.pokemon_details()}\n"
        return string_to_return
