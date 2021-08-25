# DATA ANALYSIS USING PYTHON AND ELASTICSEARCH
## Team work
- 1- Saulo acevedo: Encargado de la visualizacion de los histogramas y analisis de los mismos............tiempo estimado 3 dias (Ayudo tambien en el codigo)
- 2- Adrian Carmona: Encargado de inspeccion del indexado y desarrollo del codigo para la visualizacion del mapa............tiempo estimado 3 dias (Aplico autimatizacion) 
- 3- Isaac Chavez: Encargado de inspeccion del indexado y desarrollo del codigo para la visualizacion del mapa..............tiempo estimado 3 dias
- 4- Auria Dzul: Encargada de obtencion, chequeo y limpieza de datos para el indexado..........tiempo estimado 3 dias
- 5- Ulises pat: Encargado de obtencion, chequeo y limpieza de datos para el indexado..........tiempo estimado 3 dias

## Introduction
This project was based in analize one data set in a faster way using elasticsearch to index all data. Why elasticsearch? **Elasticsearch** is a distributed, open source analytics and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. And the data set that we used was about taxis trips, then we needed to make graphs using geopoints by that reasons we must put it in applying indexation with Elasticsearch.

In the other hand, for the visualization, we made a heatmap to show the most frecuent places to pickup people and the same with dropoff. These maps can be filter in months or anual mode, but also we made an data visualization using **Tableau**

![Elasticsearch](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/Intro.png?raw=true)

![Myservice](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/elastic.png?raw=true)

