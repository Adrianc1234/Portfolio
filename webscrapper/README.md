<h1><center>WEB SCRAPER FOR LINKEDIN</h1></center>

## What is LinkedIn? <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20" height="20">

LinkedIn is a platform that was born as a social network for professionals and companies. Its main objective is to connect people looking for work synergies and new professional or business opportunities.

It is currently owned by Microsoft and is considered the largest professional community worldwide. In fact, in Spain alone it already has more than 10 million users, since it was launched in 2003.

It is a network designed not so much to foster personal relationships, as Instagram, Facebook or Twitter are, but to create a network of contacts in the professional or work environment.

## What is a Web Scraper for LinkedIn? <img src="https://www.pngmart.com/files/4/Microsoft-Logo-PNG-Transparent-Image.png" width="40" height="30"> 

Web scraping is used in many digital companies that are dedicated to the collection of databases. To better clarify what web scraping is, you need to know what are the legitimate use cases of web scraping:

- Search engine robots crawl a site, analyze its content and then rank it.
- Price comparison sites that implement bots to automatically obtain prices and product descriptions for allied vendor websites.
- Market research companies that use it to extract data from forums and social networks.

To learn more about what web scraping is you should know that it is also used for illegal purposes. Including price scraping and stealing copyrighted content. An affected digital entity can suffer serious financial losses. Especially if it is a business that relies primarily on competitive pricing models or offers in content distribution.

The objective of Web Scraping in this social network is to get to know your contacts more closely and apply a deep analysis of social networks to understand your personal social network, as well as a sampling of your network in order to generate a visualization in the form of a graph.

## How to use it?

### Requirements Installation

  The first thing to do is to run a python script, which will install the necessary libraries to be able to run our new scripts. The first command we     must execute in our terminal is the following:
  
  `pip3 install -r requirements.txt` 

### Extraction Process
  
  - <strong>Step 1</strong>
  
  This command will allow us to start the extraction process automatically by simply executing the following command:
  
  `python3 extraction.py`
  
  - <strong>Step 2</strong>
  
  In this step we must add all our necessary information to be able to log in LinkedIn, as well as our user name in the social network, as it appears     there. It is important to mention that the password will not be displayed at any time, but it will be saved, so when you finish typing it press the     enter key after each added information.
  
  <img src="https://snipboard.io/diQqZ2.jpg" width="600" height="100"> 
  
  - <strong>Step 3</strong>
  
  Once we provide our login data, the scraper will access your account and will go to the contacts section, where it will extract all the list of your     contacts. Then the terminal will ask you for a number of contacts that you want to scrape, `note that this may affect the scraping time`.
  
  <img src="https://snipboard.io/NK7kMe.jpg" width="700" height="350"> 
  
  - <strong>Step 4</strong>
  
  The scraper will return the number of chosen contacts and their names, which are randomly selected from your original contact list. Once the list is     displayed, the screen will proceed to scrape and for each person scraped it will display a status `person's name - Extracted Successfully`.
  
  Once the extraction is finished it will show a message saying that the files have been generated perfectly, asking if we want to render or not the       graph with the files, in case we say `n`, the program will close. The opposite case will execute the rendering script, generating a `.html` file in     your folder, which can be opened with any browser.
  
  <img src="https://snipboard.io/bx5cDn.jpg" width="400" height="80"> 
  
  In case you answer `y`, you will get this screen:
  
  <img src="https://snipboard.io/b8zJkp.jpg" width="400" height="100"> 
  
  - <strong>Step 5</strong>
  
  Open this file with your navigator with right click and selecting `open with` and enjoy it.
  
  <img src="https://snipboard.io/SI5ABs.jpg" width="700" height="400"> 

## How does it work?

### Extraction

- #### Actions Sections
```python3
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
```
- `scroll_down()`: Is the one in charge of scrolling down the whole body of the page, it works with the active page.<br><br>
- `scroll_up()`: Is the one in charge of scrolling up the body of the page, reaching the title of the active page.<br><br>
- `scroll_more_contacts(scroll_down,scroll_top)`: This function combines the two previous ones so that when the scraper accesses your contacts, the list is expanded and then extracted.<br><br>

- #### Extraction functions

```python3
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

#looking for friend's friends
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

#visit each profile
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

#selecting an amount of random contacts
def corte_cantidad(my_contact_original,data_original):
    links = []
    cantidad = int(input('Contactos a scrappear: '))
    my_contact = np.random.choice(my_contact_original, cantidad, False)
    for item in my_contact:
        links.append(data_original[my_contact_original.index(item)])
    data = links
    return my_contact,data
```
- `log_in(username,password)`: This function is in charge of requesting the username and password of your account, without the password being displayed in the terminal, which then within the same function, will open the LinkedIn login and insert them. After that, click on the login button and you will be in your account.<br><br>
- `nav_contactos(scroll_more_contacts)`: This function takes as a parameter another function, which allows you to expand the whole list of your contacts and extract it. In addition to this, it is in charge of directing you from the home page to the page of your contacts.<br><br>
- `my_contacts()`: This function allows you to scroll down to expand the entire list of your contacts and then extract and return it in an array.<br><br>
- `friend_contacs(scroll_down)`: This function scrolls through the list of your friends' friends, and if you have multiple friends it clicks on the `next` button, returning an array with their information. <br><br>
- `open_and_extract(data,friend_contacs)`: This function takes as parameter the links and the names of the people in your friends list, to view them one by one, calling in its process the function `friend_contacs(scroll_down)`, so that for each visited friend, the function extracts its contacts. <br><br>
- `corte_cantidad(my_contact_original,data_original)`: This function is nothing more than a function to shorten the search, since LinkedIn can block us if we exceed the number of profiles visited.<br><br>

### Creation of our network & files. 
 - #### Making our network and saving information
 ```python3
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


np.save('my_contact.npy', my_contact)
np.save('my_contact_original.npy', my_contact_original)
np.save('friend_contacts.npy', friend_contacts)

G = nx.Graph() # crear un grafo
G = add_nodes(my_contact_original,friend_contacts,G = G)
G = add_edges(my_contact_original,my_name,my_contact,friend_contacts,G = G)

nx.write_gexf(G, "linkedin_graf.gexf")
```
 
- ### Visualization

