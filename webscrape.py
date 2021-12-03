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
# url = "https://www.fftoday.com/stats/players/1812/Tom_Brady"
# player_url = "https://www.fftoday.com/stats/players"
################ BS4 ####################################################
print('Which Player would you like to get stats for? ')
last_name = input('Enter by Last Name: ')
print('------------------------------')
player_url = fr"https://www.fftoday.com/stats/players?Search={last_name}"
page = requests.get(player_url).text
soup = BeautifulSoup(page, "html.parser")
# page_text = soup.find_all(class_="smallbody")
dfs = pd.read_html(player_url)
#########################################################################
# check_url = fr"https://www.fftoday.com/stats/players/*/*{last_name}"

# responses = requests.get(player_url)
# for response in responses.history:
#     print(response.url)

new_url = player_url

response = requests.get(new_url)
if response.history:
    print('------------------------------')
    print('Current stats for '+last_name+' are:')
    dfs = pd.read_html(new_url)
    df = dfs[7]
    print(df)
    print()
else:
    player_list = []
    index = 1
    links = soup.find_all("a", href=True)
    players = soup.find_all(class_="smallbody")
    print("---Multiple Player(s) Found---")
    for player in players:
        print(index, player.text)
        # player_list.append(link)
        index += 1
    print('------------------------------')
#########################################################################
# valid=validators.url(fr"https://www.fftoday.com/stats/players?Search={last_name}")

# if valid==False:
#     print('Current stats for '+last_name+' are:')
#     dfs = pd.read_html(player_url)
#     df = dfs[7]
#     print(df)
# else:
#     player_list = []
#     index = 1
#     links = soup.find_all("a", href=True)
#     players = soup.find_all(class_="smallbody")
#     for player in players:
#         print(index, player.text)
#         # player_list.append(link)
#         index += 1

#########################################################################
# player_list = []
# index = 1
# links = soup.find_all("a", href=True)
# players = soup.find_all(class_="smallbody")
# for player in players:
#     print(index, player.text)
#     # player_list.append(link)
#     index += 1

# print()
# print(player_list)

############ PANDAS #####################################################
#GRAB TABLE FOR PLAYER CAREER STATS
# print('Current stats for '+last_name+' are:')
# dfs = pd.read_html(player_url)
# df = dfs[7]
# print(df)
#########################################################################
# PRINTS THE PLAYER DATA INTO A CSV FILE
# df.to_excel(r"C:\Users\Giovannie\Desktop\dataproject\statscrape.xlsx")
# df.to_csv(r"C:\Users\Giovannie\Desktop\dataproject\tablescrape.csv")
# print('Table Data has been written to an excel file')

print('END')