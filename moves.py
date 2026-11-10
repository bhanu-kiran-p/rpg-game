class Move:
    def __init__(self, name, atk, damage, heal):
        self.name = name
        self.atk = atk
        self.damage = damage
        self.heal = heal
    def __str__(self):
        return self.name