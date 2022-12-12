import characters
import end_game


def set_player_class():
    player_classes = {"1": "knight", "2": "wizard", "3": "thief"}
    while True:
        selected_class = input("choose your class (1-3): ")
        if selected_class in player_classes.keys():
            print(f"selected class is {player_classes[selected_class]}")
            return player_classes[selected_class]
        else:
            print("wrong input!")


def set_map_size():
    maps = {"1": 4, "2": 5, "3": 8}
    while True:
        room_size = input("select map size (1-3): ")
        if room_size in maps.keys():
            print(f"map size is {maps[room_size]}x{maps[room_size]}")
            return maps[room_size]
        else:
            print("wrong input!")


def select_option():
    while True:
        selected_option = input("select option (1-2): ")
        if selected_option == "1":
            return game_setup()
        elif selected_option == "2":
            return get_stats()
        else:
            print("wrong input!")


def game_setup():
    # check if player already exists
    # else, create new
    player_class = set_player_class()

    player = characters.Player(type=player_class)
    map_size = set_map_size()


<< << << < HEAD
player = characters.Player(type=player_class)
char = end_game.char_creation(player.type)
end_game.write_json(char, fpjson=end_game.FILEPATHJSON)
== == == =

>>>>>> > 0dd257786e5d5ee3c239db35223823a3aec5a819


def get_stats():
    # print stats
    pass


if __name__ == "__main__":
    select_option()
