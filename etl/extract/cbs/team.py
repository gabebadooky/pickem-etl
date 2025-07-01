def get_away_team_abbreviation(game_code: str) -> str:
    """Method to extract and construct team code from CBS game URL"""
    try:
        beginning_index: int = game_code.find("_", game_code.find("_") + 1) + 1
        ending_index: int = game_code.find("@")
        return game_code[beginning_index:ending_index]
    except:
        return None