import requests, time
from etl.extract.espn import game as eg
from etl.extract.espn import team as et
from etl.transform import transform as t
from etl.load import mysql_db as ld

cfb_espn_scoreboard_endpoint = f'https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?seasontype=2&week='
cfb_espn_team_endpoint = f'http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/'

def get_all_games_in_week(espn_scoreboard_endpoint: str) -> list:
    data = requests.get(espn_scoreboard_endpoint).json()
    events = data['events']
    return events

def get_team(espn_team_endpoint: str) -> dict:
    data_fetched = False
    while data_fetched is not True:
        try:
            data = requests.get(espn_team_endpoint).json()
            data_fetched = True
        except Exception as e:
            print(f'Error occurred retrieving data from {espn_team_endpoint}:\n{e}')
            time.sleep(2)
    return data

def load_game_data(game_data: object):
    ld.load_box_scores(t.format_away_box_score(game_data))
    ld.load_box_scores(t.format_home_box_score(game_data))
    ld.load_location(t.format_location(game_data))
    ld.load_odds(t.format_odds(game_data))
    ld.load_game(t.format_game(game_data))

def load_team_data(team_data: object):
    ld.load_record(t.format_conference_record(team_data))
    ld.load_record(t.format_overall_record(team_data))
    ld.load_team_stats(t.format_team_stats(team_data))
    ld.load_team(t.format_team(team_data))

def extract_and_load_games(weeks):
    distinct_away_teams = set()
    for week in range(weeks):
        week += 1
        cfb_week_response = get_all_games_in_week(f'{cfb_espn_scoreboard_endpoint}{week}')
        for cfb_game_json in cfb_week_response:
            print(f"\n\nProcessing Game {cfb_game_json['id']}")
            game = eg.Game(cfb_game_json, 'CFB')
            distinct_away_teams.add(game.away_team_id)
            load_game_data(game)
    return distinct_away_teams

def extract_and_load_teams(distinct_away_teams):
    for distict_team in distinct_away_teams:
        print(f"\n\nProcessing Team {distict_team}")
        team_json = get_team(f'{cfb_espn_team_endpoint}{distict_team}')
        time.sleep(1.5)
        team = et.Team(team_json)
        load_team_data(team)

