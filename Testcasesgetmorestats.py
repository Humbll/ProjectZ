import requests
import pyodbc


context = pyodbc.connect(f'DRIVER={{ODBC Driver 18 for SQL Server}};server=localhost\\SQLExpress;database=master;Encrypt=No;Trusted_Connection=Yes',autocommit=True)
cursor = context.cursor()
cursor.execute('use test')
# cursor.execute('create database test')
# cursor.execute('create table users (username VARCHAR(MAX), password VARCHAR(MAX))')
cursor.execute('create table shortgames')






# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'RGAPI-6fcd2047-a50f-40ab-a2a1-7c18d2adcad2'
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
    longest_game_duration = 0
    longest_game_id = None

    for match_id in match_ids:
        match_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}'
        resp = requests.get(match_url)
        match_data = resp.json()
        print(match_data)
        # Calculate the game duration in minutes
        game_duration = match_data['info']['gameDuration'] / 60
        
        # Check for the longest game
        if game_duration > longest_game_duration:
            longest_game_duration = game_duration
            longest_game_id = match_id

    if longest_game_id:
        print(f'Longest Game ID: {longest_game_id}')
        print(f'Longest Game Duration: {longest_game_duration} minutes')
    else:
        print(f'No recorded games found.')

if match_ids:
    shortest_game_duration = float('inf')
    shortest_game_id = None

    for match_id in match_ids:
        match_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}'
        resp = requests.get(match_url)
        match_data = resp.json()
        
        # Calculate the game duration in minutes
        game_duration = match_data['info']['gameDuration'] / 60
        
        # Check for the shortest game
        if game_duration < shortest_game_duration:
            shortest_game_duration = game_duration
            shortest_game_id = match_id

    if shortest_game_id:
        print(f'Shortest Game ID: {shortest_game_id}')
        print(f'Shortest Game Duration: {shortest_game_duration} minutes')
    else:
        print(f'No recorded games found.')

else:
    print(f'{summoner_name} has no recorded games.')
