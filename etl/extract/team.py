from bs4 import BeautifulSoup
import etl.extract.espn.team as espn
import etl.extract.cbs.team_stats as cbs


class Team:
    def __init__(self, espn_team: dict, cbs_team: BeautifulSoup):
        self.team_id: str = espn.extract_team_id(espn_team)
        self.league: str
        self.espn_code: str
        self.cbs_code: str
        self.fox_code: str
        self.vegas_code: str
        self.conference_code: str = espn.extract_conference_code(espn_team)
        self.conference_name: str = espn.extract_conference_name(espn_team)
        self.division_name: str = espn.extract_division_name(espn_team)
        self.team_name: str = espn.extract_team_name(espn_team)
        self.team_mascot: str = espn.extract_team_mascot(espn_team)
        self.power_conference: bool = espn.is_power_conference(self.conference_name)
        self.team_logo_url: str = espn.extract_logo_url(espn_team)
        self.primary_color: str = espn.extract_primary_color(espn_team)
        self.alternate_color: str = espn.extract_alternate_color(espn_team)
        self.conference_wins: int = 0       # TODO: Parse record from espn team endpoint
        self.conference_losses: int = 0     # TODO: Parse record from espn team endpoint
        self.conference_ties: int = 0       # TODO: Parse record from espn team endpoint
        self.overall_wins: int = 0          # TODO: Parse record from espn team endpoint
        self.overall_losses: int = 0        # TODO: Parse record from espn team endpoint
        self.overall_ties: int = 0          # TODO: Parse record from espn team endpoint
        self.pass_attempts: str = cbs.get_team_pass_attempts(cbs_team)
        self.opp_pass_attempts: str = cbs.get_opp_pass_attempts(cbs_team)
        self.pass_completions: str = cbs.get_team_pass_completions(cbs_team)
        self.opp_pass_completions: str = cbs.get_opp_pass_completions(cbs_team)
        self.completion_percentage: str = cbs.get_team_completion_percentage(cbs_team)
        self.opp_completion_percentage: str = cbs.get_opp_completion_percentage(cbs_team)
        self.pass_yards: str = cbs.get_team_pass_yards(cbs_team)
        self.opp_pass_yards: str = cbs.get_opp_pass_yards(cbs_team)
        self.pass_touchdowns: str = cbs.get_team_pass_yards(cbs_team)
        self.opp_pass_touchdowns: str = cbs.get_opp_pass_yards(cbs_team)
        self.offense_interceptions: str = cbs.get_team_offense_interceptions(cbs_team)
        self.defense_interceptions: str = cbs.get_team_defense_interceptions(cbs_team)
        self.rush_yards: str = cbs.get_team_rush_yards(cbs_team)
        self.opp_rush_yards: str = cbs.get_opp_rush_yards(cbs_team)
        self.rush_attempts: str = cbs.get_team_rush_attempts(cbs_team)
        self.opp_rush_attempts: str = cbs.get_opp_rush_attempts(cbs_team)
        self.yards_per_rush: str = cbs.get_team_yard_per_rush(cbs_team)
        self.opp_yards_per_rush: str = cbs.get_opp_yard_per_rush(cbs_team)
        self.rush_touchdowns: str = cbs.get_team_rush_touchdowns(cbs_team)
        self.opp_rush_touchdowns: str = cbs.get_opp_rush_touchdowns(cbs_team)