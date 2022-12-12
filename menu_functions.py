import characters
import end_game
import visual_menu
import os
import time
import player_movement


def set_player_class():
    player_classes = {"1": "knight", "2": "wizard", "3": "thief"}
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(visual_menu.MENU_CHARACTER_CHOICE)
        selected_class = input("choose your class (1-3): ")
        if selected_class in player_classes.keys():
            print(f"selected class is {player_classes[selected_class]}")
            return player_classes[selected_class]
        else:
            print("wrong input!")


def set_map_size():
    maps = {"1": 4, "2": 5, "3": 8}
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(visual_menu.MENU_MAP_CHOICE)
        room_size = input("select map size (1-3): ")
        if room_size in maps.keys():
            print(f"map size is {maps[room_size]}x{maps[room_size]}")
            return maps[room_size]
        else:
            print("wrong input!")


def set_start_pos():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(visual_menu.MENU_MAP_START_POS)
        positions = {"1": "top left", "2": "top right ",
                     "3": "bottom left", "4": "bottom right"}
        starting_pos = input("choose a starting position (1-4): ")
        if starting_pos in positions:
            print(f"starting postion is {positions[starting_pos]}")
            return int(starting_pos)
        else:
            print("wrong input!")


def game_setup():
    # check if player already exists
    # else, create new
    player_class = set_player_class()

    # creates player and generates all stats according to selected class
    player = characters.Player(type=player_class)
    player = characters.Player(type=player_class)
    char = end_game.char_creation(player.type)
    end_game.write_json(char, fpjson=end_game.FILEPATHJSON)
    player_movement.main(set_start_pos(),set_map_size())

#TODO Load char from jsons

def get_stats():
    # print stats
    pass


def main_menu():
    while True:
        # runs cls if os is windows. runs clear if unix-based (osx, linux)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(visual_menu.MENU_WELCOME_SCREEN)
        print(visual_menu.MENU_USER_SIGNUP)
        selected_option = input("select option (1-2): ")
        if selected_option == "1":
            return game_setup()
        elif selected_option == "2":
            return get_stats()
        else:
            print("wrong input!")
            time.sleep(1)


if __name__ == "__main__":
    main_menu()
