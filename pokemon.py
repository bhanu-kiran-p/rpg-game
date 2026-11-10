from type import Type


class Pokemon(Type):
    def __init__(self, name, type, level, xp, hp, moves):
        self.name = name
        self.type = type
        self.level = level
        self.xp = xp
        self.hp = hp
        self.moves = moves

    def get_type(self):
        return self.type

    def set_weakness(self, weakness):
        self.type.weakness = weakness

    def test_print(self):
        print(
            "name : {}\ntype :{}\nlevel : {}\nxp : {}\nhp : {}".format(
                self.name, self.type, self.level, self.xp, self.hp
            )
        )
        print("--moves--")
        for move in self.moves:
            print("-{}".format(move))
