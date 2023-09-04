import requests

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'RGAPI-80bed39b-409c-4394-a7b9-9962fc2a1631'
summoner_name = 'aaddee'
region = 'euw1'  # Change this to your region if it's different

summoner_url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
headers = {'X-Riot-Token': api_key}
summoner_url = summoner_url + '?api_key=' + api_key

try:
    # Send a GET request to obtain summoner data
    response = requests.get(summoner_url, headers=headers)
    response.raise_for_status()
    summoner_data = response.json()
    summoner_id = summoner_data['puuid']
    
     # Create the matchlist URL
    matchlist_url = f'https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{summoner_id}'


except requests.exceptions.HTTPError as e:
    print(f'Error: {e}')