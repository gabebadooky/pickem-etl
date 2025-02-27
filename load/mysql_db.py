import mysql.connector
from credentials import mysql_connection_string as database_connection

def call_proc(sql: str):
    conn = mysql.connector.connect(**database_connection.config)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def load_game(game: dict):
    procedure_params = f""
    for key in game:
        procedure_params += f"{game[key]}, " if isinstance(game[key], int) else f"'{game[key]}', "
    procedure_params = procedure_params.rstrip(', ')

    sql_statement = f'CALL PROC_LOAD_GAME({procedure_params});'
    print(sql_statement)
    call_proc(sql_statement)

def load_team(team: dict):
    sql_statement = f'CALL PROC_LOAD_TEAM({team.values()});'
    call_proc(sql_statement)

def load_odds(odds: dict):
    sql_statement = f'CALL PROC_LOAD_ODDS({odds.values()});'
    call_proc(sql_statement)

def load_team_stats(team_stats: list):
    for stat in team_stats:
        sql_statement = f'CALL PROC_LOAD_STATS({stat.values()});'
        call_proc(sql_statement)

def load_record(record: dict):
    sql_statement = f'CALL PROC_LOAD_RECORD({record.values()});'
    call_proc(sql_statement)

def load_box_scores(box_score: dict):
    sql_statement = f'CALL PROC_LOAD_BOX_SCORE({box_score.values()});'
    call_proc(sql_statement)

def load_location(location: dict):
    sql_statement = f'CALL PROC_LOAD_LOCATION({location.values()});'
    call_proc(sql_statement)
