class Team:
    def __init__(self, team: object):
        self.team_id = extract_team_id(team)
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
        self.primary_color = extract_primary_color(team)
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

def extract_team_id(data: dict) -> str:
    try:
        formatted_team_location = data['team']['location'].replace('é', 'e').replace('&', '').replace('.', '').replace(' ', '-').replace('(', '').replace(')', '').lower()
        formatted_team_name = data['team']['name'].replace('é', 'e').replace('&', '').replace('.', '').replace(' ', '-').replace('(', '').replace(')', '').lower()
        return f"{formatted_team_location}-{formatted_team_name}"
    except:
        return None

def extract_team_name(data: dict) -> str:
    try:
        return data['team']['location']
    except:
        return None

def extract_team_mascot(data: dict) -> str:
    try:
        return data['team']['name']
    except:
        return None

def extract_conference_code(data: dict) -> str:
    try:
        return data['team']['groups']['id']
    except:
        return None

def extract_conference_name(data: dict) -> str:
    try:
        conference_name = data['team']['standingSummary'].split(' in ')[1]
        if '-' in conference_name:
            conference_name = conference_name.split(' - ')[0]
        if 'AFC' in conference_name:
            conference_name = 'AFC'
        if 'NFC' in conference_name:
            conference_name = 'NFC'
        return conference_name
    except:
        return None

def extract_division_name(data: dict) -> str:
    try:
        division_name = data['team']['standingSummary'].split(' in ')[1]
        if '-' in division_name:
            division_name = division_name.split(' - ')[1]
        if 'AFC' not in division_name or 'NFC' not in division_name:
            division_name = None
        return division_name
    except:
        return None

def is_power_conference(conference_name: str) -> bool:
    return True if conference_name in ['ACC', 'Big 12', 'Big Ten', 'SEC'] else False

def extract_logo_url(data: dict) -> str:
    try:
        return data['team']['logos'][0]['href']
    except:
        return None

def extract_primary_color(data: dict) -> str:
    try:
        return data['team']['color']
    except:
        return '000000'

def extract_alternate_color(data: dict) -> str:
    try:
        return data['team']['alternateColor']
    except:
        try:
            if data['team']['color'] == 'ffffff':
                return '000000'
            else:
                return 'ffffff'
        except:
            return 'ffffff'


