import requests

def find_longest_shortest_game(api_key, match_ids):
    longest_game_duration = 0
    longest_game_id = None
    shortest_game_duration = float('inf')
    shortest_game_id = None

    for match_id in match_ids:
        match_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}'
        resp = requests.get(match_url)
        match_data = resp.json()

        # Calculate the game duration in minutes
        game_duration = match_data['info']['gameDuration'] / 60

        # Check for the longest game
        if game_duration > longest_game_duration:
            longest_game_duration = game_duration
            longest_game_id = match_id

        # Check for the shortest game
        if game_duration < shortest_game_duration:
            shortest_game_duration = game_duration
            shortest_game_id = match_id

    return longest_game_id, longest_game_duration, shortest_game_id, shortest_game_duration

if __name__ == "__main__":
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

    # Get the PUUID URL
    api_url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20'
    api_url = api_url + '&api_key=' + api_key
    resp = requests.get(api_url)

    match_ids = resp.json()

    if match_ids:
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