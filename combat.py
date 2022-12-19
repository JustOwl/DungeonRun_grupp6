import time
import characters
import os


def check_initative(player, monster):
    print("checking initative score.. ")
    time.sleep(1)
    print("Your turn: ")
    input("roll dice")
    player_result = player.roll_dice(player.initiative)
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("checking initative score.. ")
    print(f"{monster.type}s turn: ")
    monster_result = monster.roll_dice(monster.initiative)

    if player_result > monster_result:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You begin the fight!")
        time.sleep(3)
        return "Your"
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{monster.type} begins the fight!")
        time.sleep(3)
        return monster.type


def combat_loop(player, monster):
    monster_turn = 1
    current_turn = check_initative(player, monster)
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("combat mode")
        print(
            f"Your health: {player.health} | {monster.type}s health: {monster.health}")
        print(f"{current_turn}s turn: ")
        if current_turn == "Your":
            print("What do you want to do?")
            print("1. Attack monster")
            print("2. Flee")
            answer = input("Answer: ")
            if answer == "1":
                monster.check_hit(player.roll_dice(player.attack))
                time.sleep(1)
                if monster.health <= 0:
                    print(f"You slayed the {monster.type}")
                    time.sleep(2)
                    return "won"
                current_turn = monster.type

            elif answer == "2":
                if player.ability == "light beam":
                    pass
                print("You successfully fled to previous room")
                time.sleep(2)
                return "fled"
        else:
            if player.ability == "shield block" and monster_turn == 1:
                print("blocked!")
            else:
                player.check_hit(monster.roll_dice(monster.attack))
            monster_turn += 1
            time.sleep(1)
            current_turn = "Your"
            if player.health <= 0:
                print("You died")
                time.sleep(2)
                return "lost"
        time.sleep(0.5)
        # runs cls if os is windows. runs clear if unix-based (osx, linux)
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    player = characters.Player(type="Knight")
    monster = characters.Monster(type="Troll")
    combat_loop(player, monster)
