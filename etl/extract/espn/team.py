def extract_team_id(data: dict) -> str:
    """Method to extract and construct custom team_id from ESPN team endpoint response"""
    try:
        formatted_team_location: str = data["team"]["location"].replace("é", "e").replace("&", "").replace(".", "").replace(" ", "-").replace("(", "").replace(")", "").lower()
        formatted_team_name: str = data["team"]["name"].replace("é", "e").replace("&", "").replace(".", "").replace(" ", "-").replace("(", "").replace(")", "").lower()
        return f"{formatted_team_location}-{formatted_team_name}"
    except:
        return None

def extract_team_name(data: dict) -> str:
    """Method to extract team location/name from ESPN team endpoint response"""
    try:
        return data["team"]["location"]
    except:
        return None

def extract_team_mascot(data: dict) -> str:
    """Method to extract team mascot from ESPN team endpoint response"""
    try:
        return data["team"]["name"]
    except:
        return None

def extract_conference_code(data: dict) -> str:
    """Method to extract team conference code from ESPN team endpoint response"""
    try:
        return data["team"]["groups"]["id"]
    except:
        return None

def extract_conference_name(data: dict) -> str:
    """Method to extract team conference name from ESPN team endpoint response"""
    try:
        conference_name: str = data["team"]["standingSummary"].split(" in ")[1]
        if "-" in conference_name:
            conference_name = conference_name.split(" - ")[0]
        if "AFC" in conference_name:
            conference_name = "AFC"
        if "NFC" in conference_name:
            conference_name = "NFC"
        return conference_name
    except:
        return None

def extract_division_name(data: dict) -> str:
    """Method to extract team division name from ESPN team endpoint response"""
    try:
        division_name: str = data["team"]["standingSummary"].split(" in ")[1]
        if "-" in division_name:
            division_name = division_name.split(" - ")[1]
        if "AFC" not in division_name or "NFC" not in division_name:
            division_name = None
        return division_name
    except:
        return None

def is_power_conference(conference_name: str) -> bool:
    """Method to define whether or not a team belongs in a power conference based 
        on the conference name from the ESPN team endpoint response"""
    return True if conference_name in ["ACC", "Big 12", "Big Ten", "SEC"] else False

def extract_logo_url(data: dict) -> str:
    """Method to extract team logo url from ESPN team endpoint response"""
    try:
        return data["team"]["logos"][0]["href"]
    except:
        return None

def extract_primary_color(data: dict) -> str:
    """Method to extract team primary color from ESPN team endpoint response"""
    try:
        return data["team"]["color"]
    except:
        return "000000"

def extract_alternate_color(data: dict) -> str:
    """Method to extract team alternate color from ESPN team endpoint response"""
    try:
        return data["team"]["alternateColor"]
    except:
        try:
            if data["team"]["color"] == "ffffff":
                return "000000"
            else:
                return "ffffff"
        except:
            return "ffffff"


