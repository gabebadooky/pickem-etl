from datetime import date
from etl import etl
from etl.load import mysql_db as db
import schedule, time

year: str = "2025"

season_weeks = [
    {"start": date(2025, 8, 19), "end": date(2025, 8, 25)},
    {"start": date(2025, 8, 26), "end": date(2025, 9, 1)},
    {"start": date(2025, 9, 2), "end": date(2025, 9, 8)},
    {"start": date(2025, 9, 9), "end": date(2025, 9, 15)},
    {"start": date(2025, 9, 16), "end": date(2025, 9, 22)},
    {"start": date(2025, 9, 23), "end": date(2025, 9, 29)},
    {"start": date(2025, 9, 30), "end": date(2025, 10, 6)},
    {"start": date(2025, 10, 7), "end": date(2025, 10, 13)},
    {"start": date(2025, 10, 14), "end": date(2025, 10, 20)},
    {"start": date(2025, 10, 21), "end": date(2025, 10, 27)},
    {"start": date(2025, 10, 28), "end": date(2025, 11, 3)},
    {"start": date(2025, 11, 4), "end": date(2025, 11, 10)},
    {"start": date(2025, 11, 11), "end": date(2025, 11, 17)},
    {"start": date(2025, 11, 18), "end": date(2025, 11, 24)},
    {"start": date(2025, 11, 25), "end": date(2025, 12, 1)},
    {"start": date(2025, 12, 2), "end": date(2025, 12, 8)},
    {"start": date(2025, 12, 9), "end": date(2025, 12, 15)},
    {"start": date(2025, 12, 16), "end": date(2025, 12, 22)},
    {"start": date(2025, 12, 23), "end": date(2025, 12, 29)},
]


def full_etl():
    db.toggle_system_maintenance_flag(True)

    for week in range(cfb_season_properties['weeks'] + 1):
        etl.extract_transform_load_games(week, cfb_season_properties)
    etl.extract_transform_load_teams(cfb_season_properties)

    for week in range(nfl_season_properties['weeks']):
        etl.extract_transform_load_games(week, nfl_season_properties)
    etl.extract_transform_load_teams(nfl_season_properties)

    db.toggle_system_maintenance_flag(False)


def cfb_games_incremental_etl():
    etl.extract_transform_load_games(cfb_season_properties["current_week"], cfb_season_properties)
    

def nfl_games_incremental_etl():
    etl.extract_transform_load_games(nfl_season_properties["current_week"], nfl_season_properties)


def cfb_teams_etl():
    etl.extract_transform_load_teams(cfb_season_properties)


def nfl_teams_etl():
    etl.extract_transform_load_teams(nfl_season_properties)


def calculate_current_week():
    today: date = date.today()
    for week in range(len(season_weeks)):
        current_week_begin_date: date = season_weeks[week - 1]["start"]
        current_week_end_date: date = season_weeks[week - 1]["end"]
        if current_week_begin_date <= today and today <= current_week_end_date:
            return week - 1
    return season_weeks[len(season_weeks)]


cfb_season_properties: dict = {
    "current_week": calculate_current_week(),
    "league": "CFB",
    "weeks": 14,
    "espn_scoreboard_endpoint": f"https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?groups=80&seasontype=2&week=",
    "espn_team_endpoint": f"http://site.api.espn.com/apis/site/v2/sports/football/college-football/teams",
    "cbs_scoreboard_week_url": f"https://www.cbssports.com/college-football/scoreboard/FBS/{year}/regular",
    "cbs_odds_week_url": f"https://www.cbssports.com/college-football/odds/FBS/2025/regular/week-",
    "cbs_team_endpoint": f"https://www.cbssports.com/college-football/teams",
    "fox_schedule_week_url": f"https://www.foxsports.com/college-football/schedule?groupId=2&seasonType=reg&week="
}

nfl_season_properties: dict = {
    "current_week": calculate_current_week() - 1,
    "league": "NFL",
    "weeks": 18,
    "espn_scoreboard_endpoint": f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?seasontype=2&dates={year}&week=",
    "espn_team_endpoint": f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams",
    "cbs_scoreboard_week_url": f"https://www.cbssports.com/nfl/scoreboard/all/{year}/regular",
    "cbs_odds_week_url": f"https://www.cbssports.com/nfl/odds/2025/regular/week-",
    "cbs_team_endpoint": f"https://www.cbssports.com/nfl/teams",
    "fox_schedule_week_url": f"https://www.foxsports.com/nfl/schedule?groupId=2&seasonType=reg&week="
}



