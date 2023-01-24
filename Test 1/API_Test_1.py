import requests 
import json

url = "https://api.opendota.com/api/matches/6984621064"
input_game_id = 6984621064

def jprint(obj):
    #creates a formatted sting of the python JSON object
    text = json.loads()
    print(text)

def getGameID(input_game_id):
    game = requests.get(f"https://api.opendota.com/api/matches/{input_game_id}").json()
    print(game)
    if "error" in game.keys():
        return "ERROR"  
    elif len(game["data"]) == 0:
        return "ERROR"
    else:
        return game["data"][0]["id"]



#Test run (working)


match_response = requests.get(url)

print(match_response.status_code)

match_data = match_response.json()

print(type(match_data))
print(len(match_data))
print(list(match_data.keys()))
print("")


