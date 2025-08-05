from etl import etl
from etl.load import mysql_db as db

year: str = "2025"

cfb_weeks: int = 14
cfb_espn_scoreboard_endpoint: str = f"https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?seasontype=2&week="
cfb_espn_team_endpoint: str = f"http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams"
cfb_cbs_scoreboard_week_url: str = f"https://www.cbssports.com/college-football/scoreboard/FBS/{year}/regular"
cfb_fox_schedule_week_url: str = f"https://www.foxsports.com/college-football/schedule?groupId=2&seasonType=reg&week="

nfl_weeks: int = 18
nfl_espn_scoreboard_endpoint: str = f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?seasontype=2&dates={year}&week="
nfl_espn_team_endpoint: str = f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams"
nfl_cbs_scoreboard_week_url: str = f"https://www.cbssports.com/nfl/scoreboard/all/{year}/regular"
nfl_fox_schedule_week_url: str = f"https://www.foxsports.com/nfl/schedule?groupId=2&seasonType=reg&week="



def full_etl(league: str, weeks: int, espn_scoreboard_endpoint: str, espn_team_endpoint: str, cbs_scoreboard_week_url: str, fox_schedule_week_url: str):
    """Method to perfrom ETL process for both games and teams from all data sources"""
    etl.extract_and_load_games(league, weeks, espn_scoreboard_endpoint, cbs_scoreboard_week_url, fox_schedule_week_url)
    distinct_teams: list[dict] = db.get_distinct_teams(league)
    etl.extract_and_load_teams(league, distinct_teams, espn_team_endpoint)

def incremental_etl(league: str, weeks: int, espn_scoreboard_endpoint: str, cbs_scoreboard_week_url: str, fox_schedule_week_url: str):
    """Method to perfrom ETL process only for games from all data sources"""
    etl.extract_and_load_games(league, weeks, espn_scoreboard_endpoint, cbs_scoreboard_week_url, fox_schedule_week_url)


# CFB Full ETL
full_etl("CFB", cfb_weeks, cfb_espn_scoreboard_endpoint, cfb_espn_team_endpoint, cfb_cbs_scoreboard_week_url, cfb_fox_schedule_week_url)

# CFB Incremental ETL
#incremental_etl("CFB", cfb_weeks, cfb_espn_scoreboard_endpoint, cfb_cbs_scoreboard_week_url, cfb_fox_schedule_week_url)

# NFL Full ETL
#full_etl("NFL", nfl_weeks, nfl_espn_scoreboard_endpoint, nfl_espn_team_endpoint, nfl_cbs_scoreboard_week_url)

# NFL Incremental ETL
# incremental_etl("NFL", nfl_weeks, nfl_espn_scoreboard_endpoint, nfl_cbs_scoreboard_week_url)