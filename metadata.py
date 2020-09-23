import requests
from bs4 import BeautifulSoup as bs

all_games = []

def get_url():
    url  = "https://store.playstation.com/en-us/grid/STORE-MSF77008-PS4ALLGAMESCATEG/"
    response = requests.get(url)
    # print(response.text)
    
    return response


def get_soup():
    response = get_url() # call  the get_url function
    
    soup = bs(response.content, "html.parser") #parse page source to bs4
    
    title = soup.title.string # for the page title
    
    game_class = "grid-cell grid-cell--game" # class for the game cards
    
    games = soup.find_all("div", {"class":game_class})
    
    for game in games:
        # prices = []
        # name = game.find("div", {"class":"grid-cell__title"})
        # name = name.text.replace("\n","")
        # print(name)
    
        # price = game.find("div", {"class":"grid-cell__footer"})
        # price = price.text.replace("\n","")
        # print(price)
        # print("\n")
        
        link = game.find("a", href= True)
        link = link['href']
        
        game_link = "http://store.playstation.com" + str(link)
        
        all_games.append(game_link)
        
        # print(game_link)
                  
get_soup()

def get_link():
    for link in all_games:
        repeat = requests.get(link)
          
        call = bs(repeat.content, "html.parser")
    
        head = call.title.string
        # print(head)

        game1_class = "pdp padding-medium"
        
        game1 = call.find("div", {"class":game1_class})
                  
        name = game1.find("h2", {"class":"pdp__title"})
        print(name.text)
        print("")
                
        description = game1.find("div", {"class":"pdp__description"})
        print(description.text)
        print("")
        
        release_date = game1.find("span", {"class":"provider-info__list-item"}).text
        print(release_date)
                
        price = game1.find("h3", {"class":"price-display__price"}).text
        print(price)
                
        genre = game1.find("li", {"class":"tech-specs__menu-items"}).text
        print(genre)
        print("")   
                    
get_link()
