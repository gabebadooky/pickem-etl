from etl.extract.game import Game
from etl.extract.team import Team

def game(game: Game) -> dict:
    """Method to transform game object into Game dictionary for database load"""
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
        game_finished = game.finished
    )
    return game_dict

def away_box_score(game: Game) -> dict:
    """Method to transform game object into Away Box Score dictionary for database load"""
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

def home_box_score(game: Game) -> dict:
    """Method to transform game object into Home Box Score dictionary for database load"""
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

def odds(game: Game) -> list[dict]:
    """Method to transform game object into Odds dictionary for database load"""
    espn_odds: dict = dict(
        game_id = game.game_id,
        game_code = game.espn_code,
        source = "ESPN",
        espn_away_moneyline = game.espn_away_moneyline,
        espn_home_moneyline = game.espn_home_moneyline,
        away_spread = game.espn_away_spread,
        espn_home_spread = game.espn_home_spread,
        espn_over_under = game.espn_over_under,
        espn_away_win_percentage = game.espn_away_win_percentage,
        espn_home_win_percentage = game.espn_home_win_percentage
    )
    cbs_odds: dict = dict(
        game_id = game.game_id,
        game_code = game.cbs_code,
        source = "CBS",
        cbs_away_moneyline = game.cbs_away_moneyline,
        cbs_home_moneyline = game.cbs_home_moneyline,
        cbs_away_spread = game.cbs_away_spread,
        cbs_home_spread = game.cbs_home_spread,
        cbs_over_under = game.cbs_over_under,
        cbs_away_win_percentage = game.cbs_away_win_percentage,
        cbs_home_win_percentage = game.cbs_home_win_percentage
    )
    fox_odds: dict = dict(
        game_id = game.game_id,
        game_code = game.fox_code,
        source = "FOX",
        fox_away_moneyline = game.fox_away_moneyline,
        fox_home_moneyline = game.fox_home_moneyline,
        fox_away_spread = game.fox_away_spread,
        fox_home_spread = game.fox_home_spread,
        fox_over_under = game.fox_over_under,
        fox_away_win_percentage = game.fox_away_win_percentage,
        fox_home_win_percentage = game.fox_home_win_percentage
    )
    return [espn_odds, cbs_odds, fox_odds]

def location(game: Game) -> dict:
    """Method to transform game object into Location dictionary for database load"""
    location = dict(
        stadium = game.stadium,
        city = game.city,
        state = game.state,
        latitude = game.latitude,
        longitude = game.longitude,
    )
    return location

def team(team: Team) -> dict:
    """Method to transform team object into Team dictionary for database load"""
    team_dict = dict(
        team_id = team.team_id,
        league = team.league,
        cbs_code = team.cbs_code,
        espn_code = team.espn_code,
        fox_code = team.fox_code,
        vegas_code = team.vegas_code,
        conference_code = team.conference_code,
        conference_name = team.conference_name,
        division_name = team.division_name,
        team_name = team.team_name,
        team_mascot = team.team_mascot,
        power_conference = team.power_conference,
        team_logo_url = team.team_logo_url,
        primary_color = team.primary_color,
        alternate_color = team.alternate_color,
        ranking = team.ranking
    )
    return team_dict

def conference_record(team: Team) -> dict:
    """Method to transform team object into Conference Record dictionary for database load"""
    conference_record = dict(
        team_id = team.team_id,
        record_type = "CONFERENCE",
        wins = team.conference_wins,
        losses = team.conference_losses,
        ties = team.conference_ties
    )
    return conference_record

def overall_record(team: Team) -> dict:
    """Method to transform team object into Overall Record dictionary for database load"""
    overall_record = dict(
        team_id = team.team_id,
        record_type = "OVERALL",
        wins = team.overall_wins,
        losses = team.overall_losses,
        ties = team.overall_ties
    )
    return overall_record

def team_stats(team: Team) -> list:
    """Method to transform team object into Team Stats list for database load"""
    team_stats: list = []
    stat_types = ["pass_attempts", "opp_pass_attempts",
                  "pass_completions", "opp_pass_completions",
                  "completion_percentage", "opp_completion_percentage",
                  "pass_yards", "opp_pass_yards",
                  "pass_touchdowns", "opp_pass_touchdowns",
                  "offense_interceptions", "defense_interceptions",
                  "rush_yards", "opp_rush_yards",
                  "rush_attempts", "opp_rush_attempts",
                  "yards_per_rush", "opp_yards_per_rush",
                  "rush_touchdowns", "opp_rush_touchdowns"]
    
    for stat_type in stat_types:
        team_stats.append({
            "team_id": team.team_id,
            "type": stat_type,
            "value": getattr(team, stat_type)
        })
    return team_stats