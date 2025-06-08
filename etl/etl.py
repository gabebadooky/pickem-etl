import requests, time
from etl.extract.espn import game as eg
from etl.extract.espn import team as et
from etl.transform import transform as t
from etl.load import mysql_db as ld


def get_all_games_in_week(espn_scoreboard_endpoint: str) -> list:
    data = requests.get(espn_scoreboard_endpoint).json()
    events = data["events"]
    return events

def get_team(espn_team_endpoint: str) -> dict:
    data_fetched = False
    while data_fetched is not True:
        try:
            data = requests.get(espn_team_endpoint).json()
            data_fetched = True
        except Exception as e:
            print(f"Error occurred retrieving data from {espn_team_endpoint}:\n{e}")
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



def extract_and_load_games(league: str, weeks: int, espn_scoreboard_endpoint: str):
    distinct_teams = set()
    for week in range(weeks):
        week += 1
        week_response = get_all_games_in_week(f"{espn_scoreboard_endpoint}{week}")
        for game_json in week_response:
            print(f"\n\nProcessing ESPN {league} Game {game_json["id"]}")
            game = eg.Game(game_json, league)
            distinct_teams.add(game_json["competitions"][0]["competitors"][0]["team"]["id"])
            distinct_teams.add(game_json["competitions"][0]["competitors"][1]["team"]["id"])
            load_game_data(game)
    return distinct_teams


def extract_and_load_teams(league: str, distinct_teams: set, espn_team_endpoint: str):
    for distict_team in distinct_teams:
        print(f"\n\nProcessing {league} Team {distict_team}")
        team_json = get_team(f"{espn_team_endpoint}{distict_team}")
        time.sleep(1.5)
        team = et.Team(team_json)
        load_team_data(team)

