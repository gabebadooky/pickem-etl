from bs4 import BeautifulSoup
from etl.extract.game import Game
from etl.extract.team import Team
import etl.extract.extract as extract
import etl.extract.espn as espn
import etl.extract.cbs.team as cbs
import etl.transform.mapping as mapping
import etl.transform.transform as transform
import etl.load.mysql_db as mysql


def extract_transform_load_games(week: int, season_properties: dict) -> None:
    """Method to perfom ETL process for games data from various sources for given week"""
    print(f"\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nProcessing {season_properties['league']} week {week} games\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    espn_games: list[dict] = extract.all_espn_games_in_week(f"{season_properties['espn_scoreboard_endpoint']}{week + 1 if week == 0 else week}")
    cbs_games_page: BeautifulSoup = extract.all_cbs_games_in_week(f"{season_properties['cbs_scoreboard_week_url']}/{week + 1 if week == 0 else week}")
    cbs_odds: BeautifulSoup = extract.all_cbs_odds_in_week(f"{season_properties['cbs_odds_week_url']}{week + 1 if week == 0 else week}")
    fox_games_page: BeautifulSoup = extract.all_fox_games_in_week(f"{season_properties['fox_schedule_week_url']}{week + 1 if week == 0 else week}")

    for espn_game in espn_games:
        print(f"\nProcessing Week {week} Game ID: {espn.game.extract_game_id(espn_game)}")
        cbs_game: BeautifulSoup = extract.cbs_game_scorecard(cbs_games_page, espn.game.extract_game_id(espn_game), week)
        fox_url: str = f"{extract.fox_game_url(fox_games_page, espn.game.extract_game_id(espn_game), week)}?tab=odds"
        fox_game: BeautifulSoup = extract.scrape_fox_game_odds_tab(fox_url)
        
        game: Game = Game(espn_game, cbs_game, cbs_odds, fox_url, fox_game)
        game.league = season_properties['league']


        mysql.load_team({
            "team_id": game.away_team_id,
            "league": season_properties["league"],
            "cbs_code": f"{cbs.get_away_team_abbreviation(game.cbs_code)}/{mapping.espn_to_cbs_team_code_mapping.get(game.away_team_id, game.away_team_id)}",
            "espn_code": espn_game["competitions"][0]["competitors"][0]["team"]["id"] if espn_game["competitions"][0]["competitors"][0]["homeAway"] == "away" else espn_game["competitions"][0]["competitors"][1]["team"]["id"],
            "fox_code": mapping.espn_to_fox_team_code_mapping.get(game.away_team_id, game.away_team_id),
            
            "vegas_code": "", "conference_code": None, "conference_name": None, "division_name": None, "team_name": None,
            "team_mascot": None, "power_conference": None, "team_logo_url": None, "primary_color": None, "alternate_color": None
        })

        mysql.load_box_scores(transform.away_box_score(game))
        mysql.load_box_scores(transform.home_box_score(game))
        mysql.load_location(transform.location(game))
        mysql.load_odds(transform.odds(game))
        mysql.load_game(transform.game(game))



def extract_transform_load_teams(season_properties: dict) -> None:
    """Method to perfom ETL process for teams data from various sources"""
    print(f"\n")
    distinct_teams: list[dict] = mysql.get_distinct_teams(season_properties["league"])
    for distinct_team in distinct_teams:
        print(f"\nProcessing Team: {distinct_team['TEAM_ID']}")
        distinct_team = {key.lower(): value for key, value in distinct_team.items()}

        espn_team: dict = extract.get_espn_team(f"{season_properties['espn_team_endpoint']}/{distinct_team['espn_code']}")
        cbs_team: dict = extract.scrape_cbs_team_stats(f"{season_properties['cbs_team_endpoint']}/{extract.map_espn_team_code_to_cbs_team_code(distinct_team['team_id'])}/stats/")

        team: Team = Team(espn_team, cbs_team)
        team.league = distinct_team["league"]
        team.cbs_code = distinct_team["cbs_code"]
        team.espn_code = distinct_team["espn_code"]
        team.fox_code = distinct_team["fox_code"]
        team.vegas_code = ""

        mysql.load_record(transform.conference_record(team))
        mysql.load_record(transform.overall_record(team))
        mysql.load_team_stats(transform.team_stats(team))
        mysql.load_team(transform.team(team))
