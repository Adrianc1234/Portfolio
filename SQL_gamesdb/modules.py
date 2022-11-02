import os
import mysql.connector
import getpass

#get password
def get_password(): 
    password = getpass.getpass("password: ")
    return password

#loggin
def login():
    user = input('User: ')
    password = get_password()
    mydb = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password
    )
    return mydb

#verify if our bd exists
def show_db(mydb):
    c = mydb.cursor()
    c.execute("SHOW DATABASES")
    for dbs in c:
        if dbs[0] ==  'NBA_DB':
            print('The datase already exists')
        else:
            pass

#creating our db
def create_db(mydb):
    c = mydb.cursor()
    c.execute("CREATE DATABASE NBA_DB")
    print("Database NBA_DB has been created")

#making game table
def game_t(mydb):
    c = mydb.cursor()
    try:
        structure = "GAME_ID int NOT NULL,\
                    GAME_STATUS_TEXT CHAR(50) NOT NULL,\
                    SEASON_ID int NOT NULL,\
                    HOME_TEAM_ID int NOT NULL,\
                    PTS_home float,\
                    FG_PCT_home float,\
                    FT_PCT_home float,\
                    FG3_PCT_home float,\
                    AST_home float,\
                    REB_home float,\
                    VISITOR_TEAM_ID int NOT NULL,\
                    PTS_away float,\
                    FG_PCT_away float,\
                    FT_PCT_away float,\
                    FG3_PCT_away float,\
                    AST_awat float,\
                    REB_away float,\
                    HOME_TEAM_WINS boolean NOT NULL,\
                    PRIMARY KEY (GAME_ID)"
        c.execute(f'CREATE TABLE Games ({structure})')
    except:
        pass
  
#making Arenas table
def Arenas_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')
    #try to build
    try:
        structure = "ARENA_ID int NOT NULL,\
                    ARENA_NAME char(50) NOT NULL,\
                    ARENACAPACITY float NOT NULL,\
                    PRIMARY KEY (ARENA_ID )"
        c.execute(f'CREATE TABLE Arenas ({structure})')
    #if it exists just pass
    except:
        #print('Algo paso')
        pass  

#Making cities table
def Cities_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #try to build
    try:
        structure = "CITY_ID int NOT NULL,\
                    CITY_NAME char(50) NOT NULL,\
                    ARENA_ID int NOT NULL,\
                    PRIMARY KEY (CITY_ID)"
        c.execute(f'CREATE TABLE Cities ({structure})')

    #if it exists just pass
    except:
        #print('Algo paso ')
        pass
    
#Making Teams table
def Teams_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')
    
    #try to build
    try:
        structure = "TEAM_ID int NOT NULL,\
                    TEAM_NAME char(50) NOT NULL,\
                    ABBREVIATION char(10) NOT NULL,\
                    NICKNAME char(50) NOT NULL,\
                    YEARFOUNDED int NOT NULL,\
                    MIN_YEAR int NOT NULL,\
                    MAX_YEAR int NOT NULL,\
                    CITY_ID int NOT NULL,\
                    OWNER char(50) NOT NULL,\
                    GENNERALMANAGER char(50) NOT NULL,\
                    HEADCOACH char(50) NOT NULL,\
                    LEAGUE_ID char(50) NOT NULL,\
                    DLEAGUEAFFILIATION char(50) NOT NULL,\
                    PRIMARY KEY (TEAM_ID)"
        c.execute(f'CREATE TABLE Teams ({structure})')

    #if it exists just pass
    except:
        pass
    
#Making Seasons table
def Seasons_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #try to build
    try:
        structure = "SEASON_ID int NOT NULL,\
                    YEAR int NOT NULL,\
                    PRIMARY KEY (SEASON_ID)"
        c.execute(f'CREATE TABLE Seasons ({structure})')

    #if it exists just pass
    except:
        #print('Algo paso ')
        pass
    
