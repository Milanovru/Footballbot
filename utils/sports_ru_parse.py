import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from fake_useragent import UserAgent


ua = UserAgent(use_cache_server=False, verify_ssl=False)
headers = {'headers': ua.random}
responce_italy = requests.get(os.getenv('PARSE_LINK_ITALY'), headers=headers).text
responce_news = requests.get(
    os.getenv('PARSE_LINK_NEWS'), headers=headers).text

soup_italy = BeautifulSoup(responce_italy, 'lxml')
soup_news = BeautifulSoup(responce_news, 'lxml')

info = soup_italy.find_all('tbody')
show_new = soup_news.body.find('div', id='branding-layout').find('div', class_ = "pageLayout").find('div', class_ = "contentLayout js-active").find('div', class_='layout-columns layout-columns_nopaddingTop').find('div', class_='news').find('div')
# присылает ссылки на мачти
match = info[0].find_all('tr') # показывает вкладку "календарь", предстоящие матчи
table = info[1].find_all('tr') # показывает таблицу
            
