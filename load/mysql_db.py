import mysql.connector
from credentials import mysql_connection_string as database_connection


def load_game(game: dict):
    columns = ', '.join(game.keys())
    values = ', '.join(['%s'] * len(game))

    check_if_record_exists_query = f'SELECT COUNT(*) FROM GAMES WHERE GAME_ID = %s;'
    insert_statement = 'INSERT INTO GAMES (%s) VALUES (%s)'
    update_statement = f"""UPDATE GAMES SET 
                            LEAGUE = %s, WEEK = %s, CBS_CODE = %s, ESPN_CODE = %s, 
                            FOX_CODE = %s, VEGAS_CODE = %s, AWAY_TEAM_ID = %s, 
                            HOME_TEAM_ID = %s, DATE = %s, TIME = %s, TV_COVERAGE = %s, 
                            STADIUM = %s, CITY = %s, STATE = %s, GAME_FINISHED = %s
                            WHERE GAME_ID = %s;"""

    conn = mysql.connector.connect(database_connection.config)
    cursor = conn.cursor()

    cursor.execute(check_if_record_exists_query, game['game_id'])
    if cursor.fetchone()[0] == 0:
        cursor.execute(insert_statement, (columns, values))
    else:
        update_values = str(values.split(', ')[1:].append(values.split(', ')[0]))
        cursor.execute(update_statement, update_values)
    conn.commit()
    cursor.close()
    conn.close()

def load_team(team: dict):
    columns = ', '.join(team.keys())
    values = ', '.join(['%s'] * len(team))

    check_if_record_exists_query = f'SELECT COUNT(*) FROM TEAMS WHERE TEAM_ID = %s;'
    insert_statement = 'INSERT INTO TEAMS (%s) VALUES (%s)'
    update_statement = f"""UPDATE TEAMS SET 
                            CBS_CODE = %s, ESPN_CODE = %s, FOX_CODE = %s, VEGAS_CODE = %s,
                            CONFERENCE_CODE = %s, CONFERENCE_NAME = %s, DIVISION_NAME = %s,
                            TEAM_NAME = %s, TEAM_MASCOT = %s, G5_CONFERENCE = %s, TEAM_LOGO_URL = %s
                            WHERE TEAM_ID = %s;"""

    conn = mysql.connector.connect(database_connection.config)
    cursor = conn.cursor()

    cursor.execute(check_if_record_exists_query, team['team_id'])
    if cursor.fetchone()[0] == 0:
        cursor.execute(insert_statement, (columns, values))
    else:
        update_values = str(values.split(', ')[1:].append(values.split(', ')[0]))
        cursor.execute(update_statement, update_values)
    conn.commit()
    cursor.close()
    conn.close()

def load_odds(odds: dict):
    columns = ', '.join(odds.keys())
    values = ', '.join(['%s'] * len(odds))

    check_if_record_exists_query = f'SELECT COUNT(*) FROM ODDS WHERE GAME_CODE = %s AND SOURCE = %s;'
    insert_statement = 'INSERT INTO ODDS (%s) VALUES (%s)'
    update_statement = f"""UPDATE ODDS SET 
                            GAME_ID = %s, GAME_CODE = %s, SOURCE = %s, AWAY_MONEYLINE = %s,
                            HOME_MONEYLINE = %s, AWAY_SPREAD = %s, HOME_SPREAD = %s,
                            OVER_UNDER = %s, AWAY_WIN_PERCENTAGE = %s, HOME_WIN_PERCENTAGE = %s
                            WHERE GAME_CODE = %s AND SOURCE = %s;"""

    conn = mysql.connector.connect(database_connection.config)
    cursor = conn.cursor()

    cursor.execute(check_if_record_exists_query, (odds['game_code'], odds['source']))
    if cursor.fetchone()[0] == 0:
        cursor.execute(insert_statement, (columns, values))
    else:
        update_values = str(values.split(', ')[2:].extend([values.split(', ')[0], values.split(', ')[1]]))
        cursor.execute(update_statement, update_values)
    conn.commit()
    cursor.close()
    conn.close()

def load_team_stats(team_stats: list):
    for stat in team_stats:
        columns = ', '.join(stat.keys())
        values = ', '.join(['%s'] * len(stat))

        check_if_record_exists_query = f'SELECT COUNT(*) FROM TEAM_STATS WHERE TEAM_ID = %s AND TYPE = %s;'
        insert_statement = 'INSERT INTO TEAM_STATS (%s) VALUES (%s)'
        update_statement = f"""UPDATE TEAM_STATS SET VALUE = %s WHERE TEAM_ID = %s AND TYPE = %s;"""

        conn = mysql.connector.connect(database_connection.config)
        cursor = conn.cursor()

        cursor.execute(check_if_record_exists_query, (stat['team_id'], stat['type']))
        if cursor.fetchone()[0] == 0:
            cursor.execute(insert_statement, (columns, values))
        else:
            cursor.execute(update_statement, (stat['value'], stat['team_id'], stat['type']))
        conn.commit()
        cursor.close()
        conn.close()