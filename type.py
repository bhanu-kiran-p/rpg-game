class Type:
    def __init__(self, type):
        self.type = type
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness
    def test_print(self):
        print("{}".format(self.type))
    def __str__(self):
        return self.type