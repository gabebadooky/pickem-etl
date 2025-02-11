import requests

game = '401754516'


def get_game_data(game_id: str) -> dict:
    """
    Method that makes GET request to ESPN College Football Schedule
    endpoint for a given Game ID and returns the JSON response
    """
    espn_game_page = f'http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event={game_id}'
    json_response = requests.get(espn_game_page).json()
    return json_response


game_json = get_game_data(game)

zulu_datetime = game_json['header']['competitions'][0]['date'].split('T')[1]
game_date = game_json['header']['competitions'][0]['date'].split('T')[0]
broadcast = game_json['header']['competitions'][0]['broadcasts']

print(broadcast)