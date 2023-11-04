import requests
import pyodbc


context = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};server=localhost\\SQLExpress;database=master;Encrypt=No;Trusted_Connection=Yes',autocommit=True)
cursor = context.cursor()
cursor.execute('use test')
# cursor.execute('create database test')
# cursor.execute('create table users (username VARCHAR(MAX), password VARCHAR(MAX))')
cursor.execute('create table shortgames')

def shortgame(api_url, summoner_name, api_key):

    response = requests.get(api_url)
    if response.status_code != 200:
        return None
    
    match_ids = response.json()

    # Initialize variables to keep track of the shortest game
    shortest_game_duration = 0
    shortest_game_id = None

    
    # Iterate through match IDs and find the shortest game
    for match_id in match_ids:
        match_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}'
        resp = requests.get(match_url)
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