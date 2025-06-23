def get_all_stats_table_wrappers(team_stats_page: str) -> str:
    """Method to extract all Stats tables from CBS team stats endpoint response"""
    return team_stats_page.find_all("div", class_="TableBaseWrapper")

def get_table_total_rows(stats_table_wrapper: str) -> str:
    """Method to extract team and opponent statistic type totals CBS team stats endpoint response"""
    return stats_table_wrapper.find("table", class_="TableBase-table").find("tbody").find_all("tr", class_="TableBase-bodyTr--total")




def get_team_pass_attempts(team_stats_page: str) -> str:
    """Method to extract team pass attempts from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[0]
    return total_row.find_all("td")[2].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[0][2]


def get_team_pass_completions(team_stats_page: str) -> str:
    """Method to extract team pass completions from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[0]
    return total_row.find_all("td")[3].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[0][3]


def get_team_completion_percentage(team_stats_page: str) -> str:
    """Method to extract team completion percentage from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[0]
    return total_row.find_all("td")[4].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[0][4]


def get_team_pass_yards(team_stats_page: str) -> str:
    """Method to extract team pass yards from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[0]
    return total_row.find_all("td")[5].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[0][5]


def get_team_passing_touchdowns(team_stats_page: str) -> str:
    """Method to extract team passing touchdowns from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[0]
    return total_row.find_all("td")[6].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[0][6]


def get_team_offense_interceptions(team_stats_page: str) -> str:
    """Method to extract team offense interceptions from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[0]
    return total_row.find_all("td")[7].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[0][7]




def get_opp_pass_attempts(team_stats_page: str) -> str:
    """Method to extract opponent pass attempts from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[1]
    return total_row.find_all("td")[2].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[1][2]


def get_opp_pass_completions(team_stats_page: str) -> str:
    """Method to extract opponent pass completions from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[1]
    return total_row.find_all("td")[3].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[1][3]


def get_opp_completion_percentage(team_stats_page: str) -> str:
    """Method to extract opponent completion percentage from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[1]
    return total_row.find_all("td")[4].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[1][4]


def get_opp_pass_yards(team_stats_page: str) -> str:
    """Method to extract opponent pass yards from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[1]
    return total_row.find_all("td")[5].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[1][5]


def get_opp_passing_touchdowns(team_stats_page: str) -> str:
    """Method to extract opponent pass touchdowns from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[1]
    return total_row.find_all("td")[6].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[1][6]


def get_team_defense_interceptions(team_stats_page: str) -> str:
    """Method to extract team defense interceptions from CBS team stats endpoint response"""
    # Player | GP | ATT | CMP | PCT | YDS | TD | INT
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[0]
    total_row: str = get_table_total_rows(stats_table_wrapper)[1]
    return total_row.find_all("td")[7].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[1][7]




def get_team_rush_yards(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    total_row: str = get_table_total_rows(stats_table_wrapper)[0]
    return total_row.find_all("td")[3].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[0][3]


def get_team_rush_attempts(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    total_row: str = get_table_total_rows(stats_table_wrapper)[0]
    return total_row.find_all("td")[2].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[0][2]


def get_team_yard_per_rush(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    total_row: str = get_table_total_rows(stats_table_wrapper)[0]
    return total_row.find_all("td")[4].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[0][4]


def get_team_rush_touchdowns(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    total_row: str = get_table_total_rows(stats_table_wrapper)[0]
    return total_row.find_all("td")[5].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[0][5]




def get_opp_rush_yards(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    total_row: str = get_table_total_rows(stats_table_wrapper)[1]
    return total_row.find_all("td")[3].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[1][3]


def get_opp_rush_attempts(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    total_row: str = get_table_total_rows(stats_table_wrapper)[1]
    return total_row.find_all("td")[2].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[1][2]


def get_opp_yard_per_rush(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    total_row: str = get_table_total_rows(stats_table_wrapper)[1]
    return total_row.find_all("td")[4].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[1][4]


def get_opp_rush_touchdowns(team_stats_page: str) -> str:
    # Player | GP | ATT | YDS | AVG | TD
    stats_table_wrapper: str = get_all_stats_table_wrappers(team_stats_page)[1]
    total_row: str = get_table_total_rows(stats_table_wrapper)[1]
    return total_row.find_all("td")[5].get_text().strip()
    # return get_table_total_rows(stats_table_wrapper)[1][5]