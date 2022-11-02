import mysql.connector
import pandas as pd
import numpy as np
import getpass
import os

def insertion():
    
    def get_password(): 
        password = getpass.getpass("password: ")
        return password

    os.system("clear")
    print("please insert your data to insert the information into the db.")
    user = input('User: ')
    password = get_password()

    season_db = pd.read_csv('data_cleanned/season.csv')
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='NBA_DB',
                                            user=user,
                                            password=password)

        mySql_insert_query = """INSERT INTO Seasons (SEASON_ID, YEAR) 
                            VALUES (%s, %s) """
        
        records_to_insert = season_db.to_numpy().tolist()

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Season table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    
    players_db = pd.read_csv('data_cleanned/players_db.csv')
    players_db1 = players_db.drop_duplicates()

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='NBA_DB',
                                            user=user,
                                            password=password)

        mySql_insert_query = """INSERT INTO Players (PLAYER_ID, PLAYER_NAME) 
                            VALUES (%s, %s) """
        
        records_to_insert = players_db1.to_numpy().tolist()

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Season table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    arenas_db = pd.read_csv('data_cleanned/arenas.csv')
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='NBA_DB',
                                            user=user,
                                            password=password)

        mySql_insert_query = """INSERT INTO Arenas (ARENA_ID, ARENA_NAME, ARENACAPACITY) 
                            VALUES (%s, %s, %s) """
        
        records_to_insert = arenas_db.to_numpy().tolist()

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Season table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


    cities_db = pd.read_csv('data_cleanned/cities.csv')
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='NBA_DB',
                                            user=user,
                                            password=password)

        mySql_insert_query = """INSERT INTO Cities (CITY_ID, CITY_NAME, ARENA_ID) 
                            VALUES (%s, %s, %s) """
        
        records_to_insert = cities_db.to_numpy().tolist()

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Season table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    teams_db = pd.read_csv('data_cleanned/teams_db.csv')
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='NBA_DB',
                                            user=user,
                                            password=password)

        mySql_insert_query = """INSERT INTO Teams (TEAM_ID, TEAM_NAME, ABBREVIATION, NICKNAME,YEARFOUNDED,MIN_YEAR, MAX_YEAR, CITY_ID, OWNER,GENNERALMANAGER,HEADCOACH,LEAGUE_ID,DLEAGUEAFFILIATION) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        
        records_to_insert = teams_db.to_numpy().tolist()

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Season table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    games_db = pd.read_csv('data_cleanned/games_db.csv')
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='NBA_DB',
                                            user=user,
                                            password=password)

        mySql_insert_query = """INSERT INTO Games (GAME_ID, GAME_STATUS_TEXT, SEASON_ID, HOME_TEAM_ID, PTS_home, FG_PCT_home, FT_PCT_home, FG3_PCT_home, AST_home, REB_home, VISITOR_TEAM_ID, PTS_away, FG_PCT_away, FT_PCT_away, FG3_PCT_away, AST_awat, REB_away, HOME_TEAM_WINS) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        
        records_to_insert = games_db.to_numpy().tolist()

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Season table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    game_details_db = pd.read_csv('data_cleanned/game_details_db.csv')
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='NBA_DB',
                                            user=user,
                                            password=password)

        mySql_insert_query = """INSERT INTO Game_details (ID,GAME_ID,TEAM_ID,PLAYER_ID, START_POSITION, COMMENT,MIN,FGM, FGA, FG_PCT, FG3M,FG3A,FG3_PCT,FTM,FTA,FT_PCT,OREB,DREB,AST,STL,BLK,TO_,PF,PTS,PLUS_MINUS) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        
        records_to_insert = game_details_db.to_numpy().tolist()

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Season table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    players_at_team_in_season_db = pd.read_csv('data_cleanned/players_at_team_in_season.csv')
    del(players_at_team_in_season_db['PLAYER_NAME'])

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='NBA_DB',
                                            user=user,
                                            password=password)

        mySql_insert_query = """INSERT INTO Players_at_team_in_season (ID, PLAYER_ID, TEAM_ID, SEASON_ID) 
                            VALUES (%s, %s, %s, %s) """
        
        records_to_insert = players_at_team_in_season_db.to_numpy().tolist()

        cursor = connection.cursor()
        cursor.executemany(mySql_insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Season table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    #Relations:
    connection = mysql.connector.connect(host='localhost',
                                         database='NBA_DB',
                                         user=user,
                                         password=password)

    cursor = connection.cursor()
    cursor.execute('USE NBA_DB')

    #ursorcities relations
    cursor.execute('ALTER TABLE Cities ADD FOREIGN KEY (ARENA_ID) REFERENCES Arenas(ARENA_ID);')

    #ursorteams relations
    cursor.execute('ALTER TABLE Teams ADD FOREIGN KEY (CITY_ID) REFERENCES Cities(CITY_ID);')

    #ursorgame details relations
    cursor.execute('ALTER TABLE Game_details ADD FOREIGN KEY (GAME_ID) REFERENCES Games(GAME_ID);')
    cursor.execute('ALTER TABLE Game_details ADD FOREIGN KEY (TEAM_ID) REFERENCES Teams(TEAM_ID);')
    #cursor.execute('ALTER TABLE Game_details ADD FOREIGN KEY (PLAYER_ID) REFERENCES Players(PLAYER_ID);')

    #cursorgames relations
    cursor.execute('ALTER TABLE Games ADD FOREIGN KEY (SEASON_ID) REFERENCES Seasons(SEASON_ID);')
    cursor.execute('ALTER TABLE Games ADD FOREIGN KEY (HOME_TEAM_ID) REFERENCES Teams(TEAM_ID);')
    cursor.execute('ALTER TABLE Games ADD FOREIGN KEY (VISITOR_TEAM_ID) REFERENCES Teams(TEAM_ID);')

    #cursorplayer at team
    #cursor.execute('ALTER TABLE Players_at_team_in_season ADD FOREIGN KEY (PLAYER_ID) REFERENCES Players(PLAYER_ID);')
    #cursor.execute('ALTER TABLE Players_at_team_in_season ADD FOREIGN KEY (TEAM_ID) REFERENCES Teams(TEAM_ID);')
    cursor.execute('ALTER TABLE Players_at_team_in_season ADD FOREIGN KEY (SEASON_ID) REFERENCES Seasons(SEASON_ID);')