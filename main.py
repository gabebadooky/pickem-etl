from etl import etl

cfb_weeks = 14
cfb_espn_scoreboard_endpoint = f'https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?seasontype=2&week='
cfb_espn_team_endpoint = f'http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/'

nfl_weeks = 18
nfl_espn_scoreboard_endpoint = f"http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?seasontype=2&week="
nfl_espn_team_endpoint = f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/"

def full_etl(league: str, weeks: int, espn_scoreboard_endpoint: str, espn_team_endpoint: str):
    teams_set = etl.extract_and_load_games(league, weeks, espn_scoreboard_endpoint)
    etl.extract_and_load_teams(league, teams_set, espn_team_endpoint)

def incremental_etl(league: str, weeks: int, espn_scoreboard_endpoint: str):
    etl.extract_and_load_games(league, weeks, espn_scoreboard_endpoint)


# CFB Full ETL
# full_etl("CFB", cfb_weeks, cfb_espn_scoreboard_endpoint, cfb_espn_team_endpoint)

# CFB Incremental ETL
# incremental_etl("CFB", cfb_weeks, cfb_espn_scoreboard_endpoint)

# NFL Full ETL
full_etl("NFL", nfl_weeks, nfl_espn_scoreboard_endpoint, nfl_espn_team_endpoint)

# NFL Incremental ETL
# incremental_etl("NFL", nfl_weeks, nfl_espn_scoreboard_endpoint)