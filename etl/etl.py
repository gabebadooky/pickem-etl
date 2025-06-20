import requests, time
import etl.extract.espn.game as eg
import etl.extract.cbs.game as cg
import etl.extract.geocodes as el
import etl.extract.espn.team as et
import etl.extract.cbs.team_stats as ct
from bs4 import BeautifulSoup
from etl.extract.game import Game
from etl.extract.team import Team
from etl.transform import transform as t
from etl.load import mysql_db as ld


def get_all_espn_games_in_week(espn_scoreboard_endpoint: str) -> list:
    """Method to retrieve all games from ESPN games endpoint"""
    data: dict = requests.get(espn_scoreboard_endpoint).json()
    events: list = data["events"]
    return events

def get_espn_team(espn_team_endpoint: str) -> dict:
    """Method to retrieve data from a given ESPN team endpoint"""
    data_fetched: bool = False
    while data_fetched is not True:
        try:
            data: dict = requests.get(espn_team_endpoint).json()
            data_fetched = True
        except Exception as e:
            print(f"Error occurred retrieving data from {espn_team_endpoint}:\n{e}")
            time.sleep(2)
    return data

def scrape_cbs_games_in_week(cbs_scoreboard_week_url: str) -> BeautifulSoup:
    """Method to scrape CBS scoreboard page for give, week"""
    page_response: requests.Response = requests.get(cbs_scoreboard_week_url)
    return BeautifulSoup(page_response.content, "html.parser")

def find_cbs_game_scorecard(page_soup: str, game_id: str) -> BeautifulSoup:
    """Method to find scorecard for current game"""
    print(game_id)
    team_links: list = page_soup.find_all("a", class_="team-name-link")
    for team_link in team_links:
        print(f"team_link: {team_link}")
        #reformatted_team: str = team_link.get_text().replace("é", "e").replace("&", "").replace(".", "").replace(" ", "-").replace("(", "").replace(")", "").lower()
        ending_index: int = team_link["href"].rfind('/')
        beginning_index: int = team_link["href"].rfind('/', 0, ending_index) + 1
        reformatted_team: str = team_link["href"][beginning_index:ending_index]
        print(reformatted_team)
        if reformatted_team in game_id:
            print("team found!")
            for parent in team_link.parents:
                parent_element: str = parent
                if parent_element.name == "div" and "single-score-card" in parent_element.get("class", []):
                    return parent_element

def load_game_data(game_data: object):
    """Method to consolidate and load game data from various sources"""
    ld.load_box_scores(t.format_away_box_score(game_data))
    ld.load_box_scores(t.format_home_box_score(game_data))
    ld.load_location(t.format_location(game_data))
    ld.load_odds(t.format_odds(game_data))
    ld.load_game(t.format_game(game_data))

def load_team_data(team_data: object):
    """Method to consolidate and load team data from various sources"""
    ld.load_record(t.format_conference_record(team_data))
    ld.load_record(t.format_overall_record(team_data))
    ld.load_team_stats(t.format_team_stats(team_data))
    ld.load_team(t.format_team(team_data))




def extract_and_load_games(league: str, weeks: int, espn_scoreboard_endpoint: str, cbs_scoreboard_week_url: str):
    """Method to perfom ETL process for games data from various sources"""
    distinct_teams: set = set()
    for week in range(weeks):
        week += 1
        espn_week_response: list = get_all_espn_games_in_week(f"{espn_scoreboard_endpoint}{week}")
        cbs_week_content: BeautifulSoup = scrape_cbs_games_in_week(f"{cbs_scoreboard_week_url}/{week}")
        for espn_game_json in espn_week_response:
            print(f"\n\nProcessing ESPN {league} Game {espn_game_json["id"]}")
            game: Game = Game()
            game_id = eg.extract_game_id(espn_game_json)
            cbs_game_scorecard_soup: BeautifulSoup = find_cbs_game_scorecard(cbs_week_content, game_id)
            print(cbs_game_scorecard_soup)
            game.game_id = game_id
            game.league = league
            game.week = week
            game.year = eg.extract_game_year(espn_game_json)
            game.espn_code = eg.extract_game_code(espn_game_json)
            game.cbs_code = cg.get_cbs_code(cbs_game_scorecard_soup) # Scrape CBS game scorebaord
            # game.fox_code = 
            # game.vegas_code = 
            game.away_team_id = eg.extract_away_team(espn_game_json)
            game.home_team_id = eg.extract_home_team(espn_game_json)
            game.date = eg.extract_game_date(espn_game_json)
            game.time = eg.extract_game_time(espn_game_json)
            game.tv_coverage = eg.extract_tv_coverage(espn_game_json)
            game.finished = eg.extract_game_finished(espn_game_json)
            # game.away_q1_score =
            # game.away_q2_score = 
            # game.away_q3_score
            # game.away_q4_score
            # game.away_overtime_score
            # game.away_total_score
            # game.home_q1_score
            # game.home_q2_score
            # game.home_q3_score
            # game.home_q4_score
            # game.home_overtime_score
            # game.home_total_score
            game.espn_away_moneyline = eg.extract_away_moneyline(espn_game_json)
            game.espn_home_moneyline = eg.extract_home_moneyline(espn_game_json)
            game.espn_away_spread = eg.extract_away_spread(espn_game_json)
            game.espn_home_spread = eg.extract_home_spread(espn_game_json)
            game.espn_over_under = eg.extract_over_under(espn_game_json)
            # game.espn_away_win_percentage = 
            # game.espn_home_win_percentage = 
            # game.cbs_away_moneyline = cg.get_away_moneyline()
            # game.cbs_home_moneyline = cg.get_home_moneyline()
            # game.cbs_away_spread = 
            # game.cbs_home_spread = 
            # game.cbs_over_under = cg.get_over_under()
            # game.cbs_away_win_percentage = 
            # game.cbs_home_win_percentage = 
            # fox odds metrics ...
            
            stadium = eg.extract_stadium(espn_game_json)
            city = eg.extract_city(espn_game_json)
            state = eg.extract_state(espn_game_json)
            lat, lon = el.get_lat_long_tuple(stadium, city, state)
            game.stadium = stadium
            game.city = city
            game.state = state
            game.latitude = lat
            game.longitude = lon

            distinct_teams.add(espn_game_json["competitions"][0]["competitors"][0]["team"]["id"])
            distinct_teams.add(espn_game_json["competitions"][0]["competitors"][1]["team"]["id"])
            load_game_data(game)

            #print(f"\n\nProcessing ESPN {league} Game {game_json["id"]}")
            #game: Game = eg.Game(game_json, league)
            #distinct_teams.add(game_json["competitions"][0]["competitors"][0]["team"]["id"])
            #distinct_teams.add(game_json["competitions"][0]["competitors"][1]["team"]["id"])
            #load_game_data(game)
    return distinct_teams


def extract_and_load_teams(league: str, distinct_teams: set, espn_team_endpoint: str):
    """Method to perfom ETL process for teams data from various sources"""
    for distict_team in distinct_teams:
        print(f"\n\nProcessing {league} Team {distict_team}")
        team_json: dict = get_espn_team(f"{espn_team_endpoint}/{distict_team}")
        time.sleep(1.5)
        team: Team = et.Team(team_json)
        load_team_data(team)