"""
data = {
    "team": {
        "id": "304", 
        "uid": "s:20~l:23~t:304", 
        "slug": "idaho-state-bengals", 
        "location": "Idaho State", 
        "name": "Bengals", 
        "nickname": "Idaho St", 
        "abbreviation": "IDST", 
        "displayName": "Idaho State Bengals", 
        "shortDisplayName": "Idaho St", 
        "color": "ef8c00", 
        "alternateColor": "e9a126", 
        "isActive": True, 
        "logos": [
            {
                "href": "https://a.espncdn.com/i/teamlogos/ncaa/500/304.png", 
                "width": 500, 
                "height": 500, 
                "alt": "", 
                "rel": ["full", "default"], 
                "lastUpdated": "2019-08-22T15:06Z"
            }, 
            {
                "href": "https://a.espncdn.com/i/teamlogos/ncaa/500-dark/304.png", 
                "width": 500, 
                "height": 500, 
                "alt": "", 
                "rel": ["full", "dark"], 
                "lastUpdated": "2019-08-22T15:06Z"
            }, 
            {
                "href": "https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/primary_logo_on_white_color.png", 
                "width": 4096, 
                "height": 4096, 
                "alt": "", 
                "rel": ["full", "primary_logo_on_white_color"], 
                "lastUpdated": "2024-11-11T01:46Z"
            }, 
            {
                "href": "https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/primary_logo_on_black_color.png", 
                "width": 4096, 
                "height": 4096, 
                "alt": "", 
                "rel": ["full", "primary_logo_on_black_color"], 
                "lastUpdated": "2024-11-11T01:46Z"
            }, 
            {
                "href": "https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/primary_logo_on_primary_color.png", 
                "width": 4096, 
                "height": 4096, 
                "alt": "", 
                "rel": ["full", "primary_logo_on_primary_color"], 
                "lastUpdated": "2024-11-11T01:46Z"
            }, 
            {
                "href": "https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/primary_logo_on_secondary_color.png", 
                "width": 4096, 
                "height": 4096, 
                "alt": "", 
                "rel": ["full", "primary_logo_on_secondary_color"], 
                "lastUpdated": "2024-11-11T01:46Z"
            }, 
            {
                "href": "https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/secondary_logo_on_white_color.png", 
                "width": 4096, 
                "height": 4096, 
                "alt": "", 
                "rel": ["full", "secondary_logo_on_white_color"], 
                "lastUpdated": "2024-11-11T01:46Z"
            }, 
            {
                "href": "https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/secondary_logo_on_black_color.png", 
                "width": 4096, 
                "height": 4096, 
                "alt": "", 
                "rel": ["full", "secondary_logo_on_black_color"], 
                "lastUpdated": "2024-11-11T01:46Z"
            }, 
            {
                "href": "https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/secondary_logo_on_primary_color.png", 
                "width": 4096, 
                "height": 4096, 
                "alt": "", 
                "rel": ["full", "secondary_logo_on_primary_color"], 
                "lastUpdated": "2024-11-11T01:46Z"
            }, 
            {
                "href": "https://a.espncdn.com/guid/015f8185-33b5-ab25-83f2-967b77eaddc1/logos/secondary_logo_on_secondary_color.png", 
                "width": 4096, 
                "height": 4096, 
                "alt": "", 
                "rel": ["full", "secondary_logo_on_secondary_color"], 
                "lastUpdated": "2024-11-11T01:46Z"
            }
        ], 
        "record": {}, 
        "groups": {
            "id": "20", 
            "parent": {
                "id": "81"
            }, 
            "isConference": True
        }, 
        "links": [
            {
                "language": "en-US", 
                "rel": ["clubhouse", "desktop", "team"], 
                "href": "https://www.espn.com/college-football/team/_/id/304/idaho-state-bengals", 
                "text": "Clubhouse", 
                "shortText": "Clubhouse", 
                "isExternal": False, 
                "isPremium": False
            },
            {
                "language": "en-US", 
                "rel": ["clubhouse", "mobile", "team"], 
                "href": "https://www.espn.com/college-football/team/_/id/304/idaho-state-bengals", 
                "text": "Clubhouse", 
                "shortText": "Clubhouse", 
                "isExternal": False, 
                "isPremium": False
            }, 
            {
                "language": "en-US", 
                "rel": ["roster", "desktop", "team"], 
                "href": "https://www.espn.com/college-football/team/roster/_/id/304", 
                "text": "Roster", 
                "shortText": "Roster", 
                "isExternal": False, 
                "isPremium": False
            }, 
            {
                "language": "en-US", 
                "rel": ["stats", "desktop", "team"], 
                "href": "https://www.espn.com/college-football/team/stats/_/id/304", 
                "text": "Statistics", 
                "shortText": "Statistics", 
                "isExternal": False, 
                "isPremium": False
            }, 
            {
                "language": "en-US", 
                "rel": ["schedule", "desktop", "team"], 
                "href": "https://www.espn.com/college-football/team/schedule/_/id/304", 
                "text": "Schedule", 
                "shortText": "Schedule", 
                "isExternal": False, 
                "isPremium": False
            }, 
            {
                "language": "en-US", 
                "rel": ["tickets", "desktop", "team"], 
                "href": "https://www.vividseats.com/idaho-state-bengals-football-tickets--sports-ncaa-football/performer/7654?wsUser=717", 
                "text": "Tickets", 
                "shortText": "Tickets", 
                "isExternal": True, 
                "isPremium": False
            }, 
            {
                "language": "en-US", 
                "rel": ["awards", "desktop", "team"], 
                "href": "https://www.espn.com/college-football/awards/_/team/304", 
                "text": "Awards", 
                "shortText": "Awards", 
                "isExternal": False, 
                "isPremium": False
            }
        ], 
        "nextEvent": [], 
        "standingSummary": "6th in Big Sky"
    }
}
"""