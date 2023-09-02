import json
import requests
import time
from random import randint
import pandas as pd
import math

url_peers = f"https://api.opendota.com/api/players/1034963399/peers"
r_peers = requests.get(url_peers)
data_peers = json.loads(r_peers.text)
print(data_peers)

peer_list = []
for peer in data_peers:
    personaname = peer['personaname']
    avatarfull = peer['avatarfull']
    account_id = peer['account_id']
    with_win = peer['with_win']
    with_games = peer['with_games']
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
    }
    if len(peer_list) < 10:
        peer_list.append(peer_info)
    else:
        break
        

peerdf = pd.DataFrame(peer_list) 
print(peer_list)
print(peerdf)
peerdf.to_json('Test2\static\JSON\peer_info.json', orient='records', indent=2)