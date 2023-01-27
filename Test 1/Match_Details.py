#This should be returning details about a specific match ID
import json
import requests
import time
from random import randint

# Steam ID's for testing purposes
# 883661889
# 80037375
# 163881259


steam_id = input('please enter player steam id: ')
steam_id = int(steam_id)

#This gets the imformation about the player itself, no game data
url1 = f'https://api.opendota.com/api/players/{steam_id}'
r1 = requests.get(url1)
data1 = json.loads("[" + r1.text + "]") #added brackets to treat it as an array

#this gets all game data
url2 = f'https://api.opendota.com/api/players/{steam_id}/recentMatches'
r2 = requests.get(url2)
data2 = json.loads(r2.text)

#user_list is a array of 1 object, allows for easy display of player profile
user_list = []
for user in data1:
    profile_name = user['profile']['personaname']
    profile_pfp = user['profile']['avatarfull']

    user_info = {
        'username': profile_name,
        'pfp': profile_pfp,
    }
    user_list.append(user_info)

#array of a collection of games, stats vary depending on what is going to be shown
game_list = []
for game in data2:
    match_id = game['match_id']
    duration = game['duration']
    hero_id = game['hero_id']
    kills = game['kills']
    deaths = game['deaths']
    assists = game['assists']
    party_size = game['party_size']
    
    match_info = {
        'match_id': match_id,
        'duration': time.strftime("%M:%S", time.gmtime(duration)), #converts the time from seconds to minutes (and seconds) in standard format
        'hero_id': hero_id,
        'kills': kills,
        'deaths': deaths,
        'assists': assists,
        'party_size': party_size     
    }
    game_list.append(match_info)

print(user_list)
print(game_list[0])
print(game_list[1])


"""  This is code to get a random game out of the list
value = randint(0, len(game_list))    
try_this = game_list[value]
""" 
""" 
person_list = []

with open('json-data.json') as json_file:
    data = json.load(json_file)
    for item in data:
        name = item['name']
        index = item['index']

        person = {
            'name': name,
            'index': index,
        }

        person_list.append(person)

print(person_list) """