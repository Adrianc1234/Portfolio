from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
import getpass
import pyautogui
from bs4 import BeautifulSoup
import networkx as nx 
from pyvis.network import Network
import matplotlib.pyplot as plt
import numpy as np

#ejecutar webscrapper
#os.system('./chromedirver')
#opciones de navegacion

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = '/Users/adriancarmona/Documents/Scrapper/chromedriver'

driver = webdriver.Chrome(driver_path, chrome_options = options)

#iniciamos la pantalla
driver.set_window_position(2000,0)
driver.maximize_window()
time.sleep(1)

#======================scroll section====================
def scroll_down():
    #for i in range(0,3):
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scroll_up():
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, -1 * document.body.scrollHeight);")

def scroll_more_contacts(scroll_down,scroll_top):
    response = 1
    while response == 1:
        try:
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.scaffold-finite-scroll__load-button'))).click()
        except:
            response = -1
            scroll_top()



#=========================================================


#log in
def log_in(username,password):

    #inicializamos el navegador
    driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')

    #añadimos usuario y contraseña
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#username'))).send_keys(username)
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#password'))).send_keys(password)

    #Enter
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
 
#display de contactos
def nav_contactos(scroll_more_contacts):

    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li-icon[type="nav-small-people-icon"]'))).click()
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,  'li-icon.mr4[type="people"]'))).click()
    time.sleep(5)
    scroll_more_contacts(scroll_down,scroll_up)

#lista de urls con nombres
def my_contacts():
    body = driver.execute_script("return document.body")
    source = body.get_attribute('innerHTML') 
    soup = BeautifulSoup(source, "html.parser")
    names = []
    data = []
    #count = 0
    for contact in soup.find_all("li", "mn-connection-card"):
        name = contact.find('span',class_='mn-connection-card__name').get_text().strip().replace('\n','')
        link= contact.find('a',attrs={"class" : "mn-connection-card__link"})
        link= 'https://www.linkedin.com' + link['href']
        if link == 'https://www.linkedin.com':
            continue
        else:
            data.append(link)
            names.append(name)
    return names,data

def friend_contacs(scroll_down):
    status = 1
    data = []
    while status == 1:
        time.sleep(2)
        scroll_down()
        body = driver.execute_script("return document.body")
        source = body.get_attribute('innerHTML') 
        soup = BeautifulSoup(source, "html.parser")
        for contact in soup.find_all("li", "reusable-search__result-container"):
            link = contact.find('span',attrs={"aria-hidden" : "true"}).get_text().strip().replace('\n','')
            if link == 'https://www.linkedin.com':
                continue
            else:
                data.append(link)
        try:
            WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.artdeco-pagination__button--next'))).click()
        except:
            status = -1
    else:
        return data

#visitar cada perfil
def open_and_extract(data,friend_contacs):
    data_contacts =[]
    #person = data
    for person in data:
        time.sleep(3)
        driver.get(person)
        body = driver.execute_script("return document.body")
        source = body.get_attribute('innerHTML') 
        soup = BeautifulSoup(source, "html.parser")
        name = soup.find('h1',class_='text-heading-xlarge').get_text().strip().replace('\n','')

        #hacemos click en busqueda de contactos
        try:
            time.sleep(3)
            WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.link-without-visited-state'))).click()
            names = friend_contacs(scroll_down)
            info = [name,names]
            data_contacts.append(info)
        except:
            info = [name,['']]
            data_contacts.append(info)
        print(f'{name} - Extracted successfully')
    return data_contacts

def corte_cantidad(my_contact_original,data_original):
    links = []
    cantidad = int(input('Contactos a scrappear: '))+1
    my_contact = np.random.choice(my_contact_original, cantidad, False)
    for item in my_contact:
        links.append(data_original[my_contact_original.index(item)])
    data = links
    return my_contact,data


#=========================== scrappeo =======================================
os.system('clear')
        
#loggeo
username = str(input('Username: '))
password = getpass.getpass('Password: ')
my_name = str(input('Name in LinkedIn: '))
log_in(username,password)

#Navegacion a tus contactos 
nav_contactos(scroll_more_contacts)

#extraccion de mis contactos

my_contact_original, data_original = my_contacts()
my_contact,data  = corte_cantidad(my_contact_original,data_original)

#solicitamos el usuario
print('Contactos Seleccionados: \n', my_contact)

#abrir contactos
friend_contacts = open_and_extract(data,friend_contacs)

#print('Info de mis constactos: \n', friend_contacts)


#=============================== grafo ======================================


def add_nodes(my_contact_original,friend_contacts,G):
    nodes = my_contact_original.copy()
    for friends in friend_contacts:
        nodes = nodes + friends[1]
    for node in nodes:
        G.add_node(node)
    G.add_node(my_name)
    return G

def add_edges(my_contact_original,my_name,my_contact,friend_contacts,G):
    
    #links a mis amigos
    for i in my_contact:
        #print(my_name,i)
        G.add_edge(my_name,i)
    
    #links amigo a sus amigos
    for n in friend_contacts:
        for nombre_amigo in n[1]:
            #print(n[0],link)
            G.add_edge(n[0],nombre_amigo)
            if nombre_amigo is my_contact_original:
                G.add_edge(my_name,nombre_amigo)
            else:
                continue

    return G

def visualizar(G):
    #nx.draw_kamada_kawai(G)
    nx.draw(G, pos = nx.spring_layout(G, scale=2), node_size=30, 
    node_color='lightblue', linewidths=0.25, font_size=10, 
    font_weight='light', with_labels=False) 
    plt.show()

np.save('my_contact.npy', my_contact)
np.save('my_contact_original.npy', my_contact_original)
np.save('friend_contacts.npy', friend_contacts)

G = nx.Graph() # crear un grafo
G = add_nodes(my_contact_original,friend_contacts,G = G)
G = add_edges(my_contact_original,my_name,my_contact,friend_contacts,G = G)

nx.write_gexf(G, "linkedin_graf.gexf")

#visualizar(G)




