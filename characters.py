class character:
    def __init__(self, type=''):
        self.initiative = 0
        self.health = 0
        self.attack = 0
        self.dexterity = 0


class player(character):
    def __init_subclass__(cls, self, points=0):
        self.points = points
        self.ability = ''
        self.generate_class()
        return super().__init_subclass__()

    def generate_class(self):
        pass

# create subclass for every character class


class monster(character):
    def __init_subclass__(cls, self):
        self.probability = 0
        self.generate_class()
        return super().__init_subclass__()

    def generate_class(self):
        pass

# create subclass for every type of monster
