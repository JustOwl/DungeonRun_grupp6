import json
import time
FILEPATHJSON = "data/users.json"

# Function for taking last added values in users.json while player exits game


class User:
    def __init__(self, user):
        self.user = user

    def update_selected_user_points(self, collected_points):
        with open("data/users.json", "r+") as f:
            data = json.load(f)
        current_points = data["users"][self.user]["points"]
        data["users"][self.user]["points"] = current_points + collected_points
        with open("data/users.json", "w") as f:
            f.write(json.dumps(data, indent=4))

    def player_dead(self):
        with open("data/users.json") as f:
            stats = json.load(f)
            player_name = [x['name'] for x in stats["users"]]
            player_class = [x['class'] for x in stats["users"]]
            player_points = [x['points'] for x in stats["users"]]
            print(f''' 
            
            You are dead. Bad luck :(
                
            STATS
            USERNAME: {player_name[self.user]}
            CLASS: {player_class[self.user]}
            POINTS: {player_points[self.user]}        
            ''')

    def player_exit(self):
        with open("data/users.json") as f:
            stats = json.load(f)
            player_name = [x['name'] for x in stats["users"]]
            player_class = [x['class'] for x in stats["users"]]
            player_points = [x['points'] for x in stats["users"]]
            print(f''' 
            You have exited the game, well played!
                
            STATS
            USERNAME: {player_name[self.user]}
            CLASS: {player_class[self.user]} 
            POINTS: {player_points[self.user]}
                ''')


# Function for taking last added values from users.json while player dies


def player_dead(self):
    with open("data/users.json") as f:
        stats = json.load(f)
        player_name = [x['name'] for x in stats["users"]]
        player_class = [x['class'] for x in stats["users"]]
        player_points = [x['points'] for x in stats["users"]]
        print(f''' 
        
        You are dead. Bad luck :(
            
        STATS
        USERNAME: {player_name[self.user]}
        CLASS: {player_class[self.user]}
        POINTS: {player_points[self.user]}        
        ''')


# Function for adding user to users.json


def write_json(new_data, fpjson):
    with open(fpjson, 'r+') as file:
        file_data = json.load(file)
        file_data["users"].append(new_data)
        file.seek(0)
        print(file_data)
        json.dump(file_data, file, indent=4)


# Function for creating new user in menu


def char_creation(player_class=""):
    data_dict = {"name": "", "class": "", "points": 0}
    data_input = input("please enter username: ")
    with open("data/users.json") as f:
        stats = json.load(f)
        players = [x['name'] for x in stats["users"]]
    if data_input in players:
        print("Username already exists... ")
        time.sleep(0.5)
        return char_creation()
    else:    
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


# Choose character to view stats from
# Y = User position in list of users

def view_stats(y):
    with open(FILEPATHJSON) as f:
        stats = json.load(f)
        player_name = [x['name'] for x in stats["users"]]
        player_class = [x['class'] for x in stats["users"]]
        player_points = [x['points'] for x in stats["users"]]
        print(f'''       
        STATS
        USERNAME: {player_name[y]}
        CLASS: {player_class[y]}
        POINTS: {player_points[y]}        
        ''')

# Function for saving collected treasures to player
# User = position in list of users
