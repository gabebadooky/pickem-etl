import mysql.connector, os, time
from dotenv import load_dotenv

load_dotenv()
db_config: dict = {
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "host": os.getenv("HOST"),
    "port": int(os.getenv("PORT")),
    "database": os.getenv("DATABASE"),
    "auth_plugin": os.getenv("AUTH_PLUGIN")
}


def get_distinct_teams(league: str) -> list:
    """Method to retrieve all distinct teams from TEAMS table"""
    sql: str = f"SELECT * FROM TEAMS WHERE LEAGUE = '{league}'"
    connected: bool = False
    while not connected:
        try:
            conn = mysql.connector.connect(**db_config)
            connected = True
        except Exception as e:
            print(f"Error occurred while connecting to the database for statement: {sql}\n{e}")
            time.sleep(1)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql)
    distinct_teams: list = cursor.fetchall()
    cursor.close()
    conn.close()
    return distinct_teams


def instantiate_procedure_params(data_dict: dict) -> str:
    """Method to convert dictionary keys into SQL statement VALUES parameters for database load"""
    procedure_params: str = ""
    for key in data_dict:
        dict_key: any = data_dict[key]
        if isinstance(dict_key, int) or isinstance(dict_key, float):
            procedure_params += f"{dict_key}, "
        elif dict_key is None:
            procedure_params += 'NULL, '
        else:
            dict_key = dict_key.replace("'", "''")
            procedure_params += f"'{dict_key}', "
    procedure_params = procedure_params.rstrip(", ")
    return procedure_params

def call_proc(sql: str) -> None:
    """Method to call given database procedure"""
    print(sql)
    connected: bool = False
    while not connected:
        try:
            conn = mysql.connector.connect(**db_config)
            connected = True
        except Exception as e:
            print(f"Error occurred while connecting to the database for statement: {sql}\n{e}")
            time.sleep(1)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def load_record(record: dict) -> None:
    """Method to construct and call SQL to load given record (in dictionary format) into MySQL Database"""
    procedure_params: str = instantiate_procedure_params(record)
    sql_statement: str = f"CALL PROC_LOAD_RECORD({procedure_params});"
    call_proc(sql_statement)

def load_team_stats(team_stats: list) -> None:
    """Method to construct and call SQL to load team_stats into MySQL Database"""
    for stat in team_stats:
        procedure_params: str = instantiate_procedure_params(stat)
        sql_statement: str = f"CALL PROC_LOAD_STATS({procedure_params});"
        call_proc(sql_statement)

def load_team(team: dict) -> None:
    """Method to construct and call SQL to load team into MySQL Database"""
    procedure_params: str = instantiate_procedure_params(team)
    sql_statement: str = f"CALL PROC_LOAD_TEAM({procedure_params});"
    call_proc(sql_statement)


def load_box_scores(box_score: dict) -> None:
    """Method to construct and call SQL to load box_scores into MySQL Database"""
    procedure_params: str = instantiate_procedure_params(box_score)
    sql_statement: str = f"CALL PROC_LOAD_BOX_SCORE({procedure_params});"
    call_proc(sql_statement)

def load_location(location: dict) -> None:
    """Method to construct and call SQL to load locations into MySQL Database"""
    procedure_params: str = instantiate_procedure_params(location)
    sql_statement: str = f"CALL PROC_LOAD_LOCATION({procedure_params});"
    call_proc(sql_statement)

def load_odds(odds: list[dict]) -> None:
    """Method to construct and call SQL to load odds into MySQL Database"""
    for metric in odds:
        procedure_params: str = instantiate_procedure_params(metric)
        sql_statement: str = f"CALL PROC_LOAD_ODDS({procedure_params});"
        call_proc(sql_statement)

def load_game(game: dict) -> None:
    """Method to construct and call SQL to load game into MySQL Database"""
    procedure_params: str = instantiate_procedure_params(game)
    sql_statement: str = f"CALL PROC_LOAD_GAME({procedure_params});"
    call_proc(sql_statement)