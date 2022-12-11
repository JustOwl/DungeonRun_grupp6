class Character:
    def __init__(self, type=''):
        self.initiative = 0
        self.health = 0
        self.attack = 0
        self.dexterity = 0


class Player(Character):
    def __init_subclass__(cls, self, name, points=0):
        self.points = points
        self.name = name
        self.ability = ''
        self.generate_class()
        return super().__init_subclass__()

    # sets stats and ability according to stats
    def generate_class(self):
        pass

# create subclass for every character class


class Monster(Character):
    def __init_subclass__(cls, self):
        self.probability = 0
        self.generate_class()
        return super().__init_subclass__()

    # sets stats and probability according to class
    def generate_class(self):
        pass

# create subclass for every type of monster
