import requests
from bs4 import BeautifulSoup
from conf_data import PARSE_LINK

responce = requests.get(PARSE_LINK).text
soup = BeautifulSoup(responce, features='html.parser')

tables = soup.find_all('tbody')

# присылает ссылки на мачти
match = tables[0].find_all('tr')
# показывает вкладку "календарь", предстоящие матчи

            