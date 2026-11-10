from type import Type
class Move:
    def __init__(self, name:str,type:Type, atk:int, damage:int, heal:int):
        self.name = name
        self.type = type
        self.atk = atk
        self.damage = damage
        self.heal = heal
    def __str__(self):
        return self.name