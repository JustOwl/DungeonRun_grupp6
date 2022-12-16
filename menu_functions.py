import characters
import stats_functions
import visual_menu
import os
import time
import player_movement
import json
import time


def set_player_class():
    player_classes = {"1": "Knight", "2": "Wizard", "3": "Thief"}
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
    char = stats_functions.char_creation(player.type)
    stats_functions.write_json(char, fpjson=stats_functions.FILEPATHJSON)
    player_movement.main(player, set_start_pos(), set_map_size())

# Gets already existing players and selects them for use


def get_info_users(stats, pos):
    char = {"name": "", "class": "", "points": 0}
    player_name = [x['name'] for x in stats["users"]]
    player_class = [x['class'] for x in stats["users"]]
    player_points = [x['points'] for x in stats["users"]]
    char["name"] = player_name[pos]
    char["class"] = player_class[pos]
    char["points"] = player_points[pos]
    return char


def select_char():
    try:
        with open("data/users.json") as f:
            char = {"name": "", "class": "", "points": 0}
            stats = json.load(f)
            print([x["name"] for x in stats["users"]])
            selected_user = input("Select user: ")
            pos = int(selected_user)
            pos = pos - 1
            char = get_info_users(stats, pos)
            print(f'''
            {visual_menu.WELCOME_BACK}
            User: {char["name"]} 
            Class: {char["class"]}
            Current points: {char["points"]}\n''')
            input("Press any key to continue")
            return (char)
    except IndexError:
        print("\n")
        print("Select user that exists. \n")
        return select_char()
# Skips steps where you create character since you´re using an already existing one


def game_start_from_char():
    char = select_char()
    player = characters.Player(type=char["class"], points=char["points"])
    player_movement.main(player, set_start_pos(), set_map_size())


def get_stats():
    try:
        with open("data/users.json") as f:
            stats = json.load(f)
            player_name = [x['name'] for x in stats["users"]]
            print(f'USERNAMES: {player_name}\n')
            selected_user = input(
                "select which player you would like to view stats from: ")
            pos = int(selected_user)
            pos = pos - 1
            stats_functions.view_stats(pos)
    except IndexError:
        print("Select a username that exists.")


def exit_game():
    confirm = input(
        "Are you sure you would like to exit the game?  Y/N \n").lower()
    if confirm == "n":
        return main_menu()
    elif confirm == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Wrong input, try again. ")
        return exit_game()


def main_menu():
    while True:
        # runs cls if os is windows. runs clear if unix-based (osx, linux)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(visual_menu.MENU_WELCOME_SCREEN)
        print(visual_menu.MENU_USER_SIGNUP)
        selected_option = input("select option (1-4): ")
        if selected_option == "1":
            return game_setup()
        elif selected_option == "2":
            return game_start_from_char()
        elif selected_option == "3":
            get_stats()
            input("Press any key to return to main menu ")
            return main_menu()
        elif selected_option == "4":
            exit_game()
            break
        else:
            print("wrong input!")
            time.sleep(1)


if __name__ == "__main__":
    main_menu()
