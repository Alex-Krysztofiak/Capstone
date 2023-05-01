#This should be returning details about a specific match ID
import json
import requests
import time
from random import randint
import pandas as pd
import math
import os
from flask import request
from datetime import datetime

# --- Steam ID's for testing purposes ---
# 883661889
# 80037375
# 163881259
# 97203194

LIMIT = 9

class Player:
    hero_info_data = open('Test2\static\JSON\heroInfo.json')
    json_hero_info_data = json.load(hero_info_data)

    base_url = f'https://api.opendota.com/api/'
    player_endpoint = f'players/'
    empty_endpoint = f'/'
    recent_matches_endpoint = f'/recentMatches/'
    wl_endpoint = f'/wl'
    peers_endpoint = f'/peers'
    heroes_endpoint = f'/heroes'

    def __init__(self, steam_id):
        self.steam_id = steam_id

    def main_request(self):
        r = requests.get(self.base_url + self.player_endpoint + self.steam_id)
        data = r.json()
        return data 

    def get_recent_matches(self):
        recent_matches = requests.get(self.base_url + self.player_endpoint + self.steam_id + self.recent_matches_endpoint)
        data_recent_matches = recent_matches.json()

        game_list = []
        for game in data_recent_matches:
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
            
            if result == 'Won Match':
                resultId = 'WonMatch'
            elif result == 'Lost Match':
                resultId = 'LostMatch'
            else:
                resultId = 'Unknown'

            for x in self.json_hero_info_data:
                if game['hero_id'] == self.json_hero_info_data[x]['id']:
                    hero_name = self.json_hero_info_data[x]['name']
        
            start_time = game['start_time']
            
            if game['lobby_type'] == 7:
                lobby_type = "Ranked"
            else:
                lobby_type = "Unranked"

            match_info = {
                'match_id': match_id,
                'duration': time.strftime("%H:%M:%S", time.gmtime(duration)), #converts the time from seconds to minutes (and seconds) in standard format
                'hero_name': hero_name,
                'kills': kills,
                'deaths': deaths,
                'assists': assists,
                'party_size': party_size, 
                'lobby_type': lobby_type,
                'start_time': datetime.fromtimestamp(start_time).strftime("%B %d, %Y"),
                'team': team,   
                'result': result,
                'resultId': resultId,

            }
            game_list.append(match_info)

        return game_list

    def get_user(self):
        user = requests.get(self.base_url + self.player_endpoint + self.steam_id)
        data_user = user.json()

        user2 = requests.get(self.base_url + self.player_endpoint + self.steam_id + self.wl_endpoint)
        data_user2 = user2.json()   
        
        winrate = float(data_user2['win'] / float(data_user2['win'] + data_user2['lose']))
        winrate = winrate * 100
        finalWinrate = str(round(winrate, 2)) + "%"
        
        if data_user['rank_tier']:
            rankName = math.trunc(int(data_user['rank_tier'])/10)
            rankNumber = int(data_user['rank_tier'])%10
        else:
            rankName = 0
            rankNumber = ""
       
        
        profile_list = []
        player_info = {
            'name': data_user['profile']['personaname'],
            'id': data_user['profile']['steamid'],
            'avatar': data_user['profile']['avatarfull'],
            'rank_name': rankName,
            'rank_number': rankNumber,
            'rank_tier': data_user['rank_tier'],
            'rank_estimate': data_user['mmr_estimate']['estimate'],
            'wins': data_user2['win'],   
            'losses': data_user2['lose'], 
            'wr': finalWinrate,
            
        }
        profile_list.append(player_info)

        return profile_list
    
    def get_peers(self):
        user = requests.get(self.base_url + self.player_endpoint + self.steam_id + self.peers_endpoint)
        data_peers = user.json()
        

        peer_list = []
        for peer in data_peers:
            personaname = peer['personaname']
            avatarfull = peer['avatarfull']
            account_id = peer['account_id']
            with_win = peer['with_win']
            with_games = peer['with_games']
            last_played = peer['last_played']
            if with_games > 0:
                wr = with_win/with_games * 100
                with_wr = str(round(wr, 2)) + "%"
            else:
                with_wr = "00.00%"
            
            peer_info = {
                'personaname': personaname,
                'avatarfull': avatarfull,
                'account_id': account_id,
                'with_win': with_win,
                'with_games': with_games ,
                'with_wr': with_wr,
                'last_played': datetime.fromtimestamp(last_played).strftime("%B %d, %Y"),
                # 'last_played': last_played,
            }
            if len(peer_list) < LIMIT:
                peer_list.append(peer_info)
            else:
                break
        return peer_list
    
    def get_most_played(self):
        most_played = requests.get(self.base_url + self.player_endpoint + self.steam_id + self.heroes_endpoint)
        data_heroes = most_played.json()

        most_played_list = []
        for game in data_heroes:
            hero_id = game['hero_id']
            games = game['games']
            win = game['win']
            last_played = game['last_played']

            if games > 0:
                wrt = win/games * 100
                wr = str(round(wrt, 2)) + "%"
            else:
                wr = "00.00%"

            
            for x in self.json_hero_info_data:
                if int(hero_id) == self.json_hero_info_data[x]['id']:
                    hero_name = self.json_hero_info_data[x]['name']
        
            
            mp_info = {
                'hero_id': hero_id,
                'hero_name': hero_name,
                'games': games,
                'win': win,
                'wr': wr,
                'last_played': datetime.fromtimestamp(last_played).strftime("%B %d, %Y"),
            }
            if len(most_played_list) < LIMIT:
                most_played_list.append(mp_info)
            else:
                break
            

        
        return most_played_list



    def make_data(self):   
        data = self.main_request()
        return data
        
    def parse_json(self):
        for items in self.get_recent_matches():
            return items

    def mainlist(self):
        mainlist = []
        mainlist.extend(self.get_recent_matches())
        return mainlist

    def profilelist(self):
        profilelist = []
        profilelist.extend(self.get_user())
        return profilelist
    
    def peerlist(self):
        peerlist = []
        peerlist.extend(self.get_peers())
        return peerlist
    
    def mostplayedlist(self):
        mostplayedlist = []
        mostplayedlist.extend(self.get_most_played())
        return mostplayedlist


    def display_player(self):
        dotadf = pd.DataFrame(self.mainlist())
        dotadf.to_json('Test2\static\JSON\matches_recent.json', orient='records', indent=2)

        dotadfProfile = pd.DataFrame(self.profilelist()) 
        dotadfProfile.to_json('Test2\static\JSON\PlayerProfile.json', orient='records', indent=2)

        dotadfPeer = pd.DataFrame(self.peerlist()) 
        dotadfPeer.to_json('Test2\static\JSON\peer_info.json', orient='records', indent=2)

        dotadfHeroes = pd.DataFrame(self.mostplayedlist()) 
        dotadfHeroes.to_json('Test2\static\JSON\mostplayed_info.json', orient='records', indent=2)