from pokemon import Pokemon
class Trainer:
    def __init__(self, name:str,money:int, pokemons:list[Pokemon]):
        self.name = name
        self.money = money
        self.pokemons = pokemons
        # inventory
        self.inventory = {'pokeballs':0,'potions':0}
    def test_print(self):
        print("name : {}\nmoney : {}".format(self.name, self.money))
        i = 1
        for pokemon in self.pokemons:
            print("pokemon {}".format(i))
            pokemon.test_print()
