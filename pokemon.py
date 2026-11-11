from type import Type
from moves import Move


class Pokemon:
    # include the threshold xp for level up later
    def __init__(
        self, name: str,id:int, type1: Type,type2:Type, level: int, xp: int, max_hp: int, moves: list[Move]
    ):
        self.name = name
        self.id = id
        self.type1 = type1
        self.type2 = type2
        self.level = level
        self.xp = xp
        self.current_hp = max_hp
        self.max_hp = max_hp
        self.moves = moves

    def get_type(self):
        return self.type

    def test_print(self):
        print(
            "name : {}\nid : {}\ntype :{}\nlevel : {}\nxp : {}\nmax hp : {}".format(
                self.name,self.id,self.type, self.level, self.xp, self.max_hp
            )
        )
        print("--moves--")
        for move in self.moves:
            print("-{}".format(move))