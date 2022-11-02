#pip3 install mysql-connector-python
import mysql.connector
import modules as md
import cleanning as cl
import insertion as ins
import os
"""
# IMPORTANT TO RUN IN YOUR MYSQL CONSOLE
#pip3 install mysql-connector-python
mysql> CREATE USER 'nuevo_usuario'@'localhost' IDENTIFIED BY 'contraseña';
mysql> GRANT ALL PRIVILEGES ON * . * TO 'nuevo_usuario'@'localhost';
mysql> FLUSH PRIVILEGES;

# The user and password will be used for the future connection.
ref: https://www.hostinger.mx/tutoriales/como-crear-usuario-mysql
"""
try:
    os.system('mkdir data_cleanned')
except:
    pass

#DATA CLEANNING
cl.games_details_cleanning()

cl.games()

cl.teams()

cl.season()

cl.players_at_team()

cl.players()

cl.arenas()

cl.cities()


#DATA INFRASTRUCTURE
mydb = md.login()

#create our db
try:
    md.delete(mydb)
    md.create_db(mydb)
except:
    pass

#verify if it exists
md.show_db(mydb)

#Arenas table
md.Arenas_T(mydb)

#Cities table
md.Cities_T(mydb)

#Teams table
md.Teams_T(mydb)

#Games Table
md.game_t(mydb)

#seasons Table
md.Seasons_T(mydb)

#players Table
md.Players_T(mydb)

#players at team in season
md.player_at_the_season(mydb)

#game Datails
md.Game_details_T(mydb)

#show tables
md.show_tables(mydb)

#relations
md.relations(mydb)

#looks relations
md.look_relation(mydb)

#data insertion
ins.insertion()

