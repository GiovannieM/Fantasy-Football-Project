#########################################################################

# THIS PROGRAM IS FOR TESTING WEB SCRAPING FOR THE MASTER CODE

#########################################################################
from bs4 import BeautifulSoup
import pandas as pd
import re
import requests
import responses
import validators

# FFTODAY WEBSITE
################ BS4 ####################################################
print('Which Player would you like to get stats for? ')
last_name = input('Enter by Last Name: ')
print('------------------------------')
player_url = fr"https://www.fftoday.com/stats/players?Search={last_name}"
page = requests.get(player_url).text
soup = BeautifulSoup(page, "html.parser")
dfs = pd.read_html(player_url)
#########################################################################
new_url = player_url
response = requests.get(new_url)

#########################################################################
if response.history:
    print('------------------------------')
    print('Current yearly stats for '+last_name+' are:')
    dfs = pd.read_html(new_url)
    df = dfs[7]
    print(df)
    print()
    
else:
    player_names = []
    player_list = []
    index = 0
    links = soup.find_all("a", href=True)
    players = soup.find_all(class_="smallbody")
    print("--- Multiple Player(s) Found ---")
    print()
    for player in players:
        print(index, player.text)
        player_names.append(player.text)
        player_list.append(player.a.get('href'))
        index += 1
    print('------------------------------')
#########################################################################
    select_player = 0
    while True:
        try:
            select_player = int(input('Select specific player with corresponding number on list: '))
            if select_player > (len(player_names)):
                print ('Sorry that is out of range. Please Try again')
                continue
        except ValueError:
            print("Must be an integer!")
            continue
        else:
            print('Current yearly stats for '+player_names[select_player]+' are:')
            sp_url = fr"https://www.fftoday.com{player_list[select_player]}"
            dfs = pd.read_html(sp_url)
            print('------------------------------------------------------------')
            df = dfs[7]
            print(df)
            print('------------------------------------------------------------')
            break 
        
    
    #########################################################################
    # PRINTS THE PLAYER DATA INTO A CSV FILE
    # df.to_excel(r"C:\Users\Giovannie\Desktop\dataproject\statscrape.xlsx")
    # df.to_csv(r"C:\Users\Giovannie\Desktop\dataproject\tablescrape.csv")
    # print('Table Data has been written to an excel file')

    print('END')