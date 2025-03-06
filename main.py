from etl import etl

cfb_weeks = 14

def full_etl():
    teams_set = etl.extract_and_load_games(cfb_weeks)
    etl.extract_and_load_teams(teams_set)

def incremental_etl():
    etl.extract_and_load_games(cfb_weeks)

full_etl()