#Making PLayers table
def Players_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #try to build
    try:
        structure = "PLAYER_ID int NOT NULL,\
                    PLAYER_NAME char(50) NOT NULL,\
                    PRIMARY KEY (PLAYER_ID)"
        c.execute(f'CREATE TABLE Players ({structure})')

    #if it exists just pass
    except:
        #print('Algo paso ')
        pass

#Making players at team table
def player_at_the_season(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #try to build
    try:
        structure = "ID int NOT NULL,\
                    PLAYER_ID int NOT NULL,\
                    TEAM_ID int NOT NULL,\
                    SEASON_ID int NOT NULL,\
                    PRIMARY KEY (ID)"

        c.execute(f'CREATE TABLE Players_at_team_in_season ({structure})')

    #if it exists just pass
    except:
        #print('Algo paso ')
        pass
    
#Making Game_details table
def Game_details_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #try to build
    try:
        structure = "ID int NOT NULL,\
                    GAME_ID int NOT NULL,\
                    TEAM_ID int NOT NULL,\
                    PLAYER_ID int NOT NULL,\
                    START_POSITION char(50),\
                    COMMENT char(200),\
                    MIN char(50),\
                    FGM float,\
                    FGA float,\
                    FG_PCT float,\
                    FG3M float,\
                    FG3A float,\
                    FG3_PCT float,\
                    FTM float,\
                    FTA float,\
                    FT_PCT float,\
                    OREB float,\
                    DREB float,\
                    AST float,\
                    STL float,\
                    BLK float,\
                    TO_ float,\
                    PF float,\
                    PTS float,\
                    PLUS_MINUS float,\
                    PRIMARY KEY (ID)"

        c.execute(f'CREATE TABLE Game_details ({structure})')

    #if it exists just pass
    except:
        #print('Algo paso ')
        pass
    
#delete our db
def delete(mydb):
    c = mydb.cursor()
    c.execute('DROP DATABASE IF EXISTS NBA_DB ')

#show tables
def show_tables(mydb):
    c = mydb.cursor()
    c.execute('SHOW TABLES')
    print("Tables: ")
    for i in c:
        print(i)

def relations(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #cities relations
    c.execute('ALTER TABLE Cities ADD FOREIGN KEY (ARENA_ID) REFERENCES Arenas(ARENA_ID);')

    #teams relations
    c.execute('ALTER TABLE Teams ADD FOREIGN KEY (CITY_ID) REFERENCES Cities(CITY_ID);')

    #game details relations
    c.execute('ALTER TABLE Game_details ADD FOREIGN KEY (GAME_ID) REFERENCES Games(GAME_ID);')
    c.execute('ALTER TABLE Game_details ADD FOREIGN KEY (TEAM_ID) REFERENCES Teams(TEAM_ID);')
    c.execute('ALTER TABLE Game_details ADD FOREIGN KEY (PLAYER_ID) REFERENCES Players(PLAYER_ID);')

    #games relations
    c.execute('ALTER TABLE Games ADD FOREIGN KEY (SEASON_ID) REFERENCES Seasons(SEASON_ID);')
    c.execute('ALTER TABLE Games ADD FOREIGN KEY (HOME_TEAM_ID) REFERENCES Teams(TEAM_ID);')
    c.execute('ALTER TABLE Games ADD FOREIGN KEY (VISITOR_TEAM_ID) REFERENCES Teams(TEAM_ID);')

    #player at team
    c.execute('ALTER TABLE Players_at_team_in_season ADD FOREIGN KEY (PLAYER_ID) REFERENCES Players(PLAYER_ID);')
    c.execute('ALTER TABLE Players_at_team_in_season ADD FOREIGN KEY (TEAM_ID) REFERENCES Teams(TEAM_ID);')
    c.execute('ALTER TABLE Players_at_team_in_season ADD FOREIGN KEY (SEASON_ID) REFERENCES Seasons(SEASON_ID);')

def look_relation(mydb):
    c = mydb.cursor()
    c.execute('SELECT * FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS WHERE CONSTRAINT_SCHEMA="NBA_DB"')
    print("\nRelations:")
    for i in c:
        print(i)
