class Map:
    def __init__(self, room_ls : list, size : int):
      self.rooms = room_ls
      self.size  = size
      self.player_location = ()
      self.current_pos = ()

    def draw_map(self, player_location: tuple):
        self.player_location = player_location
        player_icon = "[X]"
        temp = ""
        row  = 0

        for i in range(self.size):
            for j in range(self.size):
                temp += str(self.rooms[j+row]) # This is for the cordinates of the rooms
                                               # Might not get used

            if (player_location[0] == i): # Get the row where the player is
                for j in range(self.size):
                    if(player_location[1] == j): # Get the collumn where the player is
                        print(" [] "*player_location[1], player_icon, " [] "*(self.size-(player_location[1]+1)))
                        # Some basic math to print where the player is and fill in the empty spaces to the left/right
            else: # All rows the player is not in
                row += self.size
                print(" [] "*self.size)
                temp = ""

    def current_room(self):
        for i in range(len(self.rooms)):
            if(self.rooms[i].location == self.player_location):
                print(self.player_location, i)
                self.current_pos = (self.rooms[i].location, i)
                return i # Returns id of current room

    def check_room(self):
        # fake code
        # if(self.current_pos[0].has_monster = True): ...

        # TODO Check current room and see if it has:
        # A: any monsters and if so start combat
        # B: any treasure and if so pick it up and add to score
        # C: None of the above and ask the player to move on
        pass 


class Room:
    def __init__(self, cordinate: tuple):
      self.location = cordinate

    def moster_spawn(): # TODO Use values from the moster classes to determine if there should be a monster here or not
        pass

    def treasure_spawn(): # TODO Use values from the treasure classes to determine if there should be a monster here or not
        pass

    def __str__(self) -> str:
       return str(self.location)


def main():
    map_size = 4  # This should be sent from the meny
    rooms    = [] # List with all instances of rooms for later use

    for i in range(map_size):
        for j in range(map_size):
            rooms.append(Room((i,j)))

    current_map = Map(rooms,map_size)
    current_map.draw_map((1,2)) # The value given is the players current position, could be sent from other scripts
                                # Format should be: tuple(int, int), must be within the bounds of the map or it wont show
    current_map.current_room()
    current_map.check_room()

if __name__ == "__main__":
    main()