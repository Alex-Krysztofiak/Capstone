match_request = requests.get('https://api.opendota.com/api/matches/6959099887')
match_metadata = match_request.json()
# This will have all the info that isn't an array
match_info = []
match_metadata = {
      'match_id': match_metadata['match_id'],
}
match_info.append(match_metadata) 
print(match_info)
print(match_metadata)