import requests
from bs4 import BeautifulSoup

link = 'https://www.sports.ru/football/match/italy/'

responce = requests.get(link).text
soup = BeautifulSoup(responce, features='html.parser')

tables = soup.find_all('tbody')

# присылает ссылки на мачти
match = tables[0].find_all('tr')
# показывает вкладку "календарь", предстоящие матчи
def show_matches():
    for items in match:
        info_match = items.find_all('td')
        #print(info_match[0].text,info_match[1].text, info_match[-3].text, info_match[-1].text)
        link_match = items.find_all('a')
        for l in link_match:
            #print(l.get('href'))
            pass