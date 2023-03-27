import json
import requests
import time
from random import randint
import pandas as pd
import math

# Test 1
""" #Used to test how to display usernames without all the other data

 
url1 = f'https://api.opendota.com/api/players/80037375'
r3 = requests.get(url1)
data3 = json.loads(r3.text)
url2 = f'https://api.opendota.com/api'
r2 = requests.get(url2)
data2 = json.loads(r2.text)

print(data3['profile']['personaname'])

print(json.dumps(data3))
print("")
print("")

print("")

#print(json.dumps(data2))

 """

# Test 2 (create the hero list json)
# url4 = f'https://api.opendota.com/api/heroes'
# r4 = requests.get(url4)
# data4 = json.loads(r4.text)

# hero_list = []
# for hero in data4:
#     id = hero['id']
#     localized_name = hero['localized_name']
#     primary_attr = hero['primary_attr']
#     attack_type =  hero['attack_type']
#     img = "static\\\\HeroImages\\\\" + hero['localized_name'] +  ".png"
#     link = "https://dota2.fandom.com/wiki/" + hero['localized_name']
       
#     hero_info = {
#         'id': id,
#         'name': localized_name,
#         'primary_attribute': primary_attr,
#         'attack_type': attack_type,
#         'img': img,
#         'link': link,
            
#     }
#     hero_list.append(hero_info)

# dotadf = pd.DataFrame(hero_list) 
# print(dotadf)
# dotadf.to_json('Test2\static\JSON\heroList.json', orient='records', indent=2 )



# url4 = f'https://api.opendota.com/api/matches/7077691612'
# r4 = requests.get(url4)
# data4 = json.loads(r4.text)

# print(data4['replay_url'])
# player_list = []
# for x in range(0,10):
#     for player in data4:
    
#         match_id = data4['players'][x]['match_id']
#         player_slot = data4['players'][x]['player_slot']
        
#         if 'personaname' in data4['players'][x]:
#             personaname = (data4['players'][x]['personaname'])
#         else:
#             personaname = "anonymous"

#         if data4['players'][x]['account_id'] is not None:
#             account_id = math.trunc(int(data4['players'][x]['account_id']))
#         else:
#             account_id = "private"

#         hero_id = data4['players'][x]['hero_id']
#         level = data4['players'][x]['level']
#         gpm = data4['players'][x]['gold_per_min']

#         item_0 = data4['players'][x]['item_0']
#         item_1 = data4['players'][x]['item_1']
#         item_2 = data4['players'][x]['item_2']
#         item_3 = data4['players'][x]['item_3']
#         item_4 = data4['players'][x]['item_4']
#         item_5 = data4['players'][x]['item_5']
     
        
#         player_info = {
#             'id': match_id,
#             'player_slot': player_slot,
#             'personaname': personaname,
#             'account_id': account_id,
#             "hero_id": hero_id,
#             "level": level,
#             "item_0": item_0,
#             "item_1": item_1,
#             "item_2": item_2,
#             "item_3": item_3,
#             "item_4": item_4,
#             "item_5": item_5,
#             'gpm': gpm
#          }
#     player_list.append(player_info)
    


# #print(player_list)
# dotadf = pd.DataFrame(player_list) 
# print(dotadf)
# dotadf.to_json('Test2\static\JSON\match_info.json', orient='records', indent=2 )




#r3 = open('hero_info.json',)
#data3 = json.load(r3)
#for x in data3:
    #print(data3[x]['id'],data3[x]['name'])
#dotadf = pd.DataFrame(hero_list) 
#dotadf.to_json('hero_info.json', orient='index', indent=2 )

#Test 3, hero icons
""" url4 = f'https://api.opendota.com/api/heroStats'
r4 = requests.get(url4)
data4 = json.loads(r4.text)

hero_list = []
for hero in data4:
    img = hero['img']
        
    hero_info = {
      'img': img
            
    }
    hero_list.append(hero_info)

dotadf = pd.DataFrame(hero_list) 
print(dotadf)
print(data4[0]['icon'])
dotadf.to_json('JSON_hero_info.json', orient='index', indent=1 ) """

#this is going to create information about a profile

# url4 = f'https://api.opendota.com/api/players/80037375'
# r4 = requests.get(url4)
# data4 = json.loads(r4.text)
# print(data4)
"""
print(data4['profile']['personaname'])
print(data4['profile']['steamid'])
print(data4['profile']['avatar'])
print(data4['rank_tier'])
print(data4['mmr_estimate']['estimate'])
"""
# playerprofile = []
# player_info = {
#     'name': data4['profile']['personaname'],
#     'id': data4['profile']['steamid'],
#     'avatar': data4['profile']['avatar'],
#     'rank': data4['rank_tier'],
#     'rank_estimate': data4['mmr_estimate']['estimate'],     
# }
# playerprofile.append(player_info)
    

# dotadf = pd.DataFrame(playerprofile) 
# #print(player_info)
# dotadf.to_json('Test1\PlayerProfile.json', orient='records', indent=1)
