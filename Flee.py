import characters
import os
import random
import time
from random import choices

def check_initative(player, monster):
    print("checking initative score.. ")
    time.sleep(0)
    print("Your turn: ")
    input("roll dice")
    player_result = player.roll_dice(player.initiative)
    time.sleep(0)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("checking initative score.. ")
    print(f"{monster.type}s turn: ")
    monster_result = monster.roll_dice(monster.initiative)

    if player_result > monster_result:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You begin the fight!")
        time.sleep(0)
        return "Your"
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{monster.type} begins the fight!")
        time.sleep(0)
        return monster.type


def trying_to_flee(player, monster):
    player.chance  = int(player.dexterity*10)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.5)
    if player.type == "Wizard":
       i = (choices(population = ["Fled","You couldn't flee from the fight."], weights=[0.8, 0.2])[0]) #Har alltid 80% chans att fly från striden pga specialförmåga
       print("Your" ,player.type, "have",(player.chance+30),"%"" ""chance to flee from the fight.")
       time.sleep(1)
       print()
       print(i)
    elif player.type == "Knight":
        i = (choices(population = ["Fled","You couldn't flee from the fight."], weights=[0.4, 0.6])[0]) #40% chans att fly från striden
        print("Your" ,player.type, "have",(player.chance),"%"" ""chance to flee from the fight.")
        time.sleep(1)
        print()
        print(i)
    elif player.type == "Thief":
        i = (choices(population = ["Fled","You couldn't flee from the fight."], weights=[0.7, 0.3])[0]) #70% chans att fly striden
        print("Your" ,player.type, "have",(player.chance),"%"" ""chance to flee from the fight.")
        time.sleep(1)
        print()
        print(i)
    if i == "Fled":
        print()
        time.sleep(1)
        print("You are getting back to previous room.")
        print()
    else:
        print()
        time.sleep(1)
        print("It's monsters turn to attack!")
        print()






def combat_loop(player, monster):
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
                    break
                current_turn = monster.type

            elif answer == "2":
                trying_to_flee(player, monster)
                time.sleep(1)
                break
        else:
            player.check_hit(monster.roll_dice(monster.attack))
            time.sleep(1)
            current_turn = "Your"
            if player.health <= 0:
                print("You died")
                time.sleep(2)
                break
        time.sleep(0.5)
        # runs cls if os is windows. runs clear if unix-based (osx, linux)
        os.system('cls' if os.name == 'nt' else 'clear')




if __name__ == "__main__":
    player = characters.Player(type="Knight")
    monster = characters.Monster(type="Troll")
    monster.health = 1
    combat_loop(player, monster)
