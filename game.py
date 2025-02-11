import requests

game = '401628504'

def extract_datetime(data: dict) -> str:
    try:
        zulu_datetime = data['header']['competitions'][0]['date'].split('T')[1]
    except Exception as e:
        print(e)
        zulu_datetime = 'TBD'
    return zulu_datetime

def extract_gamedate(data: dict) -> str:
    try:
        gamedate = data['header']['competitions'][0]['date'].split('T')[0]
    except Exception as e:
        print(e)
        gamedate = ''
    return gamedate

def extract_broadcast(data: dict) -> str:
    try:
        broadcast = data['header']['competitions'][0]['broadcasts'][0]['media']['shortName']
    except Exception as e:
        print(e)
        broadcast = ''
    return broadcast

def get_game_data(game_id: str) -> dict:
    """
    Method that makes GET request to ESPN College Football Schedule
    endpoint for a given Game ID and returns the JSON response
    """
    espn_game_page = f'http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event={game_id}'
    json_response = requests.get(espn_game_page).json()
    return json_response


game_data = get_game_data(game)
print(extract_broadcast(game_data))