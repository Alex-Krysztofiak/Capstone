#This should be returning details about a specific match ID
import json
import requests
import time
from random import randint
import pandas as pd
import math


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



steam_id = '883661889'

def set_steamid(steam_id):
    
    return steam_id

baseurl = f'https://api.opendota.com/api/'
player = f'players/{steam_id}/'
endpoint = f''
heroInfoData = open('.\Test1\heroInfo.json')
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

        for x in jsonData:
            if game['hero_id'] == jsonData[x]['id']:
                hero_name = jsonData[x]['name']
        
        match_info = {
            'match_id': match_id,
            'duration': time.strftime("%H:%M:%S", time.gmtime(duration)), #converts the time from seconds to minutes (and seconds) in standard format
            'hero_name': hero_name,
            'kills': kills,
            'deaths': deaths,
            'assists': assists,
            'party_size': party_size,  
            'team': team,   
            'result': result
        }
        game_list.append(match_info)

    return game_list



def get_user(response):
    endpoint = f''
    user = requests.get(baseurl + player + endpoint)
    data_user = user.json()

    endpoint2 = f'wl'
    user2 = requests.get(baseurl + player + endpoint2)
    data_user2 = user2.json() 

    print(data_user['profile']['personaname'])
    
    winrate = float(data_user2['win'] / float(data_user2['win'] + data_user2['lose']))
    winrate = winrate * 100
    finalWinrate = str(round(winrate, 2)) + "%"

    rankName = math.trunc(int(data_user['rank_tier'])/10)
    rankNumber = int(data_user['rank_tier'])%10

    profile_list = []
    player_info = {
        'name': data_user['profile']['personaname'],
        'id': data_user['profile']['steamid'],
        'avatar': data_user['profile']['avatarfull'],
        'rank_name': rankName,
        'rank_number': rankNumber,
        'rank_estimate': data_user['mmr_estimate']['estimate'],
        'wins': data_user2['win'],   
        'losses': data_user2['lose'], 
        'wr': finalWinrate,
    }
    profile_list.append(player_info)

    return profile_list



def parse_json(response):
    for items in get_recentMatches(data):
        return items
        

mainlist = []
profilelist = []
data = main_request(baseurl, player, endpoint)

    
# get_user(data)
mainlist.extend(get_recentMatches(data))
profilelist.extend(get_user(data))


dotadf = pd.DataFrame(mainlist) 
dotadfProfile = pd.DataFrame(profilelist) 
# print(dotadf)
# print(dotadfProfile)
dotadf.to_json('Test2\static\JSON\matches_recent.json', orient='records', indent=2)
dotadfProfile.to_json('Test2\static\JSON\PlayerProfile.json', orient='records', indent=2)