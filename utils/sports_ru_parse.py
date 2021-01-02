import requests
from bs4 import BeautifulSoup
from conf_data import PARSE_LINK

responce = requests.get(PARSE_LINK).text
soup = BeautifulSoup(responce, features='html.parser')

tables = soup.find_all('tbody')

# присылает ссылки на мачти
match = tables[0].find_all('tr')
# показывает вкладку "календарь", предстоящие матчи
def show_matches():
    match_time = []
    home_team =[]
    guest_team = []
    for items in match:
        info_match = items.find_all('td')
        #info_match[0].text # дата
        match_time.append(info_match[1].text) # время
        home_team.append(info_match[-3].text) # домашняя команда
        guest_team.append(info_match[-1].text) # гостевая команда
    return info_match[0].text, match_time, home_team, guest_team
    for items in match:
        link_match = items.find_all('a')
        for l in link_match:
            return "l.get('href')"
            