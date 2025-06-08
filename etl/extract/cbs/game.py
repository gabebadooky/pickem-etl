# https://www.cbssports.com/college-football/gametracker/preview/NCAAF_20250823_IOWAST@KSTATE/


def get_url_date(scorecard_soup: str) -> str:
    date_span: str = scorecard_soup.find("div", class_="top-bar").find("div", class_="game-status").find("span", class_="game-status").find("span", class_="formatter").get_text()
    return f"2025{date_span.split(",").replace("/")}"


def get_team_code(away_team_ancher_tag: str) -> str:
    beginning_index: int = away_team_ancher_tag.find("/teams/")
    away_team_code: str = away_team_ancher_tag[beginning_index:]
    ending_index: int = away_team_code.find("/")
    away_team_code = away_team_code[:ending_index]
    return away_team_code


def get_cbs_code(scorecard_soup: str) -> str:
    """Method to extract CBS Game Code ex: `NCAAF_20250823_IOWAST@KSTATE`"""
    # scorecard_soup.get("data-abbrev")
    url_date: str = get_url_date(scorecard_soup)
    team_rows: str = scorecard_soup.find_all('div', class_="team-details-wrapper")
    away_team_anchor: str = team_rows[0].find('a').get('href')
    home_team_anchor: str = team_rows[1].find('a').get('href')
    away_team_code: str = get_team_code(away_team_anchor)
    home_team_code: str = get_team_code(home_team_anchor)
    return f"NCAAF_{url_date}_{away_team_code}@{home_team_code}"


def get_away_odds(scorecard_soup: str) -> str:
    """Method to extract CBS away team odds metrics"""
    return scorecard_soup.find("div", class_="in-progress-odds-away").get_text()


def get_home_odds(scorecard_soup: str) -> str:
    """Method to extract CBS home team odds metrics"""
    return scorecard_soup.find("div", class_="in-progress-odds-home").get_text()


def get_game_odds(scorecard_soup: str) -> dict:
    """Method to exxtract CBS college football game odds metrics for given game"""
    away_odds = get_away_odds(scorecard_soup)
    home_odds = get_home_odds(scorecard_soup)

    odds = {
        "away_moneyline": home_odds[1:] if "+" in home_odds else f"+{home_odds[1:]}",
        "home_moneyline": home_odds[1:] if "-" in home_odds else f"+{home_odds[1:]}",
        "over_under": away_odds[1:]
    }

    return odds
