#This should be returning details about a specific match ID
import json
import requests
import time
from random import randint
import pandas as pd

# --- Steam ID's for testing purposes ---
# 883661889
# 80037375
# 163881259
# 97203194
# --- Sample endpoints ---
# wl
# recentMatches
# heroes
# wordcloud
#Base URL
#baseurl = f'https://api.opendota.com/api/'

steam_id = input("Steam ID:")

baseurl = f'https://api.opendota.com/api/'
player = f'players/{steam_id}/'
endpoint = f''
heroInfoData = open('Test 1\heroInfo.json')
jsonData = json.load(heroInfoData)


def main_request(baseurl, player, endpoint):
    r = requests.get(baseurl + player + endpoint)
    data = r.json()

def get_recentMatches(response):
    endpoint = f'recentMatches/'
    recentMatches = requests.get(baseurl + player + endpoint)
    data_recentMatches = recentMatches.json()

    game_list = []
    for game in data_recentMatches:
        match_id = game['match_id']
        duration = game['duration']
        #hero_id = game['hero_id']
        kills = game['kills']
        deaths = game['deaths']
        assists = game['assists']
        party_size = game['party_size']

        #Dtermines what team the player is on
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

        for x in jsonData:
            if game['hero_id'] == jsonData[x]['id']:
                hero_name = jsonData[x]['name']
        
        match_info = {
            'match id': match_id,
            'duration': time.strftime("%H:%M:%S", time.gmtime(duration)), #converts the time from seconds to minutes (and seconds) in standard format
            'hero name': hero_name,
            'kills': kills,
            'deaths': deaths,
            'assists': assists,
            'party size': party_size,  
            'team': team,   
            'result': result
        }
        game_list.append(match_info)

    return game_list


def get_user(response):
    endpoint = f''
    user = requests.get(baseurl + player + endpoint)
    data_user = user.json()
    print(data_user['profile']['personaname'])

def parse_json(response):
    for items in get_recentMatches(data):
        return items
        

mainlist = []
data = main_request(baseurl, player, endpoint)
get_user(data)
mainlist.extend(get_recentMatches(data))

dotadf = pd.DataFrame(mainlist) 
#print(dotadf)
dotadf.to_json('Test 1\matches_recent.json', orient='records', indent=2) 