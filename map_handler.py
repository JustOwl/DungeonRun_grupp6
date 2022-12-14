import combat
import random
import characters
import menu_functions
import stats_functions


class Map:

    def __init__(self, room_ls: list, size: int, player):
        self.rooms = room_ls
        self.size = size
        self.player_location = ()
        self.current_pos = ()
        self.player = player
        self.points = 0

    def draw_map_easy(self, player_location: tuple = (0, 0)):
        row = 0
        self.player_location = player_location
        for i in range(self.size):  # Rows
            temp_ls = []
            for j in range(self.size):  # Collums in the row
                temp_ls.insert(
                    self.rooms[j+row].location[1], self.rooms[j+row].room_icon)
            if (player_location[0] == i):
                temp_ls[player_location[1]] = "[X]"
            print(''.join(temp_ls))
            row += self.size

    # Will not get used but did not want to delete
    # Hard mode, player needs to remember where they are
    def draw_map_hard(self, player_location: tuple):
        self.player_location = player_location
        player_icon = "[X]"
        row = 0

        for i in range(self.size):
            if (player_location[0] == i):  # Get the row where the player is
                for j in range(self.size):
                    # Get the collumn where the player is
                    if (player_location[1] == j):
                        print(" [] "*player_location[1], player_icon,
                              " [] "*(self.size-(player_location[1]+1)))
                        # Some basic math to print where the player is and fill in the empty spaces to the left/right
            else:  # All rows the player is not in
                row += self.size
                print(" [] "*self.size)

    def current_room(self, player_pos):
        for i in range(len(self.rooms)):
            if (self.rooms[i].location == player_pos):
                #print(self.player_location, i)
                self.current_pos = (self.rooms[i].location, i)
                return i  # Returns id of current room

    def check_room(self, user):
        c_room = self.current_room(self.player_location)

        if self.rooms[c_room].has_exit == True:
            exit_in = input(
                "You have found an exit! Do you wish to leave the map? (Y/N): ")
            try:
                if (exit_in.lower() == "y"):
                    user.update_selected_user_points(self.points)
                    stats = stats_functions.get_update_json()
                    user.player_exit(stats)
                    input("Press enter to return to main menu! ")
                    menu_functions.main_menu()
                elif (exit_in.lower() == "n"):
                    self.rooms[c_room].room_icon = "[E]"
                    return False
            except Exception:
                print("Wrong input")
        elif self.rooms[c_room].monster != "":
            print("There is a monster here")
            monster = characters.Monster(type=self.rooms[c_room].monster)
            result = combat.combat_loop(self.player, monster)
            if result == "won":
                self.rooms[c_room].monster = ""
                save_room(self.rooms, c_room)
                return True
            elif result == "fled":
                self.rooms[c_room].room_icon = "[!]"
                return False
            else:
                user.player_dead()
                input("Press enter to return to main menu! ")
                menu_functions.main_menu()
            # TODO Call start of combat with c_room.monster as the type of monster to fight
            # When the combat loop exits it should automaticaly return here (i think)
        if self.rooms[c_room].treasure != 0:
            print(
                f"There is a treasure here worth {self.rooms[c_room].treasure} points!")
            self.add_score(self.rooms[c_room].treasure)
            self.rooms[c_room].room_icon = "[ ]"
            self.rooms[c_room].treasure = 0
            return True
        else:
            self.rooms[c_room].room_icon = "[ ]"
            return True

    def add_score(self, points):
        self.points += points


class Room:
    def __init__(self, cordinate: tuple, has_exit: bool = False, room_icon: str = "[?]"):
        self.location = cordinate
        self.monster = ""
        self.treasure = 0
        self.has_exit = has_exit
        self.room_icon = room_icon

    def monster_spawn(self):
        spawn_chanse = random.randint(0, 100)

        if (spawn_chanse in range(51, 101)):
            self.monster = ""
        elif (spawn_chanse in range(0, 21)):
            self.monster = "Spider"
        elif (spawn_chanse in range(21, 36)):
            self.monster = "Skeleton"
        elif (spawn_chanse in range(36, 46)):
            self.monster = "Orc"
        elif (spawn_chanse in range(46, 51)):
            self.monster = "Troll"

    def treasure_spawn(self):
        spawn_chanse = random.randint(0, 100)

        if (spawn_chanse in range(0, 41)):
            self.treasure = 2
        elif (spawn_chanse in range(41, 61)):
            self.treasure = 6
        elif (spawn_chanse in range(61, 76)):
            self.treasure = 10
        elif (spawn_chanse in range(76, 86)):
            self.treasure = 14
        elif (spawn_chanse in range(86, 91)):
            self.treasure = 20

    def __str__(self) -> str:
        return str(self.location)


def make_map(map_size=4):
    rooms = []  # List with all instances of rooms for later use

    for i in range(map_size):
        for j in range(map_size):
            rooms.append(Room((i, j)))

    return rooms


def gen_random(rooms):
    exit_room = random.randint(0, len(rooms))

    for i in range(len(rooms)):
        if (i == exit_room):
            rooms[i].has_exit = True
        else:
            rooms[i].monster_spawn()
            rooms[i].treasure_spawn()


def save_room(rooms: list, room_id: int):
    rooms[room_id].room_icon = "[ ]"
    rooms[room_id].monster = ""


def next_round(map, rooms: list, user, map_size=4, player_location=(0, 0)):
    map.player_location = player_location
    if map.check_room(user):
        return True
    else:  # If the player flees then they return to the last room
        return False

# Used for testing


def main():
    rooms = make_map()
    _map = Map(rooms, 4, characters.Player(type="Knight"))
    while True:
        next_round(_map, rooms)
        input("Press enter for next round")


if __name__ == "__main__":
    main()
