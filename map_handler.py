import random
import characters
import combat


class Map:
    def __init__(self, room_ls: list, size: int, player):
        self.rooms = room_ls
        self.size = size
        self.player_location = ()
        self.current_pos = ()
        self.player = player

    def draw_map_easy(self, player_location: tuple = (0, 0)):
        row = 0
        self.player_location = player_location
        for i in range(self.size):  # Rows
            temp_ls = []
            for j in range(self.size):  # Collums in the row
                temp_ls.insert(
                    self.rooms[j+row].location[1], self.rooms[j+row].has_visited)
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

    def check_room(self):
        c_room = self.current_room(self.player_location)

        if self.rooms[c_room].has_exit == True:
            pass
            # TODO Call the function that asks if the player wants to exit or not

        if self.rooms[c_room].monster != "":
            print("There is a monster here")
            monster = characters.Monster(type=self.rooms[c_room].monster)
            result = combat.combat_loop(self.player, monster)
            if result == "won":
                self.rooms[c_room].monster = ""
            elif result == "fled":
                # TODO put player in previous room if fled
                pass
            else:
                # TODO add game ending if dead
                pass
            # TODO Call start of combat with c_room.monster as the type of monster to fight
            # When the combat loop exits it should automaticaly return here (i think)

        # TODO Call the function that saves loot
        # The function might want to look like: add_loot(c_room.treasure : int)


class Room:
    def __init__(self, cordinate: tuple, has_exit: bool = False, has_visited: str = "[?]"):
        self.location = cordinate
        self.monster = ""
        self.treasure = 0
        self.has_exit = has_exit
        self.has_visited = has_visited

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

    for i in rooms:
        if (i == exit_room):
            i.has_exit = True
        else:
            i.monster_spawn()
            i.treasure_spawn()


def save_room(rooms: list, room_id: int):
    rooms[room_id].has_visited = "[ ]"
    rooms[room_id].monster = ""
    rooms[room_id].treasure = 0


def next_round(map, rooms: list, map_size=4, player_location=(0, 0)):
    map.draw_map_easy(player_location)
    map.check_room()
    save_room(rooms, map.current_room(player_location))

# Used for testing


def main():
    rooms = make_map()
    _map = Map(rooms, 4, characters.Player(type="Knight"))
    while True:
        next_round(_map, rooms)
        input("Press enter for next round")


if __name__ == "__main__":
    main()
