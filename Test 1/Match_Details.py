#This should be returning details about a specific match ID

import json
import requests

url = "https://api.opendota.com/api/players/883661889/recentMatches"

r = requests.get(url)
data = json.loads(r.text)

game_list = []

for game in data:
    match_id = game['match_id']
    duration = game['duration']
    hero_id = game['hero_id']
    kills = game['kills']
    deaths = game['deaths']
    assists = game['assists']
    party_size = game['party_size']
    
    match_info = {
        'match_id': match_id,
        'duration': duration,
        'hero_id': hero_id,
        'kills': kills,
        'deaths': deaths,
        'assists': assists,
        'party_size': party_size
        
        
    }
    game_list.append(match_info)
    
    

print("XXXXX's Recent Matches")
print(game_list)


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