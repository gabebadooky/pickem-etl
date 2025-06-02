import mysql.connector
from credentials import mysql_connection_string as database_connection

def instantiate_procedure_params(data_dict: dict):
    procedure_params = f""
    for key in data_dict:
        dict_key = data_dict[key]
        if isinstance(dict_key, int) or isinstance(dict_key, float):
            procedure_params += f"{dict_key}, "
        elif dict_key is None:
            procedure_params += 'NULL, '
        else:
            dict_key = dict_key.replace("'", "''")
            procedure_params += f"'{dict_key}', "
    procedure_params = procedure_params.rstrip(', ')
    return procedure_params

def call_proc(sql: str):
    print(sql)
    conn = mysql.connector.connect(**database_connection.config)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print('SQL Committed...')
    cursor.close()
    conn.close()


def load_record(record: dict):
    procedure_params = instantiate_procedure_params(record)
    sql_statement = f'CALL PROC_LOAD_RECORD({procedure_params});'
    call_proc(sql_statement)

def load_team_stats(team_stats: list):
    for stat in team_stats:
        procedure_params = instantiate_procedure_params(stat)
        sql_statement = f'CALL PROC_LOAD_STATS({procedure_params});'
        call_proc(sql_statement)

def load_team(team: dict):
    procedure_params = instantiate_procedure_params(team)
    sql_statement = f'CALL PROC_LOAD_TEAM({procedure_params});'
    call_proc(sql_statement)


def load_box_scores(box_score: dict):
    procedure_params = instantiate_procedure_params(box_score)
    sql_statement = f'CALL PROC_LOAD_BOX_SCORE({procedure_params});'
    call_proc(sql_statement)

def load_location(location: dict):
    procedure_params = instantiate_procedure_params(location)
    sql_statement = f'CALL PROC_LOAD_LOCATION({procedure_params});'
    call_proc(sql_statement)

def load_odds(odds: dict):
    procedure_params = instantiate_procedure_params(odds)
    sql_statement = f'CALL PROC_LOAD_ODDS({procedure_params});'
    call_proc(sql_statement)

def load_game(game: dict):
    procedure_params = instantiate_procedure_params(game)
    sql_statement = f'CALL PROC_LOAD_GAME({procedure_params});'
    call_proc(sql_statement)