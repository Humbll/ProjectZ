import requests

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'RGAPI-80bed39b-409c-4394-a7b9-9962fc2a1631'
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
api_url = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/K-UDi0UtqeVFQRI1pEZaROIdCjYk0ObnXiUXmGuG-LDiB16LLc9jddPn7FzDbQwIXDFey-Gt6b40Gw/ids?start=0&count=20"
api_url = api_url + '&api_key=' + api_key 
resp = requests.get(api_url)

# Get the latest match data
match_ids = resp.json()
# Check if there are any match IDs

if match_ids:
    from gamelength import find_longest_shortest_game  # Import the function

    (longest_id, longest_duration, shortest_id, shortest_duration) = find_longest_shortest_game(api_key, match_ids)

    if longest_id:
        print(f'Longest Game ID: {longest_id}')
        print(f'Longest Game Duration: {longest_duration} minutes')
    else:
        print(f'No recorded longest games found.')

    if shortest_id:
        print(f'Shortest Game ID: {shortest_id}')
        print(f'Shortest Game Duration: {shortest_duration} minutes')
    else:
        print(f'No recorded shortest games found.')

else:
    print(f'{summoner_name} has no recorded games.')