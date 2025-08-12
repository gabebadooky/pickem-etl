from bs4 import BeautifulSoup
import etl.transform.mapping as mapping
import requests, time

###### Methods to extract all games in week from source ######
def all_espn_games_in_week(espn_scoreboard_endpoint: str) -> list[dict]:
    """Method to retrieve all games from ESPN games endpoint"""
    print(f"Retrieving games for current week from ESPN endpoint {espn_scoreboard_endpoint}")
    data: dict = requests.get(espn_scoreboard_endpoint).json()
    events: list = data["events"]
    return events


def all_cbs_games_in_week(cbs_scoreboard_week_url: str) -> BeautifulSoup:
    """Method to scrape CBS scoreboard page for given week"""
    print(f"Scraping games for current week from CBS games page {cbs_scoreboard_week_url}")
    page_fetched: bool = False
    while page_fetched is not True:
        try:
            page_response: requests.Response = requests.get(cbs_scoreboard_week_url)
            page_fetched = True
        except Exception as e:
            print(f"Error occurred attempting cbs game week page request... Reattempting request!\nError: {e}\n")
            time.sleep(1)
    return BeautifulSoup(page_response.content, "html.parser")


def all_cbs_odds_in_week(cbs_odds_week_url: str) -> BeautifulSoup:
    """Method to scrape CBS odds page for given week"""
    print(f"Scraping odds for current week from CBS odds page {cbs_odds_week_url}")
    page_fetched: bool = False
    while page_fetched is not True:
        try:
            page_response: requests.Response = requests.get(cbs_odds_week_url)
            page_fetched = True
        except Exception as e:
            print(f"Error occurred attempting cbs odds week page request... Reattempting request!\nError: {e}\n")
            time.sleep(1)
    return BeautifulSoup(page_response.content, "html.parser")
             


def all_fox_games_in_week(fox_schedule_week_url: str):
    """Method to scrape Fox schedule page for given week"""
    print(f"Scraping games for current week from FOX games page {fox_schedule_week_url}")
    page_fetched: bool = False
    while page_fetched is not True:
        try:
            page_response: requests.Response = requests.get(fox_schedule_week_url)
            page_fetched = True
        except Exception as e:
            print(f"Error occurred attempting Fox game week page request... Reattempting request!\nError: {e}\n")
            time.sleep(1)
    return BeautifulSoup(page_response.content, "html.parser")
##############################################################



######## Methods to scrape specific game from source #########
def cbs_game_scorecard(page_soup: str, game_id: str, week: int) -> BeautifulSoup:
    """Method to scrape scorecard for current CFB game"""
    print(f"Scraping {game_id} scorecard from CBS game page")
    # TODO: Refactor me plz
    team_links: list = page_soup.find_all("a", class_="team-name-link")
    scorecards: list[str] = []
    for team_link in team_links:
        ending_index: int = team_link["href"].rfind('/')
        beginning_index: int = team_link["href"].rfind('/', 0, ending_index) + 1
        reformatted_team: str = team_link["href"][beginning_index:ending_index]
        if reformatted_team in mapping.cbs_to_espn_team_code_mapping:
            reformatted_team = mapping.cbs_to_espn_team_code_mapping[reformatted_team]
        if reformatted_team in game_id:
            for parent in team_link.parents:
                parent_element: str = parent
                if parent_element.name == "div" and "single-score-card" in parent_element.get("class", []):
                    if week <= 1:
                        scorecards.append(parent_element)
                    else:
                        return parent_element
    if len(scorecards) > 1:
        return scorecards[week]
    else:
        return scorecards[0]


def fox_game_url(page_soup: str, game_id: str, week: int) -> str:
    """Method to scrape score chip for current game"""
    print(f"Scraping {game_id} score chip from Fox schedule page")
    game_links: list = [] # .find_all("div", class_="table-segment")
    game_tables: list = page_soup.find_all("tbody", class_="row-data")
    
    for table in game_tables:
        for row in table.find_all("tr"):
            game_anchor_href: str = row.find("td").find("div").find("a")["href"]
            beginning_index: int = game_anchor_href.find("college-football/") + 17
            ending_index: int = game_anchor_href.find("-vs-")
            formatted_away_team = game_anchor_href[beginning_index:ending_index]
            if formatted_away_team in mapping.fox_to_espn_team_code_mapping:
                formatted_away_team = mapping.fox_to_espn_team_code_mapping[formatted_away_team]
            if formatted_away_team in game_id:
                game_url: str = f"https://www.foxsports.com{game_anchor_href}"
                if week <=1:
                    game_links.append(game_url)
                else:
                    return game_url
    if len(game_links) > 1:
        return game_links[week]
    else:
        return game_links[0]
    

def scrape_fox_game_odds_tab(game_url: str):
    """Method to scrape Fox game odds page"""
    page_fetched = False
    while page_fetched is not True:
        try:
            page_response: requests.Response = requests.get(game_url)
            page_fetched = True
        except Exception as e:
            print(f"Error occurred attempting Fox game odds page request.. Reattempting request!\nError: {e}\n")
            time.sleep(1)
    return BeautifulSoup(page_response.content, "html.parser")
##############################################################



###### Methods to scrape specific team from from source ######
def get_espn_team(espn_team_endpoint: str) -> dict:
    """Method to retrieve data from a given ESPN team endpoint"""
    print(f"Retrieving team from ESPN team endpoint {espn_team_endpoint}")
    data_fetched: bool = False
    while data_fetched is not True:
        try:
            data: dict = requests.get(espn_team_endpoint).json()
            data_fetched = True
        except Exception as e:
            print(f"Error occurred attempting team endpoint request... Reattempting request!\nError: {e}\n")
            time.sleep(1)
    return data


def map_espn_team_code_to_cbs_team_code(team_id: str) -> str:
    """Method to map ESPN team code to CBS code"""
    if team_id in mapping.espn_to_cbs_team_code_mapping:
        cbs_team_code: str = mapping.espn_to_cbs_team_code_mapping[team_id]
    else: 
        cbs_team_code: str = team_id
    return cbs_team_code


def scrape_cbs_team_stats(team_stats_page_url: str) -> BeautifulSoup:
    """Method to scrape CBS team stats page"""
    print(f"Scraping stats for current team from CBS team stats page {team_stats_page_url}")
    page_fetched: bool = False
    while page_fetched is not True:
        try:
            page_response: requests.Response = requests.get(team_stats_page_url)
            page_fetched = True
        except Exception as e:
            print(f"Error occurred attempting CBS Team Stats page request... Reattempting request!\nError: {e}\n")
            time.sleep(1)
    return BeautifulSoup(page_response.content, "html.parser")
##############################################################