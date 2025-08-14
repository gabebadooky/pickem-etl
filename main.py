from etl import etl
from etl.load import mysql_db as db

year: str = "2025"
current_week: tuple = (0, 1)

cfb_season_properties: dict = {
    "league": "CFB",
    "weeks": 14,
    "espn_scoreboard_endpoint": f"https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?seasontype=2&week=",
    "espn_team_endpoint": f"http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams",
    "cbs_scoreboard_week_url": f"https://www.cbssports.com/college-football/scoreboard/FBS/{year}/regular",
    "cbs_odds_week_url": f"https://www.cbssports.com/college-football/odds/FBS/2025/regular/week-",
    "cbs_team_endpoint": f"https://www.cbssports.com/college-football/teams",
    "fox_schedule_week_url": f"https://www.foxsports.com/college-football/schedule?groupId=2&seasonType=reg&week="
}

nfl_season_properties: dict = {
    "league": "NFL",
    "weeks": 18,
    "espn_scoreboard_endpoint": f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?seasontype=2&dates={year}&week=",
    "espn_team_endpoint": f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams",
    "cbs_scoreboard_week_url": f"https://www.cbssports.com/nfl/scoreboard/all/{year}/regular",
    "cbs_odds_week_url": f"https://www.cbssports.com/nfl/odds/2025/regular/week-",
    "cbs_team_endpoint": f"https://www.cbssports.com/nfl/teams",
    "fox_schedule_week_url": f"https://www.foxsports.com/nfl/schedule?groupId=2&seasonType=reg&week="
}


def full_etl():
    for week in range(cfb_season_properties['weeks'] + 1):
        etl.extract_transform_load_games(week, cfb_season_properties)
    etl.extract_transform_load_teams(cfb_season_properties)

    for week in range(nfl_season_properties['weeks']):
        etl.extract_transform_load_games(week, nfl_season_properties)
    etl.extract_transform_load_teams(nfl_season_properties)


def incremental_etl():
    etl.extract_transform_load_games(current_week[0], cfb_season_properties)
    etl.extract_transform_load_games(current_week[1], nfl_season_properties)



# full_etl()
etl.extract_transform_load_teams(nfl_season_properties)

