import requests
import numpy as np



# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'RGAPI-80bed39b-409c-4394-a7b9-9962fc2a1631'
summoner_name = 'aaddee'
region = 'euw1'  # Change this to your region if it's different


summoner_url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
headers = {'X-Riot-Token': api_key}

try:
    response = requests.get(summoner_url, headers=headers)
    response.raise_for_status()
    summoner_data = response.json()
    summoner_id = summoner_data['id']

    ranked_url = f'https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}'
    response = requests.get(ranked_url, headers=headers)
    response.raise_for_status()
    ranked_data = response.json()

    # Check if the summoner is ranked in Solo/Duo queue
    for entry in ranked_data:
        if entry['queueType'] == 'RANKED_SOLO_5x5':
            tier = entry['tier']
            rank = entry['rank']
            print(f'Summoner: {summoner_name}')
            print(f'Tier: {tier} {rank}')
            break
    else:
        print(f'{summoner_name} is not currently ranked in Solo/Duo queue.')

except requests.exceptions.HTTPError as e:
    print(f'Error: {e}')