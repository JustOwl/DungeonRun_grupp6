import map_handler
import menu_functions
import characters


def main(player, user, corner_int=1, map_size=4):
    room_ls = map_handler.make_map(map_size)
    current_map = map_handler.Map(room_ls, map_size, player)
    player_pos = pick_corner(corner_int, map_size)
    map_movement = Movement(player_pos, map_size, user)
    current_map.draw_map_easy(player_pos)
    map_handler.gen_random(room_ls)
    while True:
        print(
            f"Health: {str(player.health)} | Class: {str(player.type)} | Points: {str(current_map.points)}")
        try:
            p_in = input("Type in cardinal direction(N/S/E/W): ")
            if (p_in.lower() == "n"):  # Go North on the map
                if map_movement.move_char(-1, 0, current_map, room_ls):
                    continue
                else:
                    print("That seems to be outside the map, try again")

            if (p_in.lower() == "s"):  # Go South on the map
                if map_movement.move_char(1, 0, current_map, room_ls):
                    continue
                else:
                    print("That seems to be outside the map, try again")

            if (p_in.lower() == "e"):  # Go East on the map
                if map_movement.move_char(1, 1, current_map, room_ls):
                    continue
                else:
                    print("That seems to be outside the map, try again")

            if (p_in.lower() == "w"):  # Go West on the map
                if map_movement.move_char(-1, 1, current_map, room_ls):
                    continue
                else:
                    print("That seems to be outside the map, try again")
        except Exception as e:
            print(e)
            print("Wrong input")

class Movement:
    def __init__(self, player_pos, map_size, user):
      self.player_pos = player_pos
      self.last_pos = ()
      self.new_pos  = ()
      self.map_size = map_size
      self.user = user

    def move_char(self,move_value : int, v_or_h : int, current_map, room_ls,):
        # v_or_h is if its vertical or horizontal movement, 0 = vertical and 1 = horizontal
        # it has to do with tuple index
        if v_or_h == 0:
            if self.player_pos[v_or_h]+move_value in range(self.map_size):
                self.last_pos = (self.player_pos[0], self.player_pos[1])
                self.new_pos  = (self.player_pos[0]+move_value, self.player_pos[1])
                if map_handler.next_round(current_map, room_ls, self.user, self.map_size, self.player_pos,):
                    current_map.draw_map_easy(self.new_pos)
                    self.player_pos = self.new_pos
                    return True
                else:
                    current_map.draw_map_easy(self.last_pos)
                    self.player_pos = self.last_pos
            else:
                return False
        else:
            if self.player_pos[v_or_h]+move_value in range(self.map_size):
                self.last_pos = (self.player_pos[0], self.player_pos[1])
                self.new_pos  = (self.player_pos[0], self.player_pos[1]+move_value)
                if map_handler.next_round(current_map, room_ls, self.user, self.map_size, self.player_pos):
                    current_map.draw_map_easy(self.new_pos)
                    self.player_pos = self.new_pos
                    return True
                else:
                    current_map.draw_map_easy(self.last_pos)
                    self.player_pos = self.last_pos
            else:
                return False

def pick_corner(corner, size):
    # 1     2
    #   map
    # 3     4
    if corner == 1:
        return (0, 0)
    elif corner == 2:
        return (0, size-1)
    elif corner == 3:
        return (size-1, 0)
    elif corner == 4:
        return (size-1, size-1)


if __name__ == "__main__":
    main()
