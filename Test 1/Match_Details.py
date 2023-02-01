#This should be returning details about a specific match ID
import json
import requests
import time
from random import randint

# Steam ID's for testing purposes
# 883661889
# 80037375
# 163881259
# 97203194
#Base URL
#baseurl = f'https://api.opendota.com/api/'

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

r3 = open('hero_info.json',)
data3 = json.load(r3)

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
    kills = game['kills']
    deaths = game['deaths']
    assists = game['assists']
    party_size = game['party_size']
    
    #Determines what team the player is on
    if game['player_slot'] < 128:
        onRadiant = True
        team = 'Radiant'
    else:
        onRadiant = False
        team = 'Dire'
    
    #Determines if the player won the game
    if game['radiant_win'] == True and onRadiant == True:
        result = 'Won Match'
    elif game['radiant_win'] == False and onRadiant == False:
        result = 'Won Match'
    else:
        result = 'Lost Match'

    for x in data3:
        if game['hero_id'] == data3[x]['id']:
            hero_name = data3[x]['name']
        
    

    match_info = {
        'match_id': match_id,
        'duration': time.strftime("%H:%M:%S", time.gmtime(duration)), #converts the time from seconds to minutes (and seconds) in standard format
        'hero name': hero_name,
        'kills': kills,
        'deaths': deaths,
        'assists': assists,
        'party_size': party_size,  
        'team': team,   
        'result': result
    }
    game_list.append(match_info)

print(user_list)

for i in game_list:
    print(i)


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