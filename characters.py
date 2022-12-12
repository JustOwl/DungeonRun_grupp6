class Character:
    def __init__(self, type=''):
        super().__init__()
        self.initiative = 0
        self.health = 0
        self.attack = 0
        self.dexterity = 0
        self.type = type


class Player(Character):
    def __init__(self, name, type, points=0):
        super().__init__(type)
        self.points = points
        self.name = name
        self.ability = ''
        self.generate_class()

    def generate_class(self):
        pass


class Monster(Character):
    def __init__(self, type):
        super().__init__(type)
        self.probability = 0
        self.generate_class()

    # sets stats and probability according to class
    def generate_class(self):
        pass
