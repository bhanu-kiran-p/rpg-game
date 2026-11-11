import csv
from pokemon import Pokemon
from type import Type

class PokemonRecords():
    def __init__(self):
        # adding the type hinting
        self.pokemon_records:dict[int, Pokemon] = {}
    def add_pokemon(self, pokemon:Pokemon):
        self.pokemon_records[pokemon.id] = pokemon
    def load_csv(self, filepath:str):
        with open(filepath , mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id = int(row['id'])
                name = row['Name']
                type1 = Type(row['Type 1'])
                type2 = Type(row['Type 2'])
                max_hp = int(row['HP'])
                level = 0
                xp = 0
                moves = [None]
                pokemon = Pokemon(name, id,type1, type2,level, xp,max_hp,moves)
                self.add_pokemon(pokemon)
    def test_print(self):
        for id, pokemon in self.pokemon_records.items():
            print("{}:{}".format(id, pokemon.name))