# https://www.cbssports.com/college-football/gametracker/preview/NCAAF_20250823_IOWAST@KSTATE/


def __get_url_date__(scorecard_soup: str) -> str:
    """Method to extract and construct game date parameters in the format used in the CBS game URL"""
    date_span: str = scorecard_soup.find("div", class_="top-bar").find("div", class_="game-status").find("span", class_="game-status").find("span", class_="formatter").get_text()
    return f"2025{date_span.split(",").replace("/")}"


def __get_team_code__(away_team_ancher_tag: str) -> str:
    """Method to extract CBS team abbreviation from CBS game endpoint response"""
    beginning_index: int = away_team_ancher_tag.find("/teams/")
    away_team_code: str = away_team_ancher_tag[beginning_index:]
    ending_index: int = away_team_code.find("/")
    away_team_code: str = away_team_code[:ending_index]
    return away_team_code


def get_cbs_code(scorecard_soup: str) -> str:
    """Method to extract CBS Game Code ex: `NCAAF_20250823_IOWAST@KSTATE`"""
    # scorecard_soup.get("data-abbrev")
    url_date: str = __get_url_date__(scorecard_soup)
    team_rows: str = scorecard_soup.find_all('div', class_="team-details-wrapper")
    away_team_anchor: str = team_rows[0].find('a').get('href')
    home_team_anchor: str = team_rows[1].find('a').get('href')
    away_team_code: str = __get_team_code__(away_team_anchor)
    home_team_code: str = __get_team_code__(home_team_anchor)
    return f"NCAAF_{url_date}_{away_team_code}@{home_team_code}"


def __get_away_odds__(scorecard_soup: str) -> str:
    """Method to extract CBS away team odds metrics"""
    return scorecard_soup.find("div", class_="in-progress-odds-away").get_text()


def __get_home_odds__(scorecard_soup: str) -> str:
    """Method to extract CBS home team odds metrics"""
    return scorecard_soup.find("div", class_="in-progress-odds-home").get_text()


def get_away_moneyline(scorecard_soup: str) -> str:
    """Method to extract CBS away team moneyline"""
    home_odds: str = __get_home_odds__(scorecard_soup)
    return home_odds[1:] if "+" in home_odds else f"+{home_odds[1:]}"


def get_home_moneyline(scorecard_soup: str) -> str:
    """Method to extract CBS home team moneyline"""
    home_odds: str = __get_home_odds__(scorecard_soup)
    return home_odds[1:] if "-" in home_odds else f"+{home_odds[1:]}"


def get_over_under(scorecard_soup: str) -> str:
    """Method to extract CBS game over/under"""
    return __get_away_odds__(scorecard_soup)[1:]



