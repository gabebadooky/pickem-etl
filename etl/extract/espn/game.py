from etl.extract import geocodes as l

class Game:
    def __init__(self, event, league):
        self.game_id = event['id']
        self.league = league
        self.week = event['week']['number']
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

def extract_game_week(data: dict) -> int:
    try:
        week = data['week']['number']
    except:
        print(f'Error occurred extracting week for game {data["id"]}')
        week = -1
    return week

def extract_datetime(data: dict) -> str:
    try:
        zulu_datetime = str(data['competitions'][0]['date'].split('T')[1])[:-1]
    except:
        print(f'Error occurred extracting zulu gametime for game {data["id"]}')
        zulu_datetime = ''
    return zulu_datetime

def extract_gamedate(data: dict) -> str:
    try:
        gamedate = str(data['competitions'][0]['date'].split('T')[0])
    except:
        print(f'Error occurred extracting gamedate for game {data["id"]}')
        gamedate = ''
    return gamedate

def get_teams(data: dict) -> dict:
    try:
        team1_home_away = str(data['competitions'][0]['competitors'][0]['homeAway'])
        team2_home_away = str(data['competitions'][0]['competitors'][1]['homeAway'])
        team1_id = str(data['competitions'][0]['competitors'][0]['id'])
        team2_id = str(data['competitions'][0]['competitors'][1]['id'])
        teams = {
            team1_home_away: team1_id,
            team2_home_away: team2_id
        }
    except:
        print(f'Error occurred extracting teams for game {data["id"]}')
        teams = {'away':'0', 'home':'0'}
    return teams

def extract_away_team(data: dict) -> str:
    try:
        teams = get_teams(data)
        away_team_id = teams['away']
    except:
        print(f'Error occurred extracting away_team for game {data["id"]}')
        away_team_id = '0'
    return away_team_id

def extract_home_team(data: dict) -> str:
    try:
        teams = get_teams(data)
        home_team_id = teams['home']
    except:
        print(f'Error occurred extracting home_team for game {data["id"]}')
        home_team_id = '0'
    return home_team_id

def extract_broadcast(data: dict) -> str:
    try:
        broadcast = str(data['competitions'][0]['broadcast'])
    except:
        print(f'Error occurred extracting broadcast for game {data["id"]}')
        broadcast = ''
    return broadcast

def extract_game_finished(data: dict) -> int:
    try:
        game_completed = 0 if str(data['competitions'][0]['status']['type']['completed']) == 'true' else 1
    except:
        print(f'Error occurred extracting game_finished for game {data["id"]}')
        game_completed = 1
    return game_completed

def extract_over_under(data: dict) -> str:
    try:
        over_under = str(data['competitions'][0]['odds'][0]['overUnder'])
    except:
        print(f'Error occurred extracting over_under for game {data["id"]}')
        over_under = '0'
    return over_under

def extract_spread(data: dict) -> int:
    try:
        spread = int(data['odds'][0]['spread'])
    except:
        print(f'Error occurred extracting spread for game {data["id"]}')
        spread = 0
    return spread

def extract_away_spread(data: dict) -> str:
    try:
        spread = extract_spread(data)
        away_spread = f'+{str(spread)}' if spread > 0 else str(spread)
    except:
        print(f'Error occurred extracting away_spread for game {data["id"]}')
        away_spread = '0'
    return away_spread

def extract_home_spread(data: dict) -> str:
    try:
        spread = extract_spread(data)
        home_spread = f'+{str(spread)}' if spread > 0 else str(spread)
    except:
        print(f'Error occurred extracting home_spread for game {data["id"]}')
        home_spread = '0'
    return home_spread

def extract_away_moneyline(data: dict) -> str:
    try:
        away_moneyline = data['odds']
    except:
        print(f'Error occurred extracting away moneyline for game {data["id"]}')
        away_moneyline = ''
    return away_moneyline

def extract_home_moneyline(data: dict) -> str:
    try:
        home_moneyline = data['odds']
    except:
        print(f'Error occurred extracting home moneyline for game {data["id"]}')
        home_moneyline = ''
    return home_moneyline

def extract_stadium(data: dict) -> str:
    try:
        stadium = data['competitions'][0]['venue']['fullName']
    except:
        print(f'Error occurred extracting stadium for game {data["id"]}')
        stadium = ''
    return stadium

def extract_state(data: dict) -> str:
    try:
        state = data['competitions'][0]['venue']['address']['state']
    except:
        print(f'Error occurred extracting state for game {data["id"]}')
        state = ''
    return state

def extract_city(data: dict) -> str:
    try:
        city = data['competitions'][0]['venue']['address']['city']
    except:
        print(f'Error occurred extracting city for game {data["id"]}')
        city = ''
    return city
