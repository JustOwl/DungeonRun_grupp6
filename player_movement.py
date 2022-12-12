import map_handler


def main(corner_int = 1, map_size = 4):
    current_map = map_handler.make_map(map_size)
    player_pos = pick_corner(corner_int, map_size)
    map_handler.next_round(current_map,map_size,player_pos)
    while True:
        p_in = input("Type in cardinal direction(N/S/E/W): ")
        if(p_in.lower() == "n"): # Go North on the map
            if player_pos[0]-1 in range(map_size):
                player_pos = (player_pos[0]-1,player_pos[1])
                map_handler.next_round(current_map,map_size,player_pos)
            else:
                print("That seems to be outside the map, try again")

        if(p_in.lower() == "s"): # Go South on the map
            if player_pos[0]+1 in range(map_size):
                player_pos = (player_pos[0]+1,player_pos[1])
                map_handler.next_round(current_map,map_size,player_pos)
            else:
                print("That seems to be outside the map, try again")

        if(p_in.lower() == "e"): # Go East on the map
            if player_pos[1]+1 in range(map_size):
                player_pos = (player_pos[0],player_pos[1]+1)
                map_handler.next_round(current_map,map_size,player_pos)
            else:
                print("That seems to be outside the map, try again")

        if(p_in.lower() == "w"): # Go West on the map
            if player_pos[1]-1 in range(map_size):
                player_pos = (player_pos[0],player_pos[1]-1)
                map_handler.next_round(current_map,map_size,player_pos)
            else:
                print("That seems to be outside the map, try again")

def pick_corner(corner ,size):
    # 1     2
    #   map
    # 3     4
    if   corner == 1:
        return (0,0)
    elif corner == 2:
        return (0,size-1)
    elif corner == 3:
        return (size-1,0)
    elif corner == 4:
        return (size-1,size-1)

if __name__ == "__main__":
    main()