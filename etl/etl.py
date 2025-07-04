import requests, time
import etl.extract.espn.game as eg
import etl.extract.cbs.game as cg
import etl.extract.opencage.geocodes as el
import etl.extract.espn.team as et
import etl.extract.cbs.team as ct
import etl.extract.cbs.team_stats as cts
import etl.load.mysql_db as ld
import etl.TeamMapping as tm
from bs4 import BeautifulSoup
from etl.extract.game import Game
from etl.extract.team import Team
from etl.transform import transform as t
from etl.load import mysql_db as ld

logfile_path: str = "./etl.log"


def get_all_espn_games_in_week(espn_scoreboard_endpoint: str) -> list:
    """Method to retrieve all games from ESPN games endpoint"""
    print(f"Retrieving games for current week from ESPN endpoint {espn_scoreboard_endpoint}")
    data: dict = requests.get(espn_scoreboard_endpoint).json()
    events: list = data["events"]
    return events

def get_espn_team(espn_team_endpoint: str) -> dict:
    """Method to retrieve data from a given ESPN team endpoint"""
    print(f"Retrieving team from ESPN team endpoint {espn_team_endpoint}")
    data_fetched: bool = False
    while data_fetched is not True:
        try:
            data: dict = requests.get(espn_team_endpoint).json()
            data_fetched = True
        except Exception as e:
            print(f"Error occurred attempting team endpoint request... Reattempting request!\nError: {e}\n")
            time.sleep(1)
    return data

def scrape_cbs_games_in_week(cbs_scoreboard_week_url: str) -> BeautifulSoup:
    """Method to scrape CBS scoreboard page for give, week"""
    print(f"Scraping games for current week from CBS games page {cbs_scoreboard_week_url}")
    page_fetched: bool = False
    while page_fetched is not True:
        try:
            page_response: requests.Response = requests.get(cbs_scoreboard_week_url)
            page_fetched = True
        except Exception as e:
            print(f"Error occurred attempting cbs game week page request... Reattempting request!\nError: {e}\n")
            time.sleep(1)
    return BeautifulSoup(page_response.content, "html.parser")

def find_cfb_cbs_game_scorecard(page_soup: str, game_id: str, week: int) -> BeautifulSoup:
    """Method to find scorecard for current CFB game"""
    print(f"Scraping {game_id} scorecard from CBS game page")
    # TODO: Refactor me plz
    team_links: list = page_soup.find_all("a", class_="team-name-link")
    scorecards: list[str] = []
    for team_link in team_links:
        ending_index: int = team_link["href"].rfind('/')
        beginning_index: int = team_link["href"].rfind('/', 0, ending_index) + 1
        reformatted_team: str = team_link["href"][beginning_index:ending_index]
        if reformatted_team in tm.cbs_to_espn_team_code_mapping:
            reformatted_team = tm.cbs_to_espn_team_code_mapping[reformatted_team]
        if reformatted_team in game_id:
            for parent in team_link.parents:
                parent_element: str = parent
                if parent_element.name == "div" and "single-score-card" in parent_element.get("class", []):
                    if week <= 1:
                        scorecards.append(parent_element)
                    else:
                        return parent_element
    if len(scorecards) > 1:
        return scorecards[week]
    else:
        return scorecards[0]

def scrape_cbs_team_stats(team_stats_page_url: str) -> BeautifulSoup:
    """Method to scrape CBS team stats page"""
    print(f"Scraping stats for current team from CBS team stats page {team_stats_page_url}")
    page_fetched: bool = False
    while page_fetched is not True:
        try:
            page_response: requests.Response = requests.get(team_stats_page_url)
            page_fetched = True
        except Exception as e:
            print(f"Error occurred attempting CBS Team Stats page request... Reattempting request!\nError: {e}\n")
            time.sleep(1)
    return BeautifulSoup(page_response.content, "html.parser")

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




