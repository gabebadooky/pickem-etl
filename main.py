from etl import etl

cfb_weeks: int = 14
cfb_espn_scoreboard_endpoint: str = "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?seasontype=2&week="
cfb_espn_team_endpoint: str = "http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams"
cbs_scoreboard_week_url: str = "https://www.cbssports.com/college-football/scoreboard/FBS/2025/regular"

nfl_weeks: int = 18
nfl_espn_scoreboard_endpoint: str = f"http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?seasontype=2&week="
nfl_espn_team_endpoint: str = f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"

def full_etl(league: str, weeks: int, espn_scoreboard_endpoint: str, espn_team_endpoint: str, cbs_scoreboard_week_url: str):
    """Method to perfrom ETL process for both games and teams from all data sources"""
    teams_set: set = etl.extract_and_load_games(league, weeks, espn_scoreboard_endpoint, cbs_scoreboard_week_url)
    etl.extract_and_load_teams(league, teams_set, espn_team_endpoint)

def incremental_etl(league: str, weeks: int, espn_scoreboard_endpoint: str, cbs_scoreboard_week_url: str):
    """Method to perfrom ETL process only for games from all data sources"""
    etl.extract_and_load_games(league, weeks, espn_scoreboard_endpoint, cbs_scoreboard_week_url)


# CFB Full ETL
full_etl("CFB", cfb_weeks, cfb_espn_scoreboard_endpoint, cfb_espn_team_endpoint, cbs_scoreboard_week_url)

# CFB Incremental ETL
# incremental_etl("CFB", cfb_weeks, cfb_espn_scoreboard_endpoint, cbs_scoreboard_week_url)

# NFL Full ETL
# full_etl("NFL", nfl_weeks, nfl_espn_scoreboard_endpoint, nfl_espn_team_endpoint)

# NFL Incremental ETL
# incremental_etl("NFL", nfl_weeks, nfl_espn_scoreboard_endpoint)