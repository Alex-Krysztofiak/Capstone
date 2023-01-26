import requests 
import json

#Used to test how to display usernames without all the other data

url1 = f'https://api.opendota.com/api/players/163881259'
r3 = requests.get(url1)
data3 = json.loads(r3.text)

print(data3['profile']['personaname'])
print(json.dumps(data3))
