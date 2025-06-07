def get_away_odds(scorecard_soup: str) -> str:
    """Method to extract CBS away team odds metrics"""
    return scorecard_soup.find("div", class_="in-progress-odds-away").get_text()


def get_home_odds(scorecard_soup: str) -> str:
    """Method to extract CBS home team odds metrics"""
    return scorecard_soup.find("div", class_="in-progress-odds-home").get_text()


def get_game_oddes(scorecard_soup: str) -> dict:
    """Method to exxtract CBS college football game odds metrics for given game"""
    away_odds = get_away_odds(scorecard_soup)
    home_odds = get_home_odds(scorecard_soup)

    odds = {
        "away_moneyline": home_odds[1:] if "+" in home_odds else f"+{home_odds[1:]}",
        "home_moneyline": home_odds[1:] if "-" in home_odds else f"+{home_odds[1:]}",
        "over_under": away_odds[1:]
    }

    return
