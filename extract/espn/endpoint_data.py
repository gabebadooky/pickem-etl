import game as g
import team as t
import extract.geocodes as l

def get_scoreboard_data(event):
    stadium = g.extract_stadium(event)
    city = g.extract_city(event)
    state = g.extract_state(event)
    lat, lon = l.get_lat_long_tuple(stadium, city, state)

    scoreboard = dict(
        game_id = event['id'],
        league = 'CFB',
        week = event['week']['number'],
        cbs_code = '',
        espn_code = event['id'],
        fox_code = '',
        vegas_code = '',
        away_team_id = g.extract_away_team(event),
        home_team_id = g.extract_home_team(event),
        date = g.extract_gamedate(event),
        time = g.extract_datetime(event),
        tv_coverage = g.extract_broadcast(event),
        game_finished = g.extract_game_finished(event),
        away_q1_score = 0,
        away_q2_score = 0,
        away_q3_score = 0,
        away_q4_score = 0,
        away_overtime_score = 0,
        away_total_score = 0,
        home_q1_score = 0,
        home_q2_score = 0,
        home_q3_score = 0,
        home_q4_score = 0,
        home_overtime_score = 0,
        home_total_score = 0,
        away_moneyline = g.extract_away_moneyline(event),
        home_moneyline = g.extract_home_moneyline(event),
        away_spread = g.extract_away_spread(event),
        home_spread = g.extract_home_spread(event),
        over_under = g.extract_over_under(event),
        away_win_percentage = '',
        home_win_percentage = '',
        stadium = stadium,
        city = city,
        state = state,
        latitude = lat,
        longitude = lon
    )
    return scoreboard


def get_team_data(data):
    team_id = data['team']['id']
    conference_name = t.extract_conference_name(data)
    team = dict(
        team_id = team_id,
        cbs_code = '',
        espn_code = team_id,
        fox_code = '',
        vegas_code = '',
        conference_code = t.extract_conference_code(data),
        conference_name = conference_name,
        division_name = t.extract_division_name(data),
        team_name = t.extract_team_name(data),
        team_mascot = t.extract_team_mascot(data),
        # Treat Notre Dame as Power 4...
        g5_conference = False if team_id == '87' else t.is_g5_conference(conference_name),
        team_logo_url = t.extract_logo_url(data),
        conference_wins = 0,
        conference_losses = 0,
        conference_ties = 0,
        overall_wins = 0,
        overall_losses = 0,
        overall_ties = 0,
        pass_attempts = 0,
        opp_pass_attempts = 0,
        pass_completions = 0,
        opp_pass_completions = 0,
        completion_percentage = 0,
        opp_completion_percentage = 0,
        pass_yards = 0,
        opp_pass_yards = 0,
        pass_touchdowns = 0,
        opp_pass_touchdowns = 0,
        offense_interceptions = 0,
        defense_interceptions = 0,
        rush_yards = 0,
        opp_rush_yards = 0,
        rush_attempts = 0,
        opp_rush_attempts = 0,
        yards_per_rush = 0,
        opp_yards_per_rush = 0,
        rush_touchdowns = 0,
        opp_rush_touchdowns = 0
    )
    return team