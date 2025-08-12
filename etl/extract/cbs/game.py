# https://www.cbssports.com/college-football/gametracker/preview/NCAAF_20250823_IOWAST@KSTATE/


def get_cbs_code(scorecard_soup: str) -> str:
    """Method to extract CBS Game Code ex: `NCAAF_20250823_IOWAST@KSTATE`"""
    return scorecard_soup["data-abbrev"]


def __scrape_odds_table__(odds_page: str, cbs_code: str) -> str | None:
    """Method that scrapes the table element with a data-game-abbrev equal to the given cbs game code"""
    try:
        return odds_page.find("table", attrs={"data-game-abbrev": f"{cbs_code}"})
    except:
        None


def away_spread(odds_page: str, cbs_code: str) -> str | None:
    """Method that scrapes the current away spread metric for the given CBS game"""
    game_odds_table: str = __scrape_odds_table__(odds_page, cbs_code)
    try:
        return game_odds_table.find_all("td", class_="OddsBlock-betOdds--spread")[0].find("div", class_="OddsBlock-boxLine").get_text().strip()
    except:
        return None


def home_spread(odds_page: str, cbs_code: str) -> str | None:
    """Method that scrapes the current home spread metric for the given CBS game"""
    game_odds_table: str = __scrape_odds_table__(odds_page, cbs_code)
    try:
        return game_odds_table.find_all("td", class_="OddsBlock-betOdds--spread")[1].find("div", class_="OddsBlock-boxLine").get_text().strip()
    except:
        return None


def over_under(odds_page: str, cbs_code: str) -> str | None:
    """Method that scrapes the current over/under metric for the given CBS game"""
    game_odds_table: str = __scrape_odds_table__(odds_page, cbs_code)
    try:
        return game_odds_table.find("td", class_="OddsBlock-betOdds--total").find("div", class_="OddsBlock-boxLine").get_text().strip()
    except:
        return None


def away_moneyline(odds_page: str, cbs_code: str) -> str | None:
    """Method that scrapes the current away moneyline metric for the given CBS game"""
    game_odds_table: str = __scrape_odds_table__(odds_page, cbs_code)
    try:
        return game_odds_table.find_all("td", class_="OddsBlock-betOdds--moneyline")[0].find("div", class_="OddsBlock-boxLine").get_text().strip()
    except:
        return None


def home_moneyline(odds_page: str, cbs_code: str) -> str | None:
    """Method that scrapes the current away moneyline metric for the given CBS game"""
    game_odds_table: str = __scrape_odds_table__(odds_page, cbs_code)
    try:
        return game_odds_table.find_all("td", class_="OddsBlock-betOdds--moneyline")[1].find("div", class_="OddsBlock-boxLine").get_text().strip()
    except:
        return None

