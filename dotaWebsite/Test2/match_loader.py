#This should be returning details about a specific match ID
import json
import requests
import time
from random import randint
import pandas as pd
import math
import os
from flask import request
from datetime import datetime, timedelta

class Match:
    item_info_data = open('Test2\static\JSON\item_ids.json')
    json_item_info_data = json.load(item_info_data)
    chatwheel_info_data = open('Test2\static\JSON\chat_wheel.json' , encoding = 'utf-8')
    json_chatwheel_info_data = json.load(chatwheel_info_data)

    base_url = f'https://api.opendota.com/api/'
    matches_midpoint = f'matches/'
    empty_endpoint = f''

    def __init__(self, match_id):
        self.match_id = match_id

    def main_request(self):
        match_request = requests.get(self.base_url + self.matches_midpoint + self.match_id)
        match_metadata = match_request.json()
        # This will have all the info that isn't an array
        match_info = []
        match_id = match_metadata['match_id']
        duration = match_metadata['duration']
        start_time = match_metadata['start_time']
        # replay_url = match_metadata['replay_url']

        if  match_metadata['lobby_type'] == "7":
            lobby_type = "Ranked"
        else:
            lobby_type = "Unranked"

        if match_metadata['radiant_win'] is True:
            winner = "Radiant"
        else:
            winner = "Dire"

        match_metadata = {
            'match_id': match_id,
            'lobby_type': lobby_type,
            'duration': time.strftime("%H:%M:%S", time.gmtime(duration)),
            'winner': winner,
            'start_time': datetime.fromtimestamp(start_time).strftime("%B %d, %Y"),
            # 'replay_url': replay_url,
        }
        match_info.append(match_metadata)

        return match_info
    
    #
    #
    # Needs more work!!
    #
    #
    # Gets a list of all players in the game as well as their personal stats
    def get_players(self):
        match_request = requests.get(self.base_url + self.matches_midpoint + self.match_id)
        match_data = match_request.json()
        
        player_list = []
        for x in range(len(match_data['players'])):
            for player in match_data['players']:
            
                match_id = match_data['players'][x]['match_id']
                player_slot = match_data['players'][x]['player_slot']
                
                if 'personaname' in match_data['players'][x]:
                    personaname = (match_data['players'][x]['personaname'])
                else:
                    personaname = "anonymous"

                if match_data['players'][x]['account_id']:
                    account_id = math.trunc(int(match_data['players'][x]['account_id']))
                else:
                    account_id = "private"

                hero_id = match_data['players'][x]['hero_id']
                level = match_data['players'][x]['level']
                gold = match_data['players'][x]['gold']
                gpm = match_data['players'][x]['gold_per_min']
                xpm = match_data['players'][x]['xp_per_min']
                kills = match_data['players'][x]['kills']
                deaths = match_data['players'][x]['deaths']
                assists = match_data['players'][x]['assists']

                for i in self.json_item_info_data:
                    if match_data['players'][x]['item_0']:
                        if int(i) == match_data['players'][x]['item_0']:
                            item_0 = self.json_item_info_data[i]
                    else:
                        item_0 = ""
                    if match_data['players'][x]['item_1']:
                        if int(i) == match_data['players'][x]['item_1']:
                            item_1 = self.json_item_info_data[i]
                    else:
                        item_1 = ""
                    if match_data['players'][x]['item_2']:
                        if int(i) == match_data['players'][x]['item_2']:
                            item_2 = self.json_item_info_data[i]
                    else:
                        item_2 = ""
                    if match_data['players'][x]['item_3']:
                        if int(i) == match_data['players'][x]['item_3']:
                            item_3 = self.json_item_info_data[i]
                    else:
                        item_3 = ""
                    if match_data['players'][x]['item_4']:
                        if int(i) == match_data['players'][x]['item_4']:
                            item_4 = self.json_item_info_data[i]
                    else:
                        item_4 = ""
                    if match_data['players'][x]['item_5']:
                        if int(i) == match_data['players'][x]['item_5']:
                            item_5 = self.json_item_info_data[i]
                    else:
                        item_5 = ""
            
                    # "backpack_0": 0,
                    # "backpack_1": 0,
                    # "backpack_2": 0,
                    # "hero_damage": 0,
                    # "hero_healing": 0,  
                    
                    # "tower_damage": 0,
                    # "xp_per_min": 0,
                    # "isRadiant": true,
                    # "win": 0,
                    # "lose": 0, 
                    # "total_gold": 0,
                    # "total_xp": 0,
                    # "observer_uses": 0,
                    # "sentry_uses": 0,
                    # "lane_efficiency": 0,
                    # "lane_efficiency_pct": 0,
                    # "lane": 0,
                    # "lane_role": 0,


                player_info = {
                    'id': match_id,
                    'player_slot': player_slot,
                    'personaname': personaname,
                    'account_id': account_id,
                    "hero_id": hero_id,
                    "level": level,
                    "gold": gold,
                    "kills": kills,
                    "deaths": deaths,
                    "assists": assists,

                    "item_0": item_0.replace("_", " "),
                    "item_1": item_1.replace("_", " "),
                    "item_2": item_2.replace("_", " "),
                    "item_3": item_3.replace("_", " "),
                    "item_4": item_4.replace("_", " "),
                    "item_5": item_5.replace("_", " "),

                    'gpm': gpm,
                    'xpm': xpm,

                }
            player_list.append(player_info)
        return player_list

    # Gets a chat log of the game
    def get_chat(self):
        match_request = requests.get(self.base_url + self.matches_midpoint + self.match_id)
        match_data = match_request.json()

        chat_list = []
        if match_data['chat']:
            for x in range(len(match_data['chat'])):
                for message in match_data['chat']:

                    # These don't need anything fancy
                    timer_check = match_data['chat'][x]['time']
                    str(timer_check)
                    
                    if "-" in str(timer_check):
                        str_time = str(timer_check)
                        str_time = str_time[1:]
                        str_time = int(str_time)
                        
                        timer = time.strftime("- 00:%M:%S", time.gmtime(str_time))
                    else:
                        timer = time.strftime("%H:%M:%S", time.gmtime(match_data['chat'][x]['time']))
                    
                         
                    key = match_data['chat'][x]['key']
                    type = match_data['chat'][x]['type']
                    
                    slot = match_data['chat'][x]['slot']
                    player_slot = match_data['chat'][x]['player_slot']

                    # This shits dumb af
                    if match_data['chat'][x]['type'] == "chatwheel":
                        if match_data['chat'][x]['key'] == '71':
                            msg = "A hero is missing"
                        else:
                            msg = self.json_chatwheel_info_data[key]['message']
                    else:
                        msg = key
                    
                    message_info = {
                        'timer': timer,
                        'type': type,
                        'key': key, 
                        'slot': slot, 
                        # Player slot will be replaced by the players name and hero picture in JS
                        'player_slot': player_slot,
                        'message': msg
                    }
                chat_list.append(message_info)
        return chat_list

    
    def make_data(self):
        data = self.main_request()
        return data
    def parse_json(self):
        for items in self.main_request():
            return items
        
    def mainlist(self):
        mainlist = []
        mainlist.extend(self.main_request())
        return mainlist
    def playerlist(self):
        playerlist = []
        playerlist.extend(self.get_players())
        return playerlist
    def chatlist(self):
        chatlist = []
        chatlist.extend(self.get_chat())
        return chatlist

    def display_match(self):
        dotadfMatch = pd.DataFrame(self.mainlist())
        dotadfMatch.to_json('Test2\static\JSON\match_info.json', orient='records', indent=2)

        dotadf_player = pd.DataFrame(self.playerlist())
        dotadf_player.to_json('Test2\static\JSON\player_info.json', orient='records', indent=2)

        dotadf_chat = pd.DataFrame(self.chatlist())
        dotadf_chat.to_json('Test2\static\JSON\chat_info.json', orient='records', indent=2)