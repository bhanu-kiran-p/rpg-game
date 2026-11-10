from pokemon import Pokemon
class Trainer:
    def __init__(self, name,money, pokemons):
        self.name = name
        self.money = money
        self.pokemons = pokemons
    def test_print(self):
        print("name : {}\nmoney : {}".format(self.name, self.money))
        i = 1
        for pokemon in self.pokemons:
            print("pokemon {}".format(i))
            pokemon.test_print()
