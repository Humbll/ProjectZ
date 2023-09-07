import requests
from shortgame import shortgame


# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'RGAPI-333dd18a-fba2-492b-8fb0-ab20bf3c22ed'
summoner_name = 'aaddee'
region = 'euw1'  # Change this to your region if it's different

api_url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
requests.get(api_url)
api_url = api_url + '?api_key=' + api_key
api_url
requests.get(api_url)

resp = requests.get(api_url)
player_info = resp.json()
puuid = player_info['puuid']
# get the PUUID URL
api_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20"

api_url = api_url + '&api_key=' + api_key 
resp = requests.get(api_url)

# Get the latest match data
match_ids = resp.json()
# Check if there are any match IDs


shortest_game_id, shortest_game_duration = shortgame(api_url, summoner_name)

if shortest_game_id:
    print(f'Summoner: {summoner_name}')
    print(f'Shortest Game ID: {shortest_game_id}')
    print(f'Shortest Game Duration: {shortest_game_duration} minutes')
else:
    print(f'No recorded shortest games found for {summoner_name}.')