# Monday ETL
schedule.every().monday.at("16:30").do(nfl_games_incremental_etl)
schedule.every().monday.at("17:30").do(nfl_games_incremental_etl)
schedule.every().monday.at("18:30").do(nfl_games_incremental_etl)
schedule.every().monday.at("19:30").do(nfl_games_incremental_etl)
schedule.every().monday.at("20:30").do(nfl_games_incremental_etl)
schedule.every().monday.at("21:30").do(nfl_games_incremental_etl)
schedule.every().monday.at("22:30").do(nfl_games_incremental_etl)
schedule.every().monday.at("23:30").do(nfl_teams_etl)

# Tuesday ETL
schedule.every().tuesday.at("16:00").do(cfb_games_incremental_etl)
schedule.every().tuesday.at("17:00").do(cfb_games_incremental_etl)
schedule.every().tuesday.at("18:00").do(cfb_games_incremental_etl)
schedule.every().tuesday.at("19:00").do(cfb_games_incremental_etl)
schedule.every().tuesday.at("20:00").do(cfb_games_incremental_etl)
schedule.every().tuesday.at("21:00").do(cfb_games_incremental_etl)
schedule.every().tuesday.at("22:00").do(cfb_games_incremental_etl)
schedule.every().tuesday.at("23:00").do(cfb_teams_etl)

# Wednesday ETL
schedule.every().wednesday.at("16:00").do(cfb_games_incremental_etl)
schedule.every().wednesday.at("17:00").do(cfb_games_incremental_etl)
schedule.every().wednesday.at("18:00").do(cfb_games_incremental_etl)
schedule.every().wednesday.at("19:00").do(cfb_games_incremental_etl)
schedule.every().wednesday.at("20:00").do(cfb_games_incremental_etl)
schedule.every().wednesday.at("21:00").do(cfb_games_incremental_etl)
schedule.every().wednesday.at("22:00").do(cfb_games_incremental_etl)
schedule.every().wednesday.at("23:00").do(cfb_teams_etl)

# Thursday ETL
schedule.every().thursday.at("16:00").do(cfb_games_incremental_etl)
schedule.every().thursday.at("16:30").do(nfl_games_incremental_etl)
schedule.every().thursday.at("17:00").do(cfb_games_incremental_etl)
schedule.every().thursday.at("17:30").do(nfl_games_incremental_etl)
schedule.every().thursday.at("18:00").do(cfb_games_incremental_etl)
schedule.every().thursday.at("18:30").do(nfl_games_incremental_etl)
schedule.every().thursday.at("19:00").do(cfb_games_incremental_etl)
schedule.every().thursday.at("19:30").do(nfl_games_incremental_etl)
schedule.every().thursday.at("20:00").do(cfb_games_incremental_etl)
schedule.every().thursday.at("20:30").do(nfl_games_incremental_etl)
schedule.every().thursday.at("21:00").do(cfb_games_incremental_etl)
schedule.every().thursday.at("21:30").do(nfl_games_incremental_etl)
schedule.every().thursday.at("22:00").do(cfb_games_incremental_etl)
schedule.every().thursday.at("22:30").do(nfl_games_incremental_etl)
schedule.every().thursday.at("23:00").do(cfb_teams_etl)
schedule.every().thursday.at("23:00").do(nfl_teams_etl)

# Friday ETL
schedule.every().friday.at("16:00").do(cfb_games_incremental_etl)
schedule.every().friday.at("17:00").do(cfb_games_incremental_etl)
schedule.every().friday.at("18:00").do(cfb_games_incremental_etl)
schedule.every().friday.at("19:00").do(cfb_games_incremental_etl)
schedule.every().friday.at("20:00").do(cfb_games_incremental_etl)
schedule.every().friday.at("21:00").do(cfb_games_incremental_etl)
schedule.every().friday.at("22:00").do(cfb_games_incremental_etl)
schedule.every().friday.at("22:30").do(nfl_games_incremental_etl)
schedule.every().friday.at("23:00").do(cfb_teams_etl)
schedule.every().friday.at("23:30").do(nfl_teams_etl)

# Saturday ETL
schedule.every().saturday.at("09:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("10:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("11:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("12:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("13:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("14:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("15:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("16:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("17:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("18:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("19:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("20:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("21:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("22:00").do(cfb_games_incremental_etl)
schedule.every().saturday.at("23:00").do(cfb_teams_etl)

# Sunday ETL
schedule.every().sunday.at("11:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("11:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("12:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("13:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("14:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("15:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("16:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("17:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("18:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("19:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("20:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("21:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("22:30").do(nfl_games_incremental_etl)
schedule.every().sunday.at("23:30").do(nfl_teams_etl)