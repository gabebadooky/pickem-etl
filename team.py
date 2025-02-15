def extract_team_name(data: dict) -> str:
    try:
        team_name = data['team']['nickname']
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
    except Exception as e:
        print(e)
        conference_name = ''
    return conference_name

def extract_division_name(data: dict) -> str:
    try:
        division_name = data['team']['standingSummary'].split(' in ')[1]
        if '-' in division_name:
            division_name = division_name.split(' - ')[1] 
    except Exception as e:
        print(e)
        division_name = ''
    return division_name