def extract_and_load_games(league: str, weeks: int, espn_scoreboard_endpoint: str, cbs_scoreboard_week_url: str) -> dict:
    """Method to perfom ETL process for games data from various sources"""
    logfile = open(logfile_path, 'a')

    for week in range(weeks + 1):
        logfile.write(f"\nProcessing {league} week {week} games")
        print(f"\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nProcessing {league} week {week} games\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
        espn_week_response: list[dict] = get_all_espn_games_in_week(f"{espn_scoreboard_endpoint}{week + 1 if week == 0 else week}")
        cbs_week_content: BeautifulSoup = scrape_cbs_games_in_week(f"{cbs_scoreboard_week_url}/{week + 1 if week == 0 else week}")
        
        for espn_game_json in espn_week_response:
            game: Game = Game()
            game.game_id = eg.extract_game_id(espn_game_json)
            game.league = league
            game.week = eg.extract_game_week(espn_game_json)
            game.year = eg.extract_game_year(espn_game_json)
            print(f"\nProcessing Week {week} Game ID: {game.game_id}")

            cbs_game_scorecard_soup: BeautifulSoup = find_cfb_cbs_game_scorecard(cbs_week_content, game.game_id, week)
            
            game.espn_code = eg.extract_game_code(espn_game_json)
            game.cbs_code = cg.get_cbs_code(cbs_game_scorecard_soup) # Scrape CBS game scorebaord
            game.fox_code = ""
            game.vegas_code = ""
            
            stadium = eg.extract_stadium(espn_game_json)
            city = eg.extract_city(espn_game_json)
            state = eg.extract_state(espn_game_json)
            lat, lon = 0.0, 0.0                     # el.get_lat_long_tuple(stadium, city, state)

            game.away_team_id = eg.extract_away_team(espn_game_json)
            game.home_team_id = eg.extract_home_team(espn_game_json)
            game.date = eg.extract_game_date(espn_game_json)
            game.time = eg.extract_game_time(espn_game_json)
            game.tv_coverage = eg.extract_tv_coverage(espn_game_json)
            game.finished = eg.extract_game_finished(espn_game_json)
            game.away_q1_score = 0                  # TODO: Develop extract_box_score methods during/after week 0
            game.away_q2_score = 0                  # TODO: Develop extract_box_score methods during/after week 0
            game.away_q3_score = 0                  # TODO: Develop extract_box_score methods during/after week 0
            game.away_q4_score = 0                  # TODO: Develop extract_box_score methods during/after week 0
            game.away_overtime_score = 0            # TODO: Develop extract_box_score methods during/after week 0
            game.away_total_score = 0               # TODO: Develop extract_box_score methods during/after week 0
            game.home_q1_score = 0                  # TODO: Develop extract_box_score methods during/after week 0
            game.home_q2_score = 0                  # TODO: Develop extract_box_score methods during/after week 0
            game.home_q3_score = 0                  # TODO: Develop extract_box_score methods during/after week 0
            game.home_q4_score = 0                  # TODO: Develop extract_box_score methods during/after week 0
            game.home_overtime_score = 0            # TODO: Develop extract_box_score methods during/after week 0
            game.home_total_score = 0               # TODO: Develop extract_box_score methods during/after week 0
            game.espn_away_moneyline = eg.extract_away_moneyline(espn_game_json)
            game.espn_home_moneyline = eg.extract_home_moneyline(espn_game_json)
            game.espn_away_spread = eg.extract_away_spread(espn_game_json)
            game.espn_home_spread = eg.extract_home_spread(espn_game_json)
            game.espn_over_under = eg.extract_over_under(espn_game_json)
            game.espn_away_win_percentage = None    # TODO: Develop extract_away_win_percentage method, when available
            game.espn_home_win_percentage = None    # TODO: Develop extract_home_win_percentage method, when available
            game.cbs_away_moneyline = None          # cg.get_away_moneyline()
            game.cbs_home_moneyline = None          # cg.get_home_moneyline()
            game.cbs_away_spread = None             # TODO: Develop extract_away_spread method, when available
            game.cbs_home_spread = None             # TODO: Develop extract_away_spread method, when available
            game.cbs_over_under = None              # cg.get_over_under()
            game.cbs_away_win_percentage = None     # TODO: Develop extract_away_win_percentage method, when available
            game.cbs_home_win_percentage = None     # TODO: Develop extract_home_win_percentage method, when available
            # fox odds metrics ... 
            game.stadium = stadium
            game.city = city
            game.state = state
            game.latitude = lat
            game.longitude = lon


            if espn_game_json["competitions"][0]["competitors"][0]["homeAway"] == "away":
                espn_away_team_code: str = espn_game_json["competitions"][0]["competitors"][0]["team"]["id"]
            else:
                espn_away_team_code: str = espn_game_json["competitions"][0]["competitors"][1]["team"]["id"]
            
            if game.away_team_id in tm.espn_to_cbs_team_code_mapping:
                cbs_away_team_name: str = tm.espn_to_cbs_team_code_mapping[game.away_team_id]
            else: 
                cbs_away_team_name: str = game.away_team_id
            cbs_away_team_code: str = f"{ct.get_away_team_abbreviation(game.cbs_code)}/{cbs_away_team_name}"

            away_team: dict = {
                "team_id": game.away_team_id,
                "league": league,
                "cbs_code": cbs_away_team_code,
                "espn_code": espn_away_team_code,
                "fox_code": "",
                "vegas_code": "",
                "conference_code": None,
                "conference_name": None,
                "division_name": None,
                "team_name": None,
                "team_mascot": None,
                "power_conference": None,
                "team_logo_url": None,
                "primary_color": None,
                "alternate_color": None
            }
            
            load_game_data(game)
            ld.load_team(away_team)



def extract_and_load_teams(league: str, distinct_teams: list[dict], espn_team_endpoint: str):
    """Method to perfom ETL process for teams data from various sources"""
    for distinct_team in distinct_teams:
        distinct_team = {key.lower(): value for key, value in distinct_team.items()}
        print(f"\n\nProcessing {league} Team {distinct_team['team_id']}")
        espn_team_json: dict = get_espn_team(f"{espn_team_endpoint}/{distinct_team['espn_code']}")
        team: Team = Team()
        team_id: str = et.extract_team_id(espn_team_json)

        if league == "CFB":
            team_stats_page_url: str = f"https://www.cbssports.com/college-football/teams/{distinct_team['cbs_code']}/stats/"
        else: # league == "NFL"
            team_stats_page_url: str = f"https://www.cbssports.com/nfl/teams/{distinct_team['cbs_code']}/stats/"
        cbs_team_stats_soup: BeautifulSoup = scrape_cbs_team_stats(team_stats_page_url)

        team.team_id = team_id
        team.league = distinct_team['league']
        team.cbs_code = distinct_team['cbs_code']
        team.espn_code = distinct_team['espn_code']
        team.fox_code = ""
        team.vegas_code = ""
        team.conference_code = et.extract_conference_code(espn_team_json)
        team.conference_name = et.extract_conference_name(espn_team_json)
        team.division_name = et.extract_division_name(espn_team_json)
        team.team_name = et.extract_team_name(espn_team_json)
        team.team_mascot = et.extract_team_mascot(espn_team_json)
        team.power_conference = et.is_power_conference(team.conference_name)
        team.team_logo_url = et.extract_logo_url(espn_team_json)
        team.primary_color = et.extract_primary_color(espn_team_json)
        team.alternate_color = et.extract_alternate_color(espn_team_json)
        team.conference_wins = 0
        team.conference_losses = 0
        team.conference_ties = 0
        team.overall_wins = 0
        team.overall_losses = 0
        team.overall_ties = 0
        
        if league == "CFB" and team.espn_code not in ["107", "2447", "2027"]:
            team.pass_attempts = cts.get_team_pass_attempts(cbs_team_stats_soup)
            team.opp_pass_attempts = cts.get_opp_pass_attempts(cbs_team_stats_soup)
            team.pass_completions = cts.get_team_pass_completions(cbs_team_stats_soup)
            team.opp_pass_completions = cts.get_opp_pass_completions(cbs_team_stats_soup)
            team.completion_percentage = cts.get_team_completion_percentage(cbs_team_stats_soup)
            team.opp_completion_percentage = cts.get_opp_completion_percentage(cbs_team_stats_soup)
            team.pass_yards = cts.get_team_pass_yards(cbs_team_stats_soup)
            team.opp_pass_yards = cts.get_opp_pass_yards(cbs_team_stats_soup)
            team.pass_touchdowns = cts.get_team_passing_touchdowns(cbs_team_stats_soup)
            team.opp_pass_touchdowns = cts.get_opp_passing_touchdowns(cbs_team_stats_soup)
            team.offense_interceptions = cts.get_team_offense_interceptions(cbs_team_stats_soup)
            team.defense_interceptions = cts.get_team_defense_interceptions(cbs_team_stats_soup)
            team.rush_yards = cts.get_team_rush_yards(cbs_team_stats_soup)
            team.opp_rush_yards = cts.get_opp_rush_yards(cbs_team_stats_soup)
            team.rush_attempts = cts.get_team_rush_attempts(cbs_team_stats_soup)
            team.opp_rush_attempts = cts.get_opp_rush_attempts(cbs_team_stats_soup)
            team.yards_per_rush = cts.get_team_yard_per_rush(cbs_team_stats_soup)
            team.opp_yards_per_rush = cts.get_opp_yard_per_rush(cbs_team_stats_soup)
            team.rush_touchdowns = cts.get_team_rush_touchdowns(cbs_team_stats_soup)
            team.opp_rush_touchdowns = cts.get_opp_rush_touchdowns(cbs_team_stats_soup)
        else:
            team.pass_attempts = None
            team.opp_pass_attempts = None
            team.pass_completions = None
            team.opp_pass_completions = None
            team.completion_percentage = None
            team.opp_completion_percentage = None
            team.pass_yards = None
            team.opp_pass_yards = None
            team.pass_touchdowns = None
            team.opp_pass_touchdowns = None
            team.offense_interceptions = None
            team.defense_interceptions = None
            team.rush_yards = None
            team.opp_rush_yards = None
            team.rush_attempts = None
            team.opp_rush_attempts = None
            team.yards_per_rush = None
            team.opp_yards_per_rush = None
            team.rush_touchdowns = None
            team.opp_rush_touchdowns = None

        load_team_data(team)

