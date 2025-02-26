import extract.espn.game as eg
import extract.espn.team as et
import transform.transform as t
import load.mysql_db as ld
import requests

weeks = 1
distinct_away_teams = set()

def get_all_games_in_week(week_num: int) -> list:
    espn_scoreboard_endpoint = f'https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?seasontype=2&week={week_num}'
    data = requests.get(espn_scoreboard_endpoint).json()
    events = data['events']
    return events

def get_team(team_id: str) -> dict:
    espn_team_endpoint = f'http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/{team_id}'
    data = requests.get(espn_team_endpoint).json()
    return data

def load_game_data(game_data: object):
    ld.load_game(t.format_game(game_data))
    ld.load_odds(t.format_odds(game_data))
    ld.load_location(t.format_location(game_data))
    ld.load_box_scores(t.format_away_box_score(game_data))
    ld.load_box_scores(t.format_home_box_score(game_data))

def load_team_data(team_data: object):
    ld.load_team(t.format_team(team_data))
    ld.load_team_stats(t.format_team_stats(team_data))
    ld.load_record(t.format_conference_record(team_data))
    ld.load_record(t.format_overall_record(team_data))

# Extract and Load Game related data
for week in range(weeks):
    week += 1
    week_json_response = get_all_games_in_week(week)
    for game_json in week_json_response:
        game = eg.Game(game_json, 'CFB')
        print(game.date)
        #game_dict = e.get_scoreboard_data(game)
        distinct_away_teams.add(game.away_team_id)
        load_game_data(game)

# Extract and Load Team related data
for distict_team in distinct_away_teams:
    #team_dict = e.get_team_data(team)
    team = et.Team(distict_team)
    load_team_data(team)

