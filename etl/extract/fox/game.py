# https://www.foxsports.com/college-football/schedule?groupId=2&seasonType=reg&week=8

# https://www.foxsports.com/college-football/iowa-state-cyclones-vs-kansas-state-wildcats-aug-23-2025-game-boxscore-42830?tab=odds

# a:odds-container div:sp-rows

def get_fox_code(score_chip: str) -> str:
    """Method to extract Fox Game Code ex: iowa-state-cyclones-vs-kansas-state-wildcats-aug-22-2025-game-boxscore-42830"""
    game_code: str = score_chip["href"]
    beginning_index: int = game_code.find("college-football/") + 17
    return game_code[beginning_index:]


def __get_odds_rows__(odds_soup: str) -> str:
    """Method to parse away odds row"""
    odds_rows: list = odds_soup.find("a", class_="odds-container").find_all("div", class_="sp-rows")
    return odds_rows


def get_away_spread(odds_soup: str) -> str:
    """Method to extract Fox away team spread"""
    away_odds_row: str = __get_odds_rows__(odds_soup)[0]
    return away_odds_row.find_all("div", class_="sp-row-data")[0].get_text()
    

def get_home_spread(odds_soup: str) -> str:
    """Method to extract Fox home team spread"""
    home_odds_row: str = __get_odds_rows__(odds_soup)[1]
    return home_odds_row.find_all("div", class_="sp-row-data")[0].get_text()


def get_away_moneyline(odds_soup: str) -> str:
    """Method to extract Fox away team moneyline"""
    away_odds_row: str = __get_odds_rows__(odds_soup)[0]
    return away_odds_row.find_all("div", class_="sp-row-data")[1].get_text()
    

def get_home_moneyline(odds_soup: str) -> str:
    """Method to extract Fox home team moneyline"""
    home_odds_row: str = __get_odds_rows__(odds_soup)[1]
    return home_odds_row.find_all("div", class_="sp-row-data")[1].get_text()


def get_over_under(odds_soup: str) -> str:
    """Method to extract Fox game over/under"""
    away_odds_row: str = __get_odds_rows__(odds_soup)[0]
    return away_odds_row.find_all("div", class_="sp-row-data")[2].get_text()[2:]