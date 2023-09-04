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
