def get_all_stats_table_wrappers(team_stats_page: str) -> str:
    return team_stats_page.find_all("div", class_="TableBaseWrapper")

def get_table_total_rows(stats_table_wrapper: str) -> str:
    return stats_table_wrapper.find("table", class_="TableBase-table").find("tbody").find_all("tr", class_="TableBase-bodyTr--total")




def get_team_pass_attempts(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[0][2]


def get_team_pass_completions(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[0][3]


def get_team_completion_percentage(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[0][4]


def get_team_pass_yards(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[0][5]


def get_team_passing_touchdowns(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[0][6]


def get_team_offense_interceptions(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[0][7]




def get_opp_pass_attempts(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[1][2]


def get_opp_pass_completions(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[1][3]


def get_opp_completion_percentage(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[1][4]


def get_opp_pass_yards(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[1][5]


def get_opp_passing_touchdowns(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[1][6]


def get_opp_defense_interceptions(team_stats_page: str) -> str:
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    return get_table_total_rows(stats_table_wrapper)[1][7]




def get_team_rush_yards(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    return get_table_total_rows(stats_table_wrapper)[0][3]


def get_team_rush_attempts(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    return get_table_total_rows(stats_table_wrapper)[0][2]


def get_team_yard_per_rush(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    return get_table_total_rows(stats_table_wrapper)[0][4]


def get_team_rush_touchdowns(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    return get_table_total_rows(stats_table_wrapper)[0][5]




def get_opp_rush_yards(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    return get_table_total_rows(stats_table_wrapper)[1][3]


def get_opp_rush_attempts(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    return get_table_total_rows(stats_table_wrapper)[1][2]


def get_opp_yard_per_rush(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    return get_table_total_rows(stats_table_wrapper)[1][4]


def get_opp_rush_touchdowns(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    return get_table_total_rows(stats_table_wrapper)[1][5]