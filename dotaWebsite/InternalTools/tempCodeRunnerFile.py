url4 = f'https://api.opendota.com/api/matches/7077691612'
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
