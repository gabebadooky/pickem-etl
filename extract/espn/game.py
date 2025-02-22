def extract_game_week(data: dict) -> int:
    try:
        week = data['week']['number']
    except Exception as e:
        print(e)
        week = -1
    return week

def extract_datetime(data: dict) -> str:
    try:
        zulu_datetime = str(data['competitions'][0]['date'].split('T')[1])
    except Exception as e:
        print(e)
        zulu_datetime = 'TBD'
    return zulu_datetime

def extract_gamedate(data: dict) -> str:
    try:
        gamedate = str(data['competitions'][0]['date'].split('T')[0])
    except Exception as e:
        print(e)
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
    except Exception as e:
        print(e)
        teams = {'away':'0', 'home':'0'}
    return teams

def extract_away_team(data: dict) -> str:
    try:
        teams = get_teams(data)
        away_team_id = teams['away']
    except Exception as e:
        print(e)
        away_team_id = '0'
    return away_team_id

def extract_home_team(data: dict) -> str:
    try:
        teams = get_teams(data)
        home_team_id = teams['home']
    except Exception as e:
        print(e)
        home_team_id = '0'
    return home_team_id

def extract_broadcast(data: dict) -> str:
    try:
        broadcast = str(data['competitions'][0]['broadcast'])
    except Exception as e:
        print(e)
        broadcast = ''
    return broadcast

def extract_game_finished(data: dict) -> bool:
    try:
        game_completed = str(data['competitions'][0]['status']['type']['completed'])
    except Exception as e:
        print(e)
        game_completed = False
    return game_completed

def extract_over_under(data: dict) -> str:
    try:
        over_under = str(data['competitions'][0]['odds'][0]['overUnder'])
    except Exception as e:
        print(e)
        over_under = '0'
    return over_under

def extract_spread(data: dict) -> int:
    try:
        spread = int(data['odds'][0]['spread'])
    except Exception as e:
        print(e)
        spread = 0
    return spread

def extract_away_spread(data: dict) -> str:
    try:
        spread = extract_spread(data)
        away_spread = f'+{str(spread)}' if spread > 0 else str(spread)
    except Exception as e:
        print(e)
        away_spread = '0'
    return away_spread

def extract_home_spread(data: dict) -> str:
    try:
        spread = extract_spread(data)
        home_spread = f'+{str(spread)}' if spread > 0 else str(spread)
    except Exception as e:
        print(e)
        home_spread = '0'
    return home_spread

def extract_away_moneyline(data: dict) -> str:
    try:
        away_moneyline = data['odds']
    except Exception as e:
        print(e)
        away_moneyline = ''
    return away_moneyline

def extract_home_moneyline(data: dict) -> str:
    try:
        home_moneyline = data['odds']
    except Exception as e:
        print(e)
        home_moneyline = ''
    return home_moneyline

def extract_stadium(data: dict) -> str:
    try:
        stadium = data['competitions'][0]['venue']['fullName']
    except Exception as e:
        print(e)
        stadium = ''
    return stadium

def extract_state(data: dict) -> str:
    try:
        state = data['competitions'][0]['venue']['address']['state']
    except Exception as e:
        print(e)
        state = ''
    return state

def extract_city(data: dict) -> str:
    try:
        city = data['competitions'][0]['venue']['address']['city']
    except Exception as e:
        print(e)
        city = ''
    return city
