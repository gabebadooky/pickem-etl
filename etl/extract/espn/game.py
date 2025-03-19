from etl.extract import geocodes as l

class Game:
    def __init__(self, event, league):
        self.game_id = extract_game_id(event)
        self.league = league
        self.week = event['week']['number']
        self.year = event['season']['year']
        self.cbs_code = ''
        self.espn_code = event['id']
        self.fox_code = ''
        self.vegas_code = ''
        self.away_team_id = extract_away_team(event)
        self.home_team_id = extract_home_team(event)
        self.date = extract_gamedate(event)
        self.time = extract_datetime(event)
        self.tv_coverage = extract_broadcast(event)
        self.game_finished = extract_game_finished(event)
        self.away_q1_score = 0
        self.away_q2_score = 0
        self.away_q3_score = 0
        self.away_q4_score = 0
        self.away_overtime_score = 0
        self.away_total_score = 0
        self.home_q1_score = 0
        self.home_q2_score = 0
        self.home_q3_score = 0
        self.home_q4_score = 0
        self.home_overtime_score = 0
        self.home_total_score = 0
        self.away_moneyline = extract_away_moneyline(event)
        self.home_moneyline = extract_home_moneyline(event)
        self.away_spread = extract_away_spread(event)
        self.home_spread = extract_home_spread(event)
        self.over_under = extract_over_under(event)
        self.away_win_percentage = ''
        self.home_win_percentage = ''
        self.stadium = extract_stadium(event)
        self.city = extract_city(event)
        self.state = extract_state(event)
        self.latitude = l.get_lat_long_tuple(extract_stadium(event), extract_city(event), extract_state(event))[0]
        self.longitude = l.get_lat_long_tuple(extract_stadium(event), extract_city(event), extract_state(event))[0]


def extract_game_id(data: dict) -> str:
    return data['name'].replace(' ', '-').replace('\'', '')

def extract_game_week(data: dict) -> int:
    if hasattr(data['week'], 'number'):
        return data['week']['number']
    else:
        return -1

def extract_datetime(data: dict) -> str:
    if hasattr(data['competitions'][0], 'date'):
        return str(data['competitions'][0]['date'].split('T')[1][:-1])
    else:
        return ''

def extract_gamedate(data: dict) -> str:
    if hasattr(data['competitions'][0], 'date'):
        return str(data['competitions'][0]['date'].split('T')[0])
    else:
        return ''

def get_teams(data: dict) -> dict:
    if (
        hasattr(data['competitions'][0]['competitors'][0], 'homeAway') and 
        hasattr(data['competitions'][0]['competitors'][1], 'homeAway') and 
        hasattr(data['competitions'][0]['competitors'][0], 'id') and 
        hasattr(data['competitions'][0]['competitors'][1], 'id')
        ):
        team1_home_away = str(data['competitions'][0]['competitors'][0]['homeAway'])
        team2_home_away = str(data['competitions'][0]['competitors'][1]['homeAway'])
        team1_id = str(data['competitions'][0]['competitors'][0]['id'])
        team2_id = str(data['competitions'][0]['competitors'][1]['id'])
        return {
            team1_home_away: team1_id,
            team2_home_away: team2_id
        }
    else:
        return {'away':'0', 'home':'0'}

def extract_away_team(data: dict) -> str:
    try:
        teams = get_teams(data)
        away_team_id = teams['away']
    except:
        print(f'Error occurred extracting away_team for game {extract_game_id(data)}')
        away_team_id = '0'
    return away_team_id

def extract_home_team(data: dict) -> str:
    try:
        teams = get_teams(data)
        home_team_id = teams['home']
    except:
        print(f'Error occurred extracting home_team for game {extract_game_id(data)}')
        home_team_id = '0'
    return home_team_id

def extract_broadcast(data: dict) -> str:
    if hasattr(data['competitions'][0], 'broadcast'):
        return str(data['competitions'][0]['broadcast'])
    else:
        return ''

def extract_game_finished(data: dict) -> int:
    if hasattr(data['competitions'][0]['status']['type'], 'completed'):
        return 0 if str(data['competitions'][0]['status']['type']['completed']) == 'true' else 1
    else:
        return 1

def extract_over_under(data: dict) -> str:
    if hasattr(data['competitions'][0], 'odds') and hasattr(data['competitions'][0]['odds'][0], 'overUnder'):
        return str(data['competitions'][0]['odds'][0]['overUnder'])
    else:
        return '0'

def extract_spread(data: dict) -> int:
    if hasattr(data['competitions'][0], 'odds') and hasattr(data['competitions'][0]['odds'][0], 'spread'):
        return int(data['competitions'][0]['odds'][0], 'spread')
    else:
        return 0

def extract_away_spread(data: dict) -> str:
    try:
        spread = extract_spread(data)
        return f'+{str(spread)}' if spread > 0 else str(spread)
    except:
        return '0'

def extract_home_spread(data: dict) -> str:
    try:
        spread = extract_spread(data)
        return f'+{str(spread)}' if spread < 0 else str(spread)
    except:
        return '0'

def extract_moneyline(data: dict) -> str:
    if hasattr(data['competitions'][0], 'odds') and hasattr(data['competitions'][0]['odds'][0], 'details'):
        return data['competitions'][0]['odds'][0]['details']
    else:
        return ''

def extract_away_moneyline(data: dict) -> str:
    try:
        spread = extract_spread(data)
        return f'+{str(spread)}' if spread > 0 else str(spread)
    except:
        return '0'

def extract_home_moneyline(data: dict) -> str:
    try:
        spread = extract_spread(data)
        return f'+{str(spread)}' if spread < 0 else str(spread)
    except:
        return '0'

def extract_stadium(data: dict) -> str:
    if hasattr(data['competitions'][0]['venue'], 'fullName'):
        return data['competitions'][0]['venue']['fullName']
    else:
        return ''

def extract_state(data: dict) -> str:
    if hasattr(data['competitions'][0]['venue']['address'], 'state'):
        return data['competitions'][0]['venue']['address']['state']
    else:
        return ''

def extract_city(data: dict) -> str:
    if hasattr(data['competitions'][0]['venue']['address'], 'city'):
        return data['competitions'][0]['venue']['address']['city']
    else:
        return ''
