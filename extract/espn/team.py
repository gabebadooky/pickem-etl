class Team:
    def __init__(self, team):
        self.team_id = team['team']['id']
        self.cbs_code = ''
        self.espn_code = team['team']['id']
        self.fox_code = ''
        self.vegas_code = ''
        self.conference_code = extract_conference_code(team)
        self.conference_name = extract_conference_name(team)
        self.division_name = extract_division_name(team)
        self.team_name = extract_team_name(team)
        self.team_mascot = extract_team_mascot(team)
        # Treat Notre Dame as Power 4...
        self.g5_conference = False if team['team']['id'] == '87' else is_power_conference(extract_conference_name(team))
        self.team_logo_url = extract_logo_url(team)
        self.conference_wins = 0
        self.conference_losses = 0
        self.conference_ties = 0
        self.overall_wins = 0
        self.overall_losses = 0
        self.overall_ties = 0
        self.pass_attempts = 0
        self.opp_pass_attempts = 0
        self.pass_completions = 0
        self.opp_pass_completions = 0
        self.completion_percentage = 0
        self.opp_completion_percentage = 0
        self.pass_yards = 0
        self.opp_pass_yards = 0
        self.pass_touchdowns = 0
        self.opp_pass_touchdowns = 0
        self.offense_interceptions = 0
        self.defense_interceptions = 0
        self.rush_yards = 0
        self.opp_rush_yards = 0
        self.rush_attempts = 0
        self.opp_rush_attempts = 0
        self.yards_per_rush = 0
        self.opp_yards_per_rush = 0
        self.rush_touchdowns = 0
        self.opp_rush_touchdowns = 0

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

def is_power_conference(conference_name: str) -> bool:
    if conference_name in ['ACC', 'Big 12', 'Big Ten', 'SEC']:
        return True
    else :
        return False

def extract_logo_url(data: dict) -> str:
    try:
        logo_url = data['team']['logos'][0]['href']
    except Exception as e:
        print(e)
        logo_url = ''
    return logo_url
