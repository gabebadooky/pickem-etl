import requests
import game as g


def get_week_games(week_num: int) -> list:
    espn_scoreboard_endpoint = f'https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?seasontype=2&week={week_num}'
    data = requests.get(espn_scoreboard_endpoint).json()
    events = data['events']
    week_games = []

    for event in events:
        game_id = f'{g.extract_away_team(event)}-{g.extract_home_team(event)}-{g.extract_gamedate(event)}'

        game = dict(
            # game
            game_id = game_id,
            league = 'CFB',
            week = week_num,
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

            # box score
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

            # odds
            source = 'ESPN',
            away_moneyline = g.extract_away_moneyline(event),
            home_moneyline = g.extract_home_moneyline(event),
            away_spread = g.extract_away_spread(event),
            home_spread = g.extract_home_spread(event),
            over_under = g.extract_over_under(event),
            away_win_percentage = '',
            home_win_percentage = '',

            # location
            stadium = g.extract_stadium(event),
            city = g.extract_city(event),
            state = g.extract_state(event),
        )
        week_games.append(game)

    return week_games