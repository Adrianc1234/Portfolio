#by Adrian Carmona and Isaac Chavez

#INEGI. Sistema de Cuentas Nacionales de México. Acervos de Capital por Entidad Federativa. Base 2013.
#Sector privado/ Tabla resultados totales privado

#import
import numpy as np
import pandas as pd
from numpy import median
from statistics import mean
from geopy.geocoders import Nominatim
import webbrowser
import folium
import branca

#declaramos la clase arbol
class Arbol(object):
    def __init__(self):
        #definimos atributos
        self.der = None  
        self.izq  = None    
        self.dato  = None 

#leemos el dataset
def leer():
    hojas = []
    df = pd.read_csv("/home/adrian/Documentos/db.csv", sep = ',')
    return df

#diseñamos nuestro arbol

def arbol(df):
    df = df
    promedio_tr = mean(df['Viviendas'] + df['Unidades de transporte'])
    promedio_ex = mean(df['Inmuebles']+ df['Maquinaria'])
    promedio_ef = mean(df['Equipo de computo'] + df['Equipo de oficina'])

    #sacamos nuestra banderas para hacer clasificacion
    bandera_1 = 0
    print(f'El valor de la bandera 1: {bandera_1}')
    print(f'La etiqueta sera: Eficiencia')
    bandera_2 = promedio_ef
    print(f'El valor de la bandera 2: {bandera_2}')
    print(f'La etiqueta sera: Trabajador')
    bandera_3 = promedio_tr
    print(f'El valor de la bandera 3: {bandera_3}')
    print(f'La etiqueta sera: Expansion')
    bandera_4 = mean(df['Total'])
    print(f'El valor de la bandera 4: {bandera_4}')
    print('1|----2|----3|----|4')
    #creamos el arbol
    raiz = Arbol() 

    #definimos dato de raiz
    raiz.dato = bandera_3

    #definimos dato de la izquierda (primer nivel)
    raiz.izq = Arbol()
    #etiqueta de trabajador
    raiz.izq.dato = 'Trabajador'

    #definimos dato de la derecha (primer nivel)
    raiz.der = Arbol()
    raiz.der.dato = bandera_2

    #definimos dato de la izquiera (segundo nivel)
    raiz.der.izq = Arbol()
    raiz.der.izq.dato = 'Eficiencia'

    #definimos dato de la derecha (segundo nivel)
    raiz.der.der = Arbol()
    raiz.der.der.dato = 'Expansion'
    
    #Hacemos la decicion
    def etiquetar():
        etiquetas = []
        
        #recorremos el dataframe
        for i in range(0,len(df)):
            lista = []
            lista.append((df.iloc[i,2] + df.iloc[i,4])/2)
            lista.append((df.iloc[i,1] + df.iloc[i,3])/2)
            lista.append((df.iloc[i,5] + df.iloc[i,6])/2)
            valor_t = max(lista)
            
            #tomamos deciciones
            if valor_t >= raiz.dato:
                etiquetas.append(str(raiz.izq.dato))
            else:
                if valor_t <= raiz.der.dato:
                    etiquetas.append(raiz.der.izq.dato)
                else:
                    etiquetas.append(raiz.der.der.dato)
        df['Area interes']  = etiquetas
        return df
    #llamamos a la funcion de etiquetas
    df = etiquetar()    
    return df

#funcion para mapear a tiempo rear
def mapear(df):
    #con los datos de 'concepto' usamos esa direccion para hacer request de coordenadas
    geolocator = Nominatim(user_agent="Karatsi")
    print('Iniciando proceso de ubicacion...')
    estados = df['Concepto']
    coordenadas=[]

    #localizamos cada direccion
    for n in estados:
        location = geolocator.geocode(n)
        dire = [location.latitude, location.longitude]
        coordenadas.append(dire)
    #añadimos una columna con las direcciones
    df['Coordenadas'] = coordenadas
    print('Proceso terminado...')
    print('Los datos de ubicacion se añadieron correctamente')
    return df

#generamos el mapa en folium
def visualizar(df):
    #ubicamos en mexico
    mi_mapa = folium.Map(location=( 19.4978, -99.1269), zoom_start=5.3)

    #se recorre la data, por cada valor se ubica y de a su etiqueta se le da un color
    for i in range(0,len(df)):
        coor = df.iloc[i,9]
        etiqueta = df.iloc[i,8]
        datos = df.iloc[i,0:8]
        if etiqueta == "Trabajador":
            por = ((datos[2] + datos[4])*100)/datos[7]
            texto = f'El {por}% de los ingresos son para el sector de {etiqueta}'
            html = f'<p>Estado:{datos[0]}</p><p>Inmuebles:{datos[1]}</p><p>viviendas:{datos[2]}</p><p>Maquinaria:{datos[3]}</p><p>Unidades de transporte:{datos[4]}</p><p>Equipo de computo:{datos[5]}</p><p>Equipo de oficina:{datos[6]}</p><p>{texto}</p>'
            iframe = branca.element.IFrame(html=html, width=300, height=200)
            marcador = folium.Marker(
                location=(coor[0], coor[1]),
                popup=folium.Popup(iframe, max_width=500),
                icon=folium.Icon(color="orange",icon = 'cloud')
            )
            marcador.add_to(mi_mapa)
        elif etiqueta == "Expansion":
            por = ((datos[1] + datos[3])*100)/datos[7]
            texto = f'El {por}% de los ingresos son para el sector de {etiqueta}'
            html = f'<p>Estado:{datos[0]}</p><p>Inmuebles:{datos[1]}</p><p>viviendas:{datos[2]}</p><p>Maquinaria:{datos[3]}</p><p>Unidades de transporte:{datos[4]}</p><p>Equipo de computo:{datos[5]}</p><p>Equipo de oficina:{datos[6]}</p><p>{texto}</p>'
            iframe = branca.element.IFrame(html=html, width=300, height=200)
            marcador = folium.Marker(
                location=(coor[0], coor[1]),
                popup=folium.Popup(iframe, max_width=500),
                icon=folium.Icon(color="blue",icon = 'cloud')
            )
            marcador.add_to(mi_mapa)
        elif etiqueta == "Eficiencia":
            por = ((datos[5] + datos[6])*100)/datos[7]
            texto = f'El {por}% de los ingresos son para el sector de {etiqueta}'
            html = f'<p>Estado:{datos[0]}</p><p>Inmuebles:{datos[1]}</p><p>viviendas:{datos[2]}</p><p>Maquinaria:{datos[3]}</p><p>Unidades de transporte:{datos[4]}</p><p>Equipo de computo:{datos[5]}</p><p>Equipo de oficina:{datos[6]}</p><p>{texto}</p>'
            iframe = branca.element.IFrame(html=html, width=300, height=200)
            marcador = folium.Marker(
                location=(coor[0], coor[1]),
                popup=folium.Popup(iframe, max_width=500),
                icon=folium.Icon(color="lightgreen",icon = 'cloud')
            )
            marcador.add_to(mi_mapa)
    #guardamos el mapa
    mi_mapa.save("mapa.html")

    #Abrimos el mapa
    webbrowser.open('/home/adrian/Documentos/mapa.html')

#corremos todo
df = leer()
df = arbol(df)
df = mapear(df)
visualizar(df)
