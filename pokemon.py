from type import Type
from moves import Move


class Pokemon:
    # include the threshold xp for level up later
    def __init__(
        self, name: str, type: Type, level: int, xp: int, max_hp: int, moves: list[Move]):
        self.name = name
        self.type = type
        self.level = level
        self.xp = xp
        self.current_hp = max_hp
        self.max_hp = max_hp
        self.moves = moves

    def get_type(self):
        return self.type

    def test_print(self):
        print(
            "name : {}\ntype :{}\nlevel : {}\nxp : {}\nhp : {}".format(
                self.name, self.type, self.level, self.xp, self.hp
            )
        )
        print("--moves--")
        for move in self.moves:
            print("-{}".format(move))
