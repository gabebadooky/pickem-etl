import requests
import game as g

def get_game_week_data(week_num: int) -> list:
    espn_scoreboard_endpoint = f'https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?seasontype=2&week={week_num}'
    data = requests.get(espn_scoreboard_endpoint).json()
    events = data['events']
    week_games = []
    for event in events:
        game = dict(
            # games
            game_id = event['id'],
            league = 'CFB',
            week = g.extract_game_week(event),
            cbs_code = '',
            espn_code = event['id'],
            fox_code = '',
            vegas_code = '',
            away_team_id = g.extract_away_team(event),
            home_team_id = g.extract_home_team(event),
            date = g.extract_gamedate(event),
            time = g.extract_datetime(event),
            tv_coverage = g.extract_broadcast(event),
            stadium = g.extract_stadium(event),
            city = g.extract_city(event),
            state = g.extract_state(event),
            game_finished = g.extract_game_finished(event),

            # odds
            source = 'ESPN',
            away_moneyline = g.extract_away_moneyline(event),
            home_moneyline = g.extract_home_moneyline(event),
            away_spread = g.extract_away_spread(event),
            home_spread = g.extract_home_spread(event),
            over_under = g.extract_over_under(event),
            #away_win_percentage,
            #home_win_percentage
        )
        week_games.append(game)
    return week_games