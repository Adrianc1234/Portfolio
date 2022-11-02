#Import libraries
from zlib import DEF_BUF_SIZE
import mysql.connector
import pandas as pd
import numpy as np

#games_details
def games_details_cleanning():
    gd = pd.read_csv('data/games_details.csv')
    game_details = gd.drop(['TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_NAME', 'REB'], axis = 1)
    game_details['ID'] = np.arange(len(game_details))
    game_details = game_details.set_index('ID')
    game_details = game_details.fillna(0)
    game_details.to_csv('data_cleanned/game_details_db.csv')

def games():
    games = pd.read_csv('data/games.csv')
    years = games.SEASON.unique()
    years.sort()
    season = pd.DataFrame()
    season['Year'] = years
    games = games.drop(['GAME_DATE_EST', 'TEAM_ID_home', 'TEAM_ID_away'], axis = 1)
    
    for i, val in enumerate(season.values):
        games.loc[games['SEASON'] == val[0], 'SEASON'] = i
    
    games = games.set_index('GAME_ID')
    games = games.reindex(columns = ['GAME_STATUS_TEXT', 'SEASON', 'HOME_TEAM_ID', 'PTS_home', 'FG_PCT_home', 'FT_PCT_home', 'FG3_PCT_home', 'AST_home', 'REB_home', 'VISITOR_TEAM_ID', 'PTS_away', 'FG_PCT_away', 'FT_PCT_away', 'FG3_PCT_away', 'AST_away', 'REB_away', 'HOME_TEAM_WINS'])
    games = games.fillna(0)
    games.to_csv('data_cleanned/games_db.csv')


def teams():
    teams = pd.read_csv('data/teams.csv')
    teams = teams.drop(['ARENA', 'ARENACAPACITY'], axis = 1)
    teams = teams.set_index('TEAM_ID')
    teams = teams.rename(columns = {'CITY':'TEAM_NAME'})
    teams['CITY_ID'] = [0, 1, 2, 3, 4, 5, 6, 8, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29] 
    teams = teams.reindex(columns=['TEAM_NAME','ABBREVIATION','NICKNAME','YEARFOUNDED','MIN_YEAR', 'MAX_YEAR', 'CITY_ID', 'OWNER','GENERALMANAGER','HEADCOACH','LEAGUE_ID','DLEAGUEAFFILIATION'])
    teams.to_csv('data_cleanned/teams_db.csv')

def season():
    games = pd.read_csv('data/games.csv')
    years = games.SEASON.unique()
    years.sort()
    season = pd.DataFrame()
    season['Year'] = years
    season['Season_Id'] = np.arange(0, 18)
    season = season.reindex(columns = ['Season_Id', 'Year'])
    season = season.reindex()
    season.to_csv('data_cleanned/season.csv', index = False)

def players_at_team():
    games = pd.read_csv('data/games.csv')
    years = games.SEASON.unique()
    years.sort()
    season = pd.DataFrame()
    season['Year'] = years
    players_d = pd.read_csv('data/players.csv')
    joined = players_d[players_d['SEASON'] == 2019].copy()
    
    for i, val in enumerate(season.values):
        players_d.loc[players_d['SEASON'] == val[0], 'SEASON'] = i
    
    players_at_team_in_season = players_d.rename(columns = {'SEASON':'SEASON_ID'})
    players_at_team_in_season['ID'] = np.arange(len(players_at_team_in_season))
    players_at_team_in_season = players_at_team_in_season.reindex()
    column = list(players_at_team_in_season.columns)
    column[0], column[1], column[2], column[3], column[4] = column[4], column[0], column[1], column[2], column[3]
    players_at_team_in_season = players_at_team_in_season[column]
    players_at_team_in_season.to_csv('data_cleanned/players_at_team_in_season.csv', index = False)
    
def players():
    players = pd.read_csv('data/players.csv')
    players.to_csv('data_cleanned/players_db.csv')


def arenas():
    arenas = pd.DataFrame()
    teams = pd.read_csv('data/teams.csv')
    arenas['ARENA_NAME'] =  teams['ARENA']
    arenas['ARENACAPACITY'] = teams['ARENACAPACITY'].fillna(0)
    arenas['ARENA_ID'] = np.arange(len(arenas))
    arenas = arenas.reindex()
    arenas.to_csv('data_cleanned/arenas.csv')

def cities():
    teams = pd.read_csv('data/teams.csv')
    arenas = pd.read_csv('data_cleanned/arenas.csv')
    cities = pd.DataFrame()
    cities['CITY'] = teams['CITY']
    cities['ARENA_ID'] = arenas['ARENA_ID']
    for i, val in enumerate(cities.values):
        cities.loc[cities['CITY'] == val[0], 'CITY_ID'] = i
    cities['CITY_ID'] = cities['CITY_ID'].astype('int64')
    cities = cities.reindex()
    cities1 = cities.set_index('CITY_ID')
    cities1.to_csv('data_cleanned/cities.csv')

