def extract_team_id(data: dict) -> str:
    """Method to extract and construct custom team_id from ESPN team endpoint response"""
    try:
        formatted_team_location: str = data["team"]["location"].replace("é", "e").replace("&", "").replace(".", "").replace(" ", "-").replace("(", "").replace(")", "").replace("'", "").replace("--", "-").lower()
        formatted_team_name: str = data["team"]["name"].replace("é", "e").replace("&", "").replace(".", "").replace(" ", "-").replace("(", "").replace(")", "").replace("'", "").replace("--", "-").lower()
        return f"{formatted_team_location}-{formatted_team_name}"
    except:
        return None

def extract_team_code(data: dict) -> str:
    """Method to extract Team ID property from ESPN team endpoint response"""
    try:
        return data["team"]["id"]
    except:
        return None

def extract_team_name(data: dict) -> str:
    """Method to extract team location/name from ESPN team endpoint response"""
    return data["team"]["location"]

def extract_team_mascot(data: dict) -> str:
    """Method to extract team mascot from ESPN team endpoint response"""
    return data["team"]["name"]

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

def extract_ranking(data: dict) -> str:
    """Method to extract team current ranking from ESPN team endpoint response"""
    try:
        next_event_competitors: str = data["team"]["nextEvent"][0]["competitions"][0]["competitors"]
        if next_event_competitors[0]["id"] == data["team"]["id"]:
            ranking: int = int(next_event_competitors[0]["curatedRank"]["current"])
        else:
            ranking: int = int(next_event_competitors[1]["curatedRank"]["current"])
        
        return ranking if ranking <= 25 else None
    
    except:
        return None

def extract_overall_record(data: dict) -> dict:
    """Method to extract overall team record from ESPN team enpoint"""
    record: dict = {
        "wins": 0,
        "losses": 0,
        "ties": 0
    }
    try:
        record_summary_elements: str = data["team"]["record"]["items"][0]["summary"].split("-")
        print(record_summary_elements)
        if len(record_summary_elements) == 3:
            record["wins"] = int(record_summary_elements[0])
            record["losses"] = int(record_summary_elements[1])
            record["ties"] = int(record_summary_elements[2])
        else:
            record["wins"] = int(record_summary_elements[0])
            record["losses"] = int(record_summary_elements[1])
    finally:
        return record