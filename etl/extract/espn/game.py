def extract_game_id(data: dict) -> str:
    return data['name'].replace('é', 'e').replace('&', '').replace('.', '').replace(' ', '-').replace('(', '').replace(')', '').lower()

def extract_game_week(data: dict) -> int:
    if hasattr(data['week'], 'number'):
        return data['week']['number']
    else:
        return -1

def extract_datetime(data: dict) -> str:
    try:
        return str(data['competitions'][0]['date'].split('T')[1][:-1])
    except:
        return None

def extract_gamedate(data: dict) -> str:
    try:
        return str(data['competitions'][0]['date'].split('T')[0])
    except:
        return None

def get_teams(data: dict) -> dict:
    try:
        team1_home_away = str(data['competitions'][0]['competitors'][0]['homeAway'])
        team2_home_away = str(data['competitions'][0]['competitors'][1]['homeAway'])
        team1_id = str(data['competitions'][0]['competitors'][0]['id'])
        team2_id = str(data['competitions'][0]['competitors'][1]['id'])
        return {
            team1_home_away: team1_id,
            team2_home_away: team2_id
        }
    except:
        return {'away': '0', 'home': '0'}

def extract_away_team(data: dict) -> str:
    try:
        away_team_id = data['name'].split(' at ')[0].replace('é', 'e').replace('&', '').replace('.', '').replace(' ', '-').replace('(', '').replace(')', '').lower()
    except:
        print(f'Error occurred extracting away_team for game {extract_game_id(data)}')
        away_team_id = 'away-team'
    return away_team_id

def extract_home_team(data: dict) -> str:
    try:
        home_team_id = data['name'].split(' at ')[1].replace('é', 'e').replace('&', '').replace('.', '').replace(' ', '-').replace('(', '').replace(')', '').lower()
    except:
        print(f'Error occurred extracting home_team for game {extract_game_id(data)}')
        home_team_id = 'home-team'
    return home_team_id

def extract_broadcast(data: dict) -> str:
    try:
        return str(data['competitions'][0]['broadcast'])
    except:
        return None

def extract_game_finished(data: dict) -> int:
    try:
        if str(data['competitions'][0]['status']['type']['completed']) == 'true':
            return 0
        else:
            return 1
    except:
        return 1

def extract_over_under(data: dict) -> str:
    try:
        return str(data['competitions'][0]['odds'][0]['overUnder'])
    except:
        return None

def extract_spread(data: dict) -> int:
    try:
        return int(data['competitions'][0]['odds'][0], 'spread')
    except:
        return None

def extract_away_spread(data: dict) -> str:
    try:
        spread = extract_spread(data)
        return f'+{str(spread)}' if spread > 0 else str(spread)
    except:
        return None

def extract_home_spread(data: dict) -> str:
    try:
        spread = extract_spread(data)
        return f'+{str(spread)}' if spread < 0 else str(spread)
    except:
        return None

def extract_moneyline(data: dict) -> str:
    try:
        return data['competitions'][0]['odds'][0]['details']
    except:
        return None

def extract_away_moneyline(data: dict) -> str:
    try:
        spread = extract_spread(data)
        return f'+{str(spread)}' if spread > 0 else str(spread)
    except:
        return None

def extract_home_moneyline(data: dict) -> str:
    try:
        spread = extract_spread(data)
        return f'+{str(spread)}' if spread < 0 else str(spread)
    except:
        return None

def extract_stadium(data: dict) -> str:
    try:
        return data['competitions'][0]['venue']['fullName']
    except:
        return None

def extract_state(data: dict) -> str:
    try:
        return data['competitions'][0]['venue']['address']['state']
    except:
        return None

def extract_city(data: dict) -> str:
    try:
        return data['competitions'][0]['venue']['address']['city']
    except:
        return None