"""
data = {
    'team': {
        'id': '304', 
        'uid': 's:20~l:23~t:304', 
        'slug': 'idaho-state-bengals', 
        'location': 'Idaho State', 
        'name': 'Bengals', 
        'nickname': 'Idaho St', 
        'abbreviation': 'IDST', 
        'displayName': 'Idaho State Bengals', 
        'shortDisplayName': 'Idaho St', 
        'color': 'ef8c00', 
        'alternateColor': 'e9a126', 
        'isActive': True, 
        'logos': [
            {
                'href': 'https://a.espncdn.com/i/teamlogos/ncaa/500/304.png', 
                'width': 500, 
                'height': 500, 
                'alt': '', 
                'rel': ['full', 'default'], 
                'lastUpdated': '2019-08-22T15:06Z'
            }, 
            {
                'href': 'https://a.espncdn.com/i/teamlogos/ncaa/500-dark/304.png', 
                'width': 500, 
                'height': 500, 
                'alt': '', 
                'rel': ['full', 'dark'], 
                'lastUpdated': '2019-08-22T15:06Z'
            }, 
            {
                'href': 'https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/primary_logo_on_white_color.png', 
                'width': 4096, 
                'height': 4096, 
                'alt': '', 
                'rel': ['full', 'primary_logo_on_white_color'], 
                'lastUpdated': '2024-11-11T01:46Z'
            }, 
            {
                'href': 'https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/primary_logo_on_black_color.png', 
                'width': 4096, 
                'height': 4096, 
                'alt': '', 
                'rel': ['full', 'primary_logo_on_black_color'], 
                'lastUpdated': '2024-11-11T01:46Z'
            }, 
            {
                'href': 'https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/primary_logo_on_primary_color.png', 
                'width': 4096, 
                'height': 4096, 
                'alt': '', 
                'rel': ['full', 'primary_logo_on_primary_color'], 
                'lastUpdated': '2024-11-11T01:46Z'
            }, 
            {
                'href': 'https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/primary_logo_on_secondary_color.png', 
                'width': 4096, 
                'height': 4096, 
                'alt': '', 
                'rel': ['full', 'primary_logo_on_secondary_color'], 
                'lastUpdated': '2024-11-11T01:46Z'
            }, 
            {
                'href': 'https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/secondary_logo_on_white_color.png', 
                'width': 4096, 
                'height': 4096, 
                'alt': '', 
                'rel': ['full', 'secondary_logo_on_white_color'], 
                'lastUpdated': '2024-11-11T01:46Z'
            }, 
            {
                'href': 'https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/secondary_logo_on_black_color.png', 
                'width': 4096, 
                'height': 4096, 
                'alt': '', 
                'rel': ['full', 'secondary_logo_on_black_color'], 
                'lastUpdated': '2024-11-11T01:46Z'
            }, 
            {
                'href': 'https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/secondary_logo_on_primary_color.png', 
                'width': 4096, 
                'height': 4096, 
                'alt': '', 
                'rel': ['full', 'secondary_logo_on_primary_color'], 
                'lastUpdated': '2024-11-11T01:46Z'
            }, 
            {
                'href': 'https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/secondary_logo_on_secondary_color.png', 
                'width': 4096, 
                'height': 4096, 
                'alt': '', 
                'rel': ['full', 'secondary_logo_on_secondary_color'], 
                'lastUpdated': '2024-11-11T01:46Z'
            }
        ], 
        'record': {}, 
        'groups': {
            'id': '20', 
            'parent': {
                'id': '81'
            }, 
            'isConference': True
        }, 
        'links': [
            {
                'language': 'en-US', 
                'rel': ['clubhouse', 'desktop', 'team'], 
                'href': 'https://www.espn.com/college-football/team/_/id/304/idaho-state-bengals', 
                'text': 'Clubhouse', 
                'shortText': 'Clubhouse', 
                'isExternal': False, 
                'isPremium': False
            },
            {
                'language': 'en-US', 
                'rel': ['clubhouse', 'mobile', 'team'], 
                'href': 'https://www.espn.com/college-football/team/_/id/304/idaho-state-bengals', 
                'text': 'Clubhouse', 
                'shortText': 'Clubhouse', 
                'isExternal': False, 
                'isPremium': False
            }, 
            {
                'language': 'en-US', 
                'rel': ['roster', 'desktop', 'team'], 
                'href': 'https://www.espn.com/college-football/team/roster/_/id/304', 
                'text': 'Roster', 
                'shortText': 'Roster', 
                'isExternal': False, 
                'isPremium': False
            }, 
            {
                'language': 'en-US', 
                'rel': ['stats', 'desktop', 'team'], 
                'href': 'https://www.espn.com/college-football/team/stats/_/id/304', 
                'text': 'Statistics', 
                'shortText': 'Statistics', 
                'isExternal': False, 
                'isPremium': False
            }, 
            {
                'language': 'en-US', 
                'rel': ['schedule', 'desktop', 'team'], 
                'href': 'https://www.espn.com/college-football/team/schedule/_/id/304', 
                'text': 'Schedule', 
                'shortText': 'Schedule', 
                'isExternal': False, 
                'isPremium': False
            }, 
            {
                'language': 'en-US', 
                'rel': ['tickets', 'desktop', 'team'], 
                'href': 'https://www.vividseats.com/idaho-state-bengals-football-tickets--sports-ncaa-football/performer/7654?wsUser=717', 
                'text': 'Tickets', 
                'shortText': 'Tickets', 
                'isExternal': True, 
                'isPremium': False
            }, 
            {
                'language': 'en-US', 
                'rel': ['awards', 'desktop', 'team'], 
                'href': 'https://www.espn.com/college-football/awards/_/team/304', 
                'text': 'Awards', 
                'shortText': 'Awards', 
                'isExternal': False, 
                'isPremium': False
            }
        ], 
        'nextEvent': [], 
        'standingSummary': '6th in Big Sky'
    }
}
"""