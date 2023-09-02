import json
import requests
import time
from random import randint
import pandas as pd
import math
LIMIT = 10

url_heroes = f"https://api.opendota.com/api/players/883661889/heroes"
r_heroes = requests.get(url_heroes)
data_heroes = json.loads(r_heroes.text)
# print(json.dumps(r_heroes.text))
r3 = open('InternalTools\heroInfo.json')
data3 = json.load(r3)
# "hero_id": "string",
# "last_played": 0,
# "games": 0,
# "win": 0,
# "with_games": 0,
# "with_win": 0,
# "against_games": 0,
# "against_win": 0

heroes_list = []
for hero in data_heroes:

    # for x in self.json_hero_info_data:
    #     if game['hero_id'] == self.json_hero_info_data[x]['id']:
    #         hero_name = self.json_hero_info_data[x]['name']
    
    hero_id = hero['hero_id']
    games = hero['games']
    win = hero['win']
    
    if games > 0:
        wrt = win/games * 100
        wr = str(round(wrt, 2)) + "%"
    else:
        wr = "00.00%"
    hero_info_data = open('Test2\static\JSON\heroInfo.json')
    json_hero_info_data = json.load(hero_info_data)

    for x in json_hero_info_data:
        if int(hero_id) == json_hero_info_data[x]['id']:
            hero_name = json_hero_info_data[x]['name']
        
    heroes_info = {
        'hero_id': hero_id,
        'hero_name': hero_name,
        'games': games,
        'win': win,
        'wr': wr
        
    }
    if len(heroes_list) < LIMIT:
        heroes_list.append(heroes_info)
    else:
        break
        

dotadfHeroes = pd.DataFrame(heroes_list) 
# print(heroes_list)
print(dotadfHeroes)
# dotadfHeroes.to_json('Test2\static\JSON\mostplayed_info.json', orient='records', indent=2)