import zulu
from datetime import datetime

def format_game(scoreboard: dict) -> dict:
    game = dict(
        game_id = scoreboard['game_id'],
        league = scoreboard['league'],
        week = scoreboard['week'],
        cbs_code = scoreboard['cbs_code'],
        espn_code = scoreboard['espn_code'],
        fox_code = scoreboard['fox_code'],
        vegas_code = scoreboard['vegas_code'],
        away_team_id = scoreboard['away_team_id'],
        home_team_id = scoreboard['home_team_id'],
        date = None if scoreboard['date'] == 'TBD' else datetime.strptime(scoreboard['date'], '%Y-%m-%d'),
        time = None if scoreboard['time'] == 'TBD' else zulu.parse(scoreboard['time'][:-1], '%H:%M'),
        tv_coverage = scoreboard['tv_coverage'],
        game_finished = scoreboard['game_finished']
    )
    return game

def format_away_box_score(scoreboard: dict) -> dict:
    away_box_score = dict(
        game_id = scoreboard['game_id'],
        team_id = scoreboard['team_id'],
        away_q1_score = scoreboard['away_q1_score'],
        away_q2_score = scoreboard['away_q2_score'],
        away_q3_score = scoreboard['away_q3_score'],
        away_q4_score = scoreboard['away_q4_score'],
        away_overtime_score = scoreboard['away_overtime_score'],
        away_total_score = scoreboard['away_total_score']
    )
    return away_box_score

def format_home_box_score(scoreboard: dict) -> dict:
    home_box_score = dict(
        game_id = scoreboard['game_id'],
        team_id = scoreboard['team_id'],
        home_q1_score = scoreboard['home_q1_score'],
        home_q2_score = scoreboard['home_q2_score'],
        home_q3_score = scoreboard['home_q3_score'],
        home_q4_score = scoreboard['home_q4_score'],
        home_overtime_score = scoreboard['home_overtime_score'],
        home_total_score = scoreboard['home_total_score']
    )
    return home_box_score

def format_odds(scoreboard: dict) -> dict:
    odds = dict(
        game_id = scoreboard['game_id'],
        game_code = scoreboard['game_code'],
        source = scoreboard['source'],
        away_moneyline = scoreboard['away_moneyline'],
        home_moneyline = scoreboard['home_moneyline'],
        away_spread = scoreboard['away_spread'],
        home_spread = scoreboard['home_spread'],
        over_under = scoreboard['over_under'],
        away_win_percentage = scoreboard['away_win_percentage'],
        home_win_percentage = scoreboard['home_win_percentage']
    )
    return odds

def format_location(scoreboard: dict) -> dict:
    location = dict(
        stadium = scoreboard['stadium'],
        city = scoreboard['city'],
        state = scoreboard['state'],
        latitude = scoreboard['latitude'],
        longitude = scoreboard['longitude'],
    )
    return location

def format_team(team: dict) -> dict:
    team = dict(
        team_id = team['team_id'],
        cbs_code = team['cbs_code'],
        espn_code = team['espn_code'],
        fox_code = team['fox_code'],
        vegas_code = team['vegas_code'],
        conference_code = team['conference_code'],
        conference_name = team['conference_name'],
        division_name = team['division_name'],
        team_name = team['team_name'],
        team_mascot = team['team_mascot'],
        g5_conference = team['g5_conference'],
        team_logo_url = team['team_logo_url']
    )
    return team

def format_conference_record(team: dict) -> dict:
    conference_record = dict(
        team_id = team['team_id'],
        record_type = 'Conference',
        wins = team['conference_wins'],
        losses = team['conference_losses'],
        ties = team['conference_ties']
    )
    return conference_record

def format_overall_record(team: dict) -> dict:
    overall_record = dict(
        team_id = team['team_id'],
        record_type = 'Overall',
        wins = 0,
        losses = 0,
        ties = 0
    )
    return overall_record

def format_team_stats(team: dict) -> list:
    team_stats = []
    stat_types = ['pass_attempts', 'opp_pass_attempts',
                  'pass_completions', 'opp_pass_completions',
                  'completion_percentage', 'opp_completion_percentage',
                  'pass_yards', 'opp_pass_yards',
                  'pass_touchdowns', 'opp_pass_touchdowns',
                  'offense_interceptions', 'defense_interceptions',
                  'rush_yards', 'opp_rush_yards',
                  'rush_attempts', 'opp_rush_attempts',
                  'yards_per_rush', 'opp_yards_per_rush',
                  'rush_touchdowns', 'opp_rush_touchdowns']
    for stat_type in stat_types:
        team_stats.append({
            'team_id': team['team_id'],
            'type': stat_type,
            'value': team[stat_type]
        })
    return team_stats