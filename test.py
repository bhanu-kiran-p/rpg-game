from pokemon import Pokemon
from trainer import Trainer
from type import Type
from moves import Move

# basic types setting
grass = Type("grass")
fire = Type("fire")
water = Type("water")
normal = Type("normal")
grass.set_weakness(fire)
fire.set_weakness(water)
water.set_weakness(grass)

# test moves settings
tailwhip = Move("tailwhip", normal, 20, 20, 0)
leafblade = Move("leafblade", grass, 30, 20, 1)
tackle = Move("tackle", normal, 20, 10, 0)
leechseed = Move("leechseed", grass, 30, 4, 10)
watergun = Move("watergun", water, 30, 5, 0)
headsmash = Move("headsmash", normal, 30, 7, 0)
bubble = Move("bubble", water, 20, 12, 0)
flamethrower = Move("flamethrower", fire, 30, 10, 0)
ember = Move("ember", fire, 10, 12, 0)
flameburst = Move("flameburst", fire, 10, 20, 6)

# test pokemon settings
bulbasaur_moves = [tailwhip, leafblade, tackle, leechseed]
squirtle_moves = [tackle, watergun, headsmash, bubble]
chramander_moves = [tackle, flameburst, flamethrower, ember]
bulbasaur = Pokemon("bulbasaur", grass, 1, 0, 100, bulbasaur_moves)
squirtle = Pokemon("squirtle", water, 1, 0, 110, squirtle_moves)
chramander = Pokemon("charmender", fire, 1, 0, 99, chramander_moves)

# test trainer settings
ash_pokemon = [bulbasaur, squirtle, chramander]
ash = Trainer("ash", 1200, ash_pokemon)
ash.test_print()