## Pipline
### Steps for normal pipline:
![Steps](https://escueladedatos.online/wp-content/uploads/2019/09/pipeline.png)

### Our pipline for the project
![pipline](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/pipline.png?raw=true)

[Simple pipline](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/pipeline.pdf)


**Define**

Data-driven projects should start by defining the problem they want to solve and their actions. It is at this stage that you ask questions and come up with the purposes of your project. In our case the question was: Where and in which month of the year the requests for taxis are more frequent? With this we solve a problem for many companies of taxi services, since many times they do not know how to create their travel plans and also do not know where to offer the services. By doing this analysis we obtain frequent places of applications and also destinations, so the company can know where to establish and also where to establish defined destinations.

As a second point you will also know in which month the trips are longer and with that same give warning about the gasoline expenses in those months, in the same way that month taxis are more requested.

![Define](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/definir.png?raw=true)

**Searching**

While the definition phase of the problem suggests which data you will need, searching for this data is another step, with much or little difficulty, depending on the problem. There are many tools and techniques to do that: from a simple question on your social media, to using tools like a search engine, open data portals or a request for access to information asking for data that is available in that government institution. In our case as we were going to do a data analysis on where the request for taxis is more frequent, we decided to look for a [dataset](https://www.kaggle.com/mnavas/taxi-routes-for-mexico-city-and-quito?select=mex_clean.csv) that can give us geopoints and times as well as frequencies, for that we use **Kaggle**.

![Searching](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/searching.png?raw=true)

**Collecting**

Producing data can be a short and easy task, or a long and complex one. The important thing is to design a replicable method and choose the most appropriate way for the project, since its scope and conclusions will depend on that choice. In our case the collection of data is done from a previously downloaded dataset, since records are already kept and in addition the mestro asked us that the user or the person who wants to do the same analysis can replicate it and this can happen, simply changing the data for others as long as they respect the names of the columns, the formats and the name of the .csv. That is to say that anyone can edit the csv and add more data and the program will continue to do the analysis with each year that is added.

![Collecting](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/collection.png?raw=true)

````Python3
import webbrowser
import pandas as pd
import numpy as np 
import folium
from elasticsearch import Elasticsearch
import time
from elasticsearch import helpers
import datetime
import os

#RECOLECCION DE DATOS
print('cargando datos...')
df = pd.read_csv("mex_clean.csv",parse_dates=["pickup_datetime","dropoff_datetime"], infer_datetime_format=True)
print('Datos cargados...')
````

**Verify**

Getting the data does not mean that the problem is solved. It is necessary to verify whether your information is valid, as well as to review the metadata and methodology with which this set of information was collected. In our case, during the verification we realized that the travel time data were unbalanced or as in the data science we say **outliers**, because for more than seconds it was, if we passed them to minutes they became more than 10,000 hours, since we identified that the cause was that the taxi drivers forgot to turn off the GPS and this continued measuring the time, so once identified and checked that the other columns were fine and that they were not going to serve us for analysis, we went to do the data cleaning.

![Verify 1](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/Verify%201.png?raw=true)

![Verify 2](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/Verify%202.png?raw=true)

**Cleanning**

It is very common for data to be obtained and validated to be in disarray and to have formatting problems: duplicate rows, column names that do not match the records, values that contain rare characters or that prevent computer processing, and others. As in our cases, the formats of dates and times in which taxi drivers were required were in the same column, which we could not leave them alone, since we needed to analyze it separately, date and time, by the issue of filters. What we did was separate into two new columns called, pickup_time and pickup_date the data, the same for the dropoff, in addition we did a cleaning of outliers, since we noticed that there were only 5 drivers that arrived at the million in the part of journey duration, so a filter was applied to the columns and rows that had a time greater than 9999 seconds were removed. Then we created a new . csv that was already clean.

````Python3
#LIMPIEZA DE DATOS
#eliminamos columnas no necesarias
viajes = df.drop(['vendor_id', 'store_and_fwd_flag'], axis = "columns")
columnas = list(viajes)
nulos = []

#checamos columnas sus valores nulos
for columna in columnas:
    cantidad = viajes[columna].isnull().sum()
    nulos.append(cantidad)
    
#verificamos el array de valores 
for i in nulos:
    if i !=0:#si alguno es diferente a 0 osea que si tiene nulos
        for columna in columnas:
            #recorremos columnas y los eliminamos
            viajes = viajes.drop(viajes[viajes[columna].isnull()].index, inplace = True)
    #sino hacemos un continue
    else:
        continue

#separar fecha y hora
viajes["pickup_date"] = viajes.pickup_datetime.dt.date
viajes["pickup_time"] = viajes.pickup_datetime.dt.time
viajes["dropoff_date"] = viajes.dropoff_datetime.dt.date
viajes["dropoff_time"] = viajes.dropoff_datetime.dt.time
viajes['trip_duration'] = viajes['trip_duration'] / 60 # convertimos de sec a minutos
viajes = viajes.drop(['wait_sec'], axis = 'columns')
viajes = viajes.drop(['pickup_datetime'], axis = 'columns')
viajes = viajes.drop(['dropoff_datetime'], axis = 'columns')
viajes['trip_duration'] = viajes['trip_duration'].astype(int) 
viajes.drop(viajes[viajes['trip_duration']>9999].index, inplace = True)
viajes.to_csv (r'viajes_limpios.csv', index = False, header=True)
data = pd.read_csv("viajes_limpios.csv",
                  parse_dates=["pickup_date","pickup_time","dropoff_time","dropoff_date"], infer_datetime_format=True)
print('Limpieza de datos finalizada...')
print('Datos listos para indexar...') 
````

**Uploading data in elasticsearch**

````Python3
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()
es.indices.delete(index="viajes")
es.indices.create(index = "viajes")


#creamos los contenedores
actions = [
  {
    "_index": "viajes",
    "_type": "doc",
    "_source": {
        'id':'int', 'pickup_longitude':'float', 'pickup_latitude':'float', 'dropoff_longitude':'float',
           'dropoff_latitude':'float', 'trip_duration':'int', 'dist_meters':'int', 'pickup_date':'datetime',
           'pickup_time':'datetime', 'dropoff_date':'datetime', 'dropoff_time':'datetime'
    }
  }
  for i in range(0,len(data))
]

st = time.time()
helpers.bulk(es, actions)
end = time.time()
print("total time", end-st)

print('indice creado...esperando insersion')
#Insertando datos
print('Empezando insersion...')
st = time.time()
for index, row in data.iterrows(): 
    doc= {'id':row['id'], 'pickup_longitude':row['pickup_longitude'], 'pickup_latitude':row['pickup_latitude'], 'dropoff_longitude':row['dropoff_longitude'],
        'dropoff_latitude':row['dropoff_latitude'], 'trip_duration':row['trip_duration'], 'dist_meters':row['dist_meters'], 'pickup_date':row['pickup_date'],
        'pickup_time':row['pickup_time'], 'dropoff_date':row['dropoff_date'], 'dropoff_time':row['dropoff_time']}
    es.index(index="viajes", doc_type="doc", id=row['id'], body=doc)
    print(f'documento #{index}.....listo')
end = time.time()
print ("total time", end-st)
os.system("clear && exit")
````
![carga](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/programa1.png?raw=true)

**Analyze**

This is the part where we get knowledge about the problem that we defined at the beginning. By putting our statistical and mathematical skills into practice, we can interview a data set like any journalist interviews their sources. In our case, our first analysis was to see on a map the most frequent places so we needed to take out the places that were repeated, how to do that if we only have locations? We had to count the number of times the dots were repeated and put them in a dataframe. The second analysis was to take out the average time it took to travel per month. The third was to take out the average mileage per month. These analyses will give the company an idea of the months in which they must invest more in the maintenance of taxis without being affected, as well as opportunities for improvements, all this measuring data per month.

![Programa2](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/programa2.png?raw=true)

![Programa3](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/programa3.png?raw=true)

![Programa4](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/programa4.png?raw=true)

![Programa5](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/programa5.png?raw=true)

**Visualization**

It is necessary to present the data: talk to your audience so that they know the questions you were looking to answer and the means that has allowed you to reach certain conclusions or start a conversation. In our case we mentioned that we made an interactive map of heat with which the user can investigate all areas of Mexico, exploring the frequency of trips with the intensity of color, in addition we made graphics that were shown below.

![mapa](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/mapa.png?raw=true)

![mapa2](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/mapa2.png?raw=true)

![grafica1](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/Graficas%201.png?raw=true)

![grafica2](https://github.com/Adrianc1234/paradigms-programming/blob/master/Big%20Data/Pictures/Graficas%202.png?raw=true)

# How can i run it? 
- 1- Download the files [here](https://upy-my.sharepoint.com/:u:/g/personal/st1809032_upy_edu_mx/ETkECiTwvwtKinBqVVcWi5QBj_MTP_lAV1SCstfuCsb9pg?e=IIEHJG), (it is a zip, dont move nothing, just follow the instructions)
- 2- unzip the file
- 3- run the first file called elasticsearch.sh with the command **./elasticsearch.sh** (in linux or ubuntu, dont forget put allow like a program)
- 4- open a new tap in the terminal and run the second script with **./programa.sh**(The same note like above)
- 5- waith that the script upload the files and then it will start.
