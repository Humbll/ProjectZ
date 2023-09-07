import requests


def shortgame(api_url, summoner_name):
   

    response = requests.get(api_url)
    
    if response.status_code != 200:
        return None
    
    match_ids = response.json()

    # Initialize variables to keep track of the shortest game
    shortest_game_duration = float('inf')
    shortest_game_id = None

    
    # Iterate through match IDs and find the shortest game
    for match_id in match_ids:
        resp = requests.get(api_url)

      
        # Parse the JSON response into match data
        match_data = resp.json()

          
        try:
            game_duration = match_data['info']['gameDuration'] / 60
            print(f'Game Duration: {game_duration} minutes')
            
            # Check if this game is shorter than the current shortest
            if game_duration < shortest_game_duration:
                shortest_game_duration = game_duration
                shortest_game_id = match_id
        except KeyError:
    # Handle the case where 'info' or 'gameDuration' is not present in match_data
            pass
    return shortest_game_id, shortest_game_duration