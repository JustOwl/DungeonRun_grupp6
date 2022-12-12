import json

# Function for taking last added values in users.json while player exits game

FILEPATHJSON = "data/users.json"


def player_exit(fpjson):
    with open(fpjson) as f:
        stats = json.load(f)
        player_name = [x['name'] for x in stats["users"]]
        player_class = [x['class'] for x in stats["users"]]
        player_points = [x['points'] for x in stats["users"]]
        print(f''' 
        You have exited the game, well played!
            
        STATS
        USERNAME: {player_name[-1]}
        CLASS: {player_class[-1]} 
        POINTS: {player_points[-1]}
            ''')


# Function for taking last added values from users.json while player dies


def player_dead(fpjson):
    with open(fpjson) as f:
        stats = json.load(f)
        player_name = [x['name'] for x in stats["users"]]
        player_class = [x['class'] for x in stats["users"]]
        player_points = [x['points'] for x in stats["users"]]
        print(f''' 
        
        You are dead. Bad luck :(
            
        STATS
        USERNAME: {player_name[-1]}
        CLASS: {player_class[-1]}
        POINTS: {player_points[-1]}        
        ''')


# Function for adding user to users.json


def write_json(new_data, fpjson):
    with open(fpjson, 'r+') as file:
        file_data = json.load(file)
        file_data["users"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


# Function for creating new user in menu


def char_creation(player_class = ""):
    data_dict = {"name": "", "class": "", "points": 0}
    data_input = input("please enter username: ")
    data_input_char = player_class
    data_dict["name"] = (data_input)
    data_dict["class"] = (data_input_char)
    print("user added")
    return data_dict


# Function for updating last user added points


def update_user_points(collected_points, fpjson):
    with open(fpjson, "r+") as f:
        data = json.load(f)
    current_points = data["users"][-1]["points"]
    data["users"][-1]["points"] = current_points + collected_points
    with open(fpjson, "w") as f:
        f.write(json.dumps(data, indent=4))


#update_user_points(collected_points=10, fpjson=FILEPATHJSON)
#write_json(char_creation(), FILEPATHJSON)
#update_user_points(collected_points=7, fpjson=FILEPATHJSON)

