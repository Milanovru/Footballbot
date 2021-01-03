import requests
from bs4 import BeautifulSoup
from conf_data import PARSE_LINK

responce = requests.get(PARSE_LINK).text
soup = BeautifulSoup(responce, features='html.parser')

info = soup.find_all('tbody')

# присылает ссылки на мачти
match = info[0].find_all('tr') # показывает вкладку "календарь", предстоящие матчи
table = info[1].find_all('tr') # показывает таблицу
            