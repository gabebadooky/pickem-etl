import requests

def extract_team_name(data: dict) -> str:
    try:
        team_name = data['team']['location']
    except Exception as e:
        print(e)
        team_name = ''
    return team_name

def extract_team_mascot(data: dict) -> str:
    try:
        team_mascot = data['team']['name']
    except Exception as e:
        print(e)
        team_mascot = ''
    return team_mascot

def extract_conference_code(data: dict) -> str:
    try:
        conference_code = data['team']['groups']['id']
    except Exception as e:
        print(e)
        conference_code = ''
    return conference_code

def extract_conference_name(data: dict) -> str:
    try:
        conference_name = data['team']['standingSummary'].split(' in ')[1]
        if '-' in conference_name:
            conference_name = conference_name.split(' - ')[0]
        if 'AFC' in conference_name:
            conference_name = 'AFC'
        if 'NFC' in conference_name:
            conference_name = 'NFC'
    except Exception as e:
        print(e)
        conference_name = ''
    return conference_name

def extract_division_name(data: dict) -> str:
    try:
        division_name = data['team']['standingSummary'].split(' in ')[1]
        if '-' in division_name:
            division_name = division_name.split(' - ')[1]
        if 'AFC' not in division_name or 'NFC' not in division_name:
            division_name = ''
    except Exception as e:
        print(e)
        division_name = ''
    return division_name

def is_g5_conference(conference_name: str) -> bool:
    g5_conference = {
        'ACC': False,
        'American': True,
        'Big 12': False,
        'Big Ten': False,
        'Conference USA': True,
        'FBS Independents': True,
        'Mid-American': True,
        'Mountain West': True,
        'Pac-12': True,
        'SEC': False,
        'Sun Belt': True
    }
    return g5_conference[conference_name]

def extract_logo_url(data: dict) -> str:
    try:
        logo_url = data['team']['logos'][0]['href']
    except Exception as e:
        print(e)
        logo_url = ''
    return logo_url
