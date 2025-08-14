from bs4 import BeautifulSoup
import etl.extract.espn.game as espn
import etl.extract.cbs.game as cbs
import etl.extract.fox.game as fox


class Game:
    def __init__(self, espn_game: dict, cbs_game: BeautifulSoup, cbs_odds: BeautifulSoup, fox_url: str, fox_game: BeautifulSoup):
        self.game_id: str = espn.extract_game_id(espn_game)
        self.league: str
        self.week: int = espn.extract_game_week(espn_game)
        self.year: int = espn.extract_game_year(espn_game)
        self.espn_code: str = espn.extract_game_code(espn_game)
        self.cbs_code: str = cbs.get_cbs_code(cbs_game)
        self.fox_code: str = fox.get_fox_code(fox_url)
        self.vegas_code: str = ""
        self.away_team_id: str = espn.extract_away_team(espn_game)
        self.home_team_id: str = espn.extract_home_team(espn_game)
        self.date: str = espn.extract_game_date(espn_game)
        self.time: str = espn.extract_game_time(espn_game)
        self.tv_coverage: str = espn.extract_tv_coverage(espn_game)
        self.finished: int = espn.extract_game_finished(espn_game)
        self.away_q1_score: int = 0                 # TODO: Develop extract_box_score methods during/after week 0
        self.away_q2_score: int = 0                 # TODO: Develop extract_box_score methods during/after week 0
        self.away_q3_score: int = 0                 # TODO: Develop extract_box_score methods during/after week 0
        self.away_q4_score: int = 0                 # TODO: Develop extract_box_score methods during/after week 0
        self.away_overtime_score: int = 0           # TODO: Develop extract_box_score methods during/after week 0
        self.away_total_score: int = 0              # TODO: Develop extract_box_score methods during/after week 0
        self.home_q1_score: int = 0                 # TODO: Develop extract_box_score methods during/after week 0
        self.home_q2_score: int = 0                 # TODO: Develop extract_box_score methods during/after week 0
        self.home_q3_score: int = 0                 # TODO: Develop extract_box_score methods during/after week 0
        self.home_q4_score: int = 0                 # TODO: Develop extract_box_score methods during/after week 0
        self.home_overtime_score: int = 0           # TODO: Develop extract_box_score methods during/after week 0
        self.home_total_score: int = 0              # TODO: Develop extract_box_score methods during/after week 0
        self.espn_away_moneyline: str = espn.extract_away_moneyline(espn_game)
        self.espn_home_moneyline: str = espn.extract_home_moneyline(espn_game)
        self.espn_away_spread: str = espn.extract_away_spread(espn_game)
        self.espn_home_spread: str = espn.extract_home_spread(espn_game)
        self.espn_over_under: str = espn.extract_over_under(espn_game)
        self.espn_away_win_percentage: str = None   # TODO:
        self.espn_home_win_percentage: str = None   # TODO:
        self.cbs_away_moneyline: str = cbs.away_moneyline(cbs_odds, self.cbs_code)
        self.cbs_home_moneyline: str = cbs.home_moneyline(cbs_odds, self.cbs_code)
        self.cbs_away_spread: str = cbs.away_spread(cbs_odds, self.cbs_code)
        self.cbs_home_spread: str = cbs.home_spread(cbs_odds, self.cbs_code)
        self.cbs_over_under: str = cbs.over_under(cbs_odds, self.cbs_code)
        self.cbs_away_win_percentage: str = None    # TODO:
        self.cbs_home_win_percentage: str = None    # TODO:
        self.fox_away_moneyline: str = fox.get_away_moneyline(fox_game)
        self.fox_home_moneyline: str = fox.get_home_moneyline(fox_game)
        self.fox_away_spread: str = fox.get_away_spread(fox_game)
        self.fox_home_spread: str = fox.get_home_spread(fox_game)
        self.fox_over_under: str = fox.get_over_under(fox_game)
        self.fox_away_win_percentage: str = fox.get_away_win_probability(fox_game)
        self.fox_home_win_percentage: str = fox.get_home_win_probability(fox_game)
        self.vegas_away_moneyline: str = None
        self.vegas_home_moneyline: str = None
        self.vegas_away_spread: str = None
        self.vegas_home_spread: str = None
        self.vegas_over_under: str = None
        self.vegas_away_win_percentage: str = None
        self.vegas_home_win_percentage: str = None
        self.stadium: str = espn.extract_stadium(espn_game)
        self.city: str = espn.extract_city(espn_game)
        self.state: str = espn.extract_state(espn_game)
        self.latitude: float = 0.0
        self.longitude: float = 0.0