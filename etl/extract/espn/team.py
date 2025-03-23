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
        self.primary_color = team['team']['color']
        self.alternate_color = extract_alternate_color(team)
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
    if hasattr(data['team'], 'location'):
        return data['team']['location']
    else:
        return ''

def extract_team_mascot(data: dict) -> str:
    if hasattr(data['team'], 'name'):
        return data['team']['name']
    else:
        return ''

def extract_conference_code(data: dict) -> str:
    try:
        return data['team']['groups']['id']
    except:
        return ''

def extract_conference_name(data: dict) -> str:
    if hasattr(data['team'], 'standingSummary'):
        conference_name = data['team']['standingSummary'].split(' in ')[1]
        if '-' in conference_name:
            conference_name = conference_name.split(' - ')[0]
        if 'AFC' in conference_name:
            conference_name = 'AFC'
        if 'NFC' in conference_name:
            conference_name = 'NFC'
    else:
        return ''

def extract_division_name(data: dict) -> str:
    if hasattr(data['team'], 'standingSummary'):
        division_name = data['team']['standingSummary'].split(' in ')[1]
        if '-' in division_name:
            division_name = division_name.split(' - ')[1]
        if 'AFC' not in division_name or 'NFC' not in division_name:
            division_name = ''
    else:
        return ''

def is_power_conference(conference_name: str) -> bool:
    return True if conference_name in ['ACC', 'Big 12', 'Big Ten', 'SEC'] else False

def extract_logo_url(data: dict) -> str:
    try:
        return data['team']['logos'][0]['href']
    except:
        return ''

def extract_alternate_color(data: dict) -> str:
    if hasattr(data['team'], 'alternateColor'):
        alternate_color = data['team']['alternateColor']
    elif data['team']['color'] == 'ffffff':
        alternate_color = '000000'
    else:
        alternate_color = 'ffffff'
    return alternate_color