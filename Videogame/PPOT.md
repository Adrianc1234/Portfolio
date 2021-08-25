# PPOT
## TEAM
- Adrian Carmona
- Saulo acevedo

This game was made to learn more about object oriented programming by @pedrojimenezp
Class that has the atributes and methods of one player, in this case it has the names and the points.
````Python
class Jugador():
    
    #cada atributo que inicie por dos guiones bajos (__) es un atributo privado de la clase...
    #lo mismo se aplica para los metodos
    
    # metodo contructor que recibe dos parametros el nombre y los puntos del jugador... 
    def __init__(self, n="",p=0):
        # __nombre y __puntos son atributos privados de la clase Jugador
        self.__nombre=n
        self.__puntos=p

    def set_nombre(self,n):
        self.__nombre = n

    def get_nombre(self):
        return self.__nombre

    def set_puntos(self, p):
        self.__puntos = p

    def get_puntos(self):
        return self.__puntos
````
This is the class that has the atributes and methods of the game for each object.
````Python
class Game():
    def __init__(self):
        #atributo que guarda las posibilidade del juego entre dos jugadores
        self.__posibilidades = {
            "piedra":{
                "piedra":0,
                "papel":-1,
                "tijera":1
            },
            "papel":{
                "papel":0,
                "tijera":-1,
                "piedra":1
            },
            "tijera":{
                "tijera":0,
                "piedra":-1,
                "papel":1
            }
        }
        #atributo para ir registrando cada enfrentamiento entre los dos jugadores
        self.__registro = []
        #atributos que guardan las elecciones de cada jugador
        self.__eleccion1 = ""
        self.__eleccion2 = ""

    def set_eleccion1(self,e1):
        self.__eleccion1 = e1

    def set_eleccion2(self,e2):
        self.__eleccion2 = e2

    def get_eleccion1(self):
        return self.__eleccion1

    def get_eleccion2(self):
        return self.__eleccion2

    def registrar(self):
        self.__registro.append({"jugador1":self.__eleccion1,"jugador2":self.__eleccion2})

    def get_registro(self):
        return self.__registro

    def eleccion_ganadora(self):
        if self.__eleccion1 != "" and self.__eleccion2 != "":
            resultado = self.__posibilidades[self.__eleccion1][self.__eleccion2]
            if resultado == 0:
                return "Empate"
            elif resultado == -1:
                return "Jugador2"
            elif resultado == 1:
                return "Jugador1
````
we made a varible to be of easy acess for the program and so dont change any variable by the other hand we save the names in the variables for the class and so we can call them in easier mode.
````Python
nombre_jugador1 = input("Ingrese el nombre del primer jugador:\n ")
j1=nombre_jugador1
nombre_jugador2 = input("Ingrese el nombre del segundo jugador:\n ")
j2=nombre_jugador2

jugador1 = Jugador(nombre_jugador1)
jugador2 = Jugador(nombre_jugador2)

print("\n START THE GAME !!! \n")
print("Estos son los jugadores")
print(jugador1.get_nombre())
print(jugador2.get_nombre())
print("\n")
````
we start the game with this function:
````Python
juego = Game()
````

for the end we make a while to see if some user wishes give up or both wish continue and if it is right the program continues with the game and if some player left, the program gives a register about matches.
````Python
while True:
    print(j1," Es tu turno")
    eleccion1 = input("Ingrese(piedra,papel,tijera) escriba 'me rindo' para retirarse: ")
    if eleccion1 == "me rindo":
        print(jugador1.get_nombre()," se retiro de la partida !!!")
        break
    print(j2, "Es tu turno")
    eleccion2 = input("Ingrese(piedra,papel,tijera)escriba 'me rindo' para retirarse: ")
    if eleccion2 == "me rindo":
        print(jugador2.get_names()," se retiro de la partida !!!")
        break

    juego.set_eleccion1(eleccion1)
    juego.set_eleccion2(eleccion2)

    juego.registrar()
    resultado = juego.eleccion_ganadora()

    if resultado == "Empate":
        print(juego.get_eleccion1(), " = ", juego.get_eleccion2())
        print("Esto es un empate! \n")
    elif resultado == "Jugador2":
        print(juego.get_eleccion1(), " ha perdido vs ", juego.get_eleccion2())
        print(jugador2.get_nombre(),"gana! \n")
        jugador2.set_puntos(jugador2.get_puntos()+1)
    elif resultado == "Jugador1":
        print(juego.get_eleccion1(), " Gana a ", juego.get_eleccion2())
        print(jugador1.get_nombre(),"gana! \n")
        jugador1.set_puntos(jugador1.get_puntos()+1)     

    print("El marcador es:\n")
    print(jugador1.get_nombre(),"     VS    ", jugador2.get_nombre())
    print(jugador1.get_puntos(), "<------->", jugador2.get_puntos(),"\n")

print("REGISTRO DEL JUEGO")
print(jugador1.get_nombre(), "     VS    ", jugador2.get_nombre())
for r in juego.get_registro():
    print(r["jugador1"], "     VS    ", r["jugador2"])

print("\n")

if jugador1.get_puntos() > jugador2.get_puntos():
    print("Ganador del juego:", jugador1.get_nombre())
elif jugador2.get_puntos() > jugador1.get_puntos():
    print("Ganador del juego:", jugador2.get_nombre())
elif jugador1.get_puntos() == jugador2.get_puntos():
    print("Esto ha sido un empate.")

print("\n")
````
