import random
import time


class Character:
    def __init__(self, type=''):
        super().__init__()
        self.initiative = 0
        self.health = 0
        self.attack = 0
        self.dexterity = 0
        self.type = type

    def roll_dice(self, no_of_dice):
        dice_score = 0
        print(f"*rolls dice*")
        time.sleep(1)

        for roll in range(no_of_dice):
            dice = random.randint(1, 6)
            print(dice)
            dice_score += dice
            time.sleep(0.1)
        print(f"result: {dice_score}")
        time.sleep(0.5)
        return dice_score

    def check_hit(self, dice_score, dmg=1):
        if dice_score < self.dexterity:
            print("miss!")
        else:
            if dmg == 2:
                msg = "critical hit! x2 damage"
            else:
                msg = "hit!"
            print(msg)
            self.health -= dmg


class Player(Character):
    def __init__(self, type, points=0):
        super().__init__(type)
        self.points = points
        self.ability = ''
        self.generate_class()

    def generate_class(self):
        # (initative, health, attack, dexterity)
        types = {"Knight": (5, 9, 6, 4, "shield block"), "Wizard": (
            6, 4, 9, 5, "light beam"), "Thief": (7, 5, 5, 7, "critical hit")}

        self.initiative, self.health, self.attack, self.dexterity, self.ability = types[
            self.type]


class Monster(Character):
    def __init__(self, type):
        super().__init__(type)
        self.generate_class()

    # sets stats according to type
    def generate_class(self):
        types = {"Spider": (7, 1, 2, 3), "Skeleton": (
            4, 2, 3, 3), "Orc": (6, 3, 4, 4), "Troll": (2, 4, 7, 2)}

        self.initiative = types[self.type][0]
        self.health = types[self.type][1]
        self.attack = types[self.type][2]
        self.dexterity = types[self.type][3]


if __name__ == "__main__":
    player = Player(type="Thief")
    monster = Monster(type="Spider")
    print(f"result: {player.roll_dice(player.initiative)}")
    print(f"result: {monster.roll_dice(monster.initiative)}")
