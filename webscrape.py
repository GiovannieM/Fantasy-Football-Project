# THIS PROGRAM IS FOR TESTING WEB SCRAPING
#########################################################################
from bs4 import BeautifulSoup
import pandas as pd
import requests
#########################################################################
print('Which Player would you like to get stats for? ')
last_name = input('Enter by Last Name: ')
print('------------------------------')
player_url = fr"https://www.fftoday.com/stats/players?Search={last_name}"
page = requests.get(player_url).text
soup = BeautifulSoup(page, "html.parser")
dfs = pd.read_html(player_url)
new_url = player_url
response = requests.get(new_url)
#########################################################################
# CHECKS TO SEE IF MULTIPLE PLAYERS EXISTS WITH THE SAME LAST NAME
# IF NOT THE IT CONTINUES TO SPECIFC PLAYER YEARLY STATS
#########################################################################
if response.history:
    print('------------------------------')
    print('Current yearly stats for '+last_name+' are:')
    dfs = pd.read_html(new_url)
    df = dfs[7]
    print(df)
    print()
#########################################################################    
# IF MULTIPLE PLAYERS EXISTS, A LIST WILL GENERATE THE LIST OF PLAYERS
# WITH THE SAME NAME 
#########################################################################    
else:
    player_names = []           # LIST CREATED FOR USER TO SELECT FROM 
    player_list = []            # LIST OF PLAYERS TO BE PRINTED OUT 
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
# LETS USER SELECT FROM THE LIST OF GENERATED PLAYERS WITH THE SAME 
# LAST NAME AND LETS USER CHOOSE WHICH PLAYER THEY ARE LOOKING FOR 
#########################################################################
    select_player = 0
    while True:
        try:
            select_player = int(input('Select specific player with corresponding number on list: '))        # CHECK USER INPUT FOR A REAL NUMBER AND 
            if select_player > (len(player_names)):                                                         # NUMBER WITHIN LIST
                print ('Sorry that is out of range. Please Try again')
                continue
        except ValueError:
            print("Must be an integer!")
            continue
        else:
            print('Current yearly stats for '+player_names[select_player]+' are:')                      # PRINTS OUT SPECIFIC PLAYER CHOSEN FORM LIST 
            sp_url = fr"https://www.fftoday.com{player_list[select_player]}"                            # AND PRINTS OUT YEARS STATS FOR THAT PLAYER
            dfs = pd.read_html(sp_url)
            print('------------------------------------------------------------')
            df = dfs[7]
            print(df)
            print('------------------------------------------------------------')
            break 
#########################################################################
# SAVING PLAYER STATS CAN BE OMMTTED OR SKIPPED !!
#########################################################################
# SAVES THE PLAYER DATA INTO A EXCEL OR CSV FILE
# while True:
#     if input('Would you like to create a txt fo csv file? Enter y/n : ') != 'y':
#         break
#     else:
#         # PLEASE CHOOSE WHICH FILE TYPE YOU'D LIKE TO USE 
#         df.to_excel(fr"( ~ YOUR PATH HERE ~ )\{player_names[select_player]}.xlsx")
#         df.to_csv(fr"( ~ YOUR PATH HERE ~ )\{player_names[select_player]}.csv") 
#         break

#########################################################################
print('PLAYER STAT SCRAPING ENDED...')