# https://www.foxsports.com/college-football/iowa-state-cyclones-vs-kansas-state-wildcats-aug-23-2025-game-boxscore-42830?tab=odds

# a:odds-container div:sp-rows

def get_fox_code(fox_game_url: str) -> str | None:
    """Method to extract Fox Game Code ex: iowa-state-cyclones-vs-kansas-state-wildcats-aug-22-2025-game-boxscore-42830"""
    beginning_index: int = fox_game_url.find("college-football/") + 17
    end_index: int = fox_game_url.find("?tab=odds")
    return fox_game_url[beginning_index:end_index]


def __get_odds_rows__(odds_soup: str) -> str | None:
    """Method to parse away odds row"""
    try:
        return odds_soup.find("a", class_="odds-container").find_all("div", class_="sp-rows")
    except:
        return None


def get_away_spread(odds_soup: str) -> str | None:
    """Method to extract Fox away team spread"""
    try:
        away_odds_row: str = __get_odds_rows__(odds_soup)[0]
        return away_odds_row.find_all("div", class_="sp-row-data")[0].get_text()
    except TypeError:
        print(f"Away Spread does not exist yet for game")
        return None
    except Exception as e:
        print(f"Error occurred scraping Fox game away team spread{e}")
        return None
    

def get_home_spread(odds_soup: str) -> str | None:
    """Method to extract Fox home team spread"""
    try:
        home_odds_row: str = __get_odds_rows__(odds_soup)[1]
        return home_odds_row.find_all("div", class_="sp-row-data")[0].get_text()
    except TypeError:
        print(f"Home Spread does not exist yet for game")
        return None
    except Exception as e:
        print(f"Error occurred scraping Fox game home team spread{e}")
        return None


def get_away_moneyline(odds_soup: str) -> str | None:
    """Method to extract Fox away team moneyline"""
    try:
        away_odds_row: str = __get_odds_rows__(odds_soup)[0]
        return away_odds_row.find_all("div", class_="sp-row-data")[1].get_text()
    except IndexError:
        print(f"Away Moneyline does not exist yet for game")
        return None
    except Exception as e:
        print(f"Error occurred scraping Fox game away team moneyline{e}")
        return None
    

def get_home_moneyline(odds_soup: str) -> str | None:
    """Method to extract Fox home team moneyline"""
    try:
        home_odds_row: str = __get_odds_rows__(odds_soup)[1]
        return home_odds_row.find_all("div", class_="sp-row-data")[1].get_text()
    except IndexError:
        print(f"Home Moneyline does not exist yet for game")
        return None
    except Exception as e:
        print(f"Error occurred scraping Fox game home team moneyline{e}")
        return None


def get_over_under(odds_soup: str) -> str | None:
    """Method to extract Fox game over/under"""
    try:
        away_odds_row: str = __get_odds_rows__(odds_soup)[0]
        return away_odds_row.find_all("div", class_="sp-row-data")[2].get_text()[2:]
    except IndexError:
        print(f"Over/Under odds do not exist yet for game")
        return None
    except Exception as e:
        print(f"Error occurred scraping Fox game over/under{e}")
        return None


def get_away_win_probability(odds_soup: str) -> str | None:
    """Method to extract Fox game away team win probability"""
    try:
        team_probability: str = odds_soup.find("div", class_="probability-stats").find("div", class_="left-team").find("div", "team-probability").get_text().strip()
        return team_probability
    except:
        return None


def get_home_win_probability(odds_soup: str) -> str | None:
    """Method to extract Fox game home team win probability"""
    try:
        team_probability: str = odds_soup.find("div", class_="probability-stats").find("div", class_="right-team").find("div", "team-probability").get_text().strip()
        return team_probability
    except:
        return None