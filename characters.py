class Character:
    def __init__(self, type=''):
        super().__init__()
        self.initiative = 0
        self.health = 0
        self.attack = 0
        self.dexterity = 0
        self.type = type


class Player(Character):
    def __init__(self, type, points=0):
        super().__init__(type)
        self.points = points
        self.ability = ''
        self.generate_class()

    def generate_class(self):
        # (initative, health, attack, dexterity)
        types = {"knight": (5, 9, 6, 4, "shield block"), "wizard": (
            6, 4, 9, 5, "light beam"), "thief": (7, 5, 5, 7, "critical hit")}

        self.initiative, self.health, self.attack, self.dexterity, self.ability = types[
            self.type]


class Monster(Character):
    def __init__(self, type):
        super().__init__(type)
        self.generate_class()

    # sets stats according to type
    def generate_class(self):
        types = {"spider": (7, 1, 2, 3), "skeleton": (
            4, 2, 3, 3), "orc": (6, 3, 4, 4), "troll": (2, 4, 7, 2)}

        self.initiative = types[self.type][0]
        self.health = types[self.type][1]
        self.attack = types[self.type][2]
        self.dexterity = types[self.type][3]
