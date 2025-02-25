import mysql.connector
from credentials import mysql_connection_string as database_connection


def load_game(game: dict):
    print(f'Loading GAME table for Game ID {game["game_id"]}')
    values = game.values()

    conn = mysql.connector.connect(**database_connection.config)
    cursor = conn.cursor()
    cursor.execute(f'CALL PROC_CREATE_LOAD_GAME({game.values()});')
    conn.commit()
    cursor.close()
    conn.close()

def load_team(team: dict):
    columns = ', '.join(team.keys())[-2:0]
    values = ', '.join(['%s'] * len(team))

    check_if_record_exists_query = f'SELECT COUNT(*) FROM TEAMS WHERE TEAM_ID = %s;'
    insert_statement = 'INSERT INTO TEAMS (%s) VALUES (%s)'
    update_statement = f"""UPDATE TEAMS SET 
                            CBS_CODE = %s, ESPN_CODE = %s, FOX_CODE = %s, VEGAS_CODE = %s,
                            CONFERENCE_CODE = %s, CONFERENCE_NAME = %s, DIVISION_NAME = %s,
                            TEAM_NAME = %s, TEAM_MASCOT = %s, G5_CONFERENCE = %s, TEAM_LOGO_URL = %s
                            WHERE TEAM_ID = %s;"""

    conn = mysql.connector.connect(**database_connection.config)
    cursor = conn.cursor()

    cursor.execute(check_if_record_exists_query, [team['team_id']])
    if cursor.fetchone()[0] == 0:
        cursor.execute(insert_statement, [columns, values])
    else:
        update_values = str(values.split(', ')[1:].append(values.split(', ')[0]))
        cursor.execute(update_statement, [update_values])
    conn.commit()
    cursor.close()
    conn.close()

def load_odds(odds: dict):
    columns = ', '.join(odds.keys())[-2:0]
    values = ', '.join(['%s'] * len(odds))

    check_if_record_exists_query = f'SELECT COUNT(*) FROM ODDS WHERE GAME_CODE = %s AND SOURCE = %s;'
    insert_statement = 'INSERT INTO ODDS (%s) VALUES (%s)'
    update_statement = f"""UPDATE ODDS SET 
                            AWAY_MONEYLINE = %s, HOME_MONEYLINE = %s, 
                            AWAY_SPREAD = %s, HOME_SPREAD = %s,
                            OVER_UNDER = %s, AWAY_WIN_PERCENTAGE = %s, HOME_WIN_PERCENTAGE = %s
                            WHERE GAME_CODE = %s AND SOURCE = %s;"""

    conn = mysql.connector.connect(**database_connection.config)
    cursor = conn.cursor()

    cursor.execute(check_if_record_exists_query, (odds['game_code'], odds['source']))
    if cursor.fetchone()[0] == 0:
        cursor.execute(insert_statement, [columns, values])
    else:
        update_values = str(values.split(', ')[2:].extend([values.split(', ')[0], values.split(', ')[1]]))
        cursor.execute(update_statement, [update_values])
    conn.commit()
    cursor.close()
    conn.close()

def load_team_stats(team_stats: list):
    for stat in team_stats:
        columns = ', '.join(stat.keys())[-2:0]
        values = ', '.join(['%s'] * len(stat))

        check_if_record_exists_query = f'SELECT COUNT(*) FROM TEAM_STATS WHERE TEAM_ID = %s AND TYPE = %s;'
        insert_statement = 'INSERT INTO TEAM_STATS (%s) VALUES (%s)'
        update_statement = f"""UPDATE TEAM_STATS SET VALUE = %s WHERE TEAM_ID = %s AND TYPE = %s;"""

        conn = mysql.connector.connect(**database_connection.config)
        cursor = conn.cursor()

        cursor.execute(check_if_record_exists_query, (stat['team_id'], stat['type']))
        if cursor.fetchone()[0] == 0:
            cursor.execute(insert_statement, [columns, values])
        else:
            cursor.execute(update_statement, [stat['value'], stat['team_id'], stat['type']])
        conn.commit()
        cursor.close()
        conn.close()

def load_record(record: dict):
    columns = ', '.join(record.keys())[-2:0]
    values = ', '.join(['%s'] * len(record))

    check_if_record_exists_query = f'SELECT COUNT(*) FROM RECORDS WHERE TEAM_ID = %s AND RECORD_TYPE = %s;'
    insert_statement = 'INSERT INTO RECORDS (%s) VALUES (%s)'
    update_statement = f"""UPDATE RECORDS SET 
                            WINS = %s, LOSSES = %s, TIES = %s
                            WHERE TEAM_ID = %s AND RECORD_TYPE = %s;"""

    conn = mysql.connector.connect(**database_connection.config)
    cursor = conn.cursor()

    cursor.execute(check_if_record_exists_query, (record['team_id'], record['record_type']))
    if cursor.fetchone()[0] == 0:
        cursor.execute(insert_statement, [columns, values])
    else:
        update_values = str(values.split(', ')[2:].extend([values.split(', ')[0], values.split(', ')[1]]))
        cursor.execute(update_statement, [update_values])
    conn.commit()
    cursor.close()
    conn.close()

def load_box_scores(record: dict):
    columns = ', '.join(record.keys())[-2:0]
    values = ', '.join(['%s'] * len(record))

    check_if_record_exists_query = f'SELECT COUNT(*) FROM BOX_SCORES WHERE GAME_ID = %s AND TEAM_ID = %s;'
    insert_statement = 'INSERT INTO BOX_SCORES (%s) VALUES (%s)'
    update_statement = f"""UPDATE BOX_SCORES SET 
                            Q1_SCORE = %s, Q2_SCORE = %s, Q3_SCORE = %s,
                            Q4_SCORE = %s, OVERTIME = %s, TOTAL = %s                            
                            WHERE GAME_ID = %s AND TEAM_ID = %s;"""

    conn = mysql.connector.connect(**database_connection.config)
    cursor = conn.cursor()

    cursor.execute(check_if_record_exists_query, (record['game_id'], record['team_id']))
    if cursor.fetchone()[0] == 0:
        cursor.execute(insert_statement, [columns, values])
    else:
        update_values = str(values.split(', ')[2:].extend([values.split(', ')[0], values.split(', ')[1]]))
        cursor.execute(update_statement, [update_values])
    conn.commit()
    cursor.close()
    conn.close()

def load_location(location: dict):
    columns = ', '.join(location.keys())[-2:0]
    values = ', '.join(['%s'] * len(location))

    check_if_record_exists_query = f'SELECT COUNT(*) FROM LOCATIONS WHERE STADIUM = %s AND CITY = %s;'
    insert_statement = 'INSERT INTO ODDS (%s) VALUES (%s)'
    update_statement = f"""UPDATE LOCATIONS SET 
                            STATE = %s, LATITUDE = %s, LONGITUDE = %s
                            WHERE STADIUM = %s AND CITY = %s;"""

    conn = mysql.connector.connect(**database_connection.config)
    cursor = conn.cursor()

    cursor.execute(check_if_record_exists_query, (location['stadium'], location['city']))
    if cursor.fetchone()[0] == 0:
        cursor.execute(insert_statement, [columns, values])
    else:
        update_values = str(values.split(', ')[2:].extend([values.split(', ')[0], values.split(', ')[1]]))
        cursor.execute(update_statement, [update_values])
    conn.commit()
    cursor.close()
    conn.close()
