def format_game(game: object) -> dict:
    game_dict = dict(
        game_id = game.game_id,
        league = game.league,
        week = game.week,
        year = game.year,
        cbs_code = game.cbs_code,
        espn_code = game.espn_code,
        fox_code = game.fox_code,
        vegas_code = game.vegas_code,
        away_team_id = game.away_team_id,
        home_team_id = game.home_team_id,
        date = game.date,
        time = game.time,
        tv_coverage = game.tv_coverage,
        stadium = game.stadium,
        city = game.city,
        game_finished = game.game_finished
    )
    return game_dict

def format_away_box_score(game: object) -> dict:
    away_box_score = dict(
        game_id = game.game_id,
        team_id = game.away_team_id,
        away_q1_score = game.away_q1_score,
        away_q2_score = game.away_q2_score,
        away_q3_score = game.away_q3_score,
        away_q4_score = game.away_q4_score,
        away_overtime_score = game.away_overtime_score,
        away_total_score = game.away_total_score
    )
    return away_box_score

def format_home_box_score(game: object) -> dict:
    home_box_score = dict(
        game_id = game.game_id,
        team_id = game.home_team_id,
        home_q1_score = game.home_q1_score,
        home_q2_score = game.home_q2_score,
        home_q3_score = game.home_q3_score,
        home_q4_score = game.home_q4_score,
        home_overtime_score = game.home_overtime_score,
        home_total_score = game.home_total_score
    )
    return home_box_score

def format_odds(game: object) -> dict:
    if len(game.espn_code) > 1:
        gamecode = game.espn_code
        source = 'ESPN'
    elif len(game.cbs_code) > 1:
        gamecode = game.cbs_code
        source = 'CBS'
    elif len(game.fox_code) > 1:
        gamecode = game.vegas_code
        source = 'FOX'
    else:
        gamecode = '0'
        source = 'ERR'

    odds = dict(
        game_id = game.game_id,
        game_code = gamecode,
        source = source,
        away_moneyline = game.away_moneyline,
        home_moneyline = game.home_moneyline,
        away_spread = game.away_spread,
        home_spread = game.home_spread,
        over_under = game.over_under,
        away_win_percentage = game.away_win_percentage,
        home_win_percentage = game.home_win_percentage
    )
    return odds

def format_location(game: object) -> dict:
    location = dict(
        stadium = game.stadium,
        city = game.city,
        state = game.state,
        latitude = game.latitude,
        longitude = game.longitude,
    )
    return location

def format_team(team: object) -> dict:
    team = dict(
        team_id = team.team_id,
        cbs_code = team.cbs_code,
        espn_code = team.espn_code,
        fox_code = team.fox_code,
        vegas_code = team.vegas_code,
        conference_code = team.conference_code,
        conference_name = team.conference_name,
        division_name = team.division_name,
        team_name = team.team_name,
        team_mascot = team.team_mascot,
        g5_conference = team.g5_conference,
        team_logo_url = team.team_logo_url,
        primary_color = team.primary_color,
        alternate_color = team.alternate_color
    )
    return team

def format_conference_record(team: object) -> dict:
    conference_record = dict(
        team_id = team.team_id,
        record_type = 'CONFERENCE',
        wins = team.conference_wins,
        losses = team.conference_losses,
        ties = team.conference_ties
    )
    return conference_record

def format_overall_record(team: object) -> dict:
    overall_record = dict(
        team_id = team.team_id,
        record_type = 'OVERALL',
        wins = 0,
        losses = 0,
        ties = 0
    )
    return overall_record

def format_team_stats(team: object) -> list:
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
            'team_id': team.team_id,
            'type': stat_type,
            'value': getattr(team, stat_type)
        })
    return team_stats