import requests
import numpy as np



# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'RGAPI-358cedb2-5d4e-4beb-b72e-f6ac8a1270a7'
summoner_name = 'emerald forest'
region = 'euw1'  # Change this to your region if it's different


summoner_url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
headers = {'X-Riot-Token': api_key}

try:
    response = requests.get(summoner_url, headers=headers)
    response.raise_for_status()
    summoner_data = response.json()
    summoner_id = summoner_data['id']

    # Step 2: Get the summoner's ranked data
    ranked_url = f'https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}'
    response = requests.get(ranked_url, headers=headers)
    response.raise_for_status()
    ranked_data = response.json()

    # Assuming you want to get the Solo/Duo ranked data (you can adjust this)
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
    
    
    matchlist_url = f'https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{summoner_id}'
    response = requests.get(matchlist_url, headers=headers)
    response.raise_for_status()
    matchlist_data = response.json()
    
    if matchlist_data['matches']:
        latest_game = matchlist_data['matches'][0]
        champion_id = latest_game['champion']
        timestamp = latest_game['timestamp']
        game_duration = latest_game['gameDuration'] // 60  # Convert seconds to minutes

        print(f'Latest Game Played:')
        print(f'Champion ID: {champion_id}')
        print(f'Timestamp: {timestamp}')
        print(f'Game Duration: {game_duration} minutes')
    else:
        print(f'{summoner_name} has no recorded games.')

except requests.exceptions.HTTPError as e:
    print(f'Error: {e}')
