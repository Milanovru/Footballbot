from utils.information_output import send_information_seria_a, send_news
import requests
from bs4 import BeautifulSoup
def get_started_match(show_matches, show_link_matches):
    # получаю дату и полную инфу на игровой день
    info = send_information_seria_a(
        show_matches=show_matches, show_link_matches=show_link_matches)
    team = 'Милан'
    team_info = ''

    # вытаскиваю строчку, где играет Милан
    for check in info:
        if team in check:
            team_info = check
            break

    # ['13', 'февраля', '22:45:', 'Специя', '-', 'Милан',
    #     'https://www.sports.ru/football/match/1461091/']
    day_cron = team_info.split()[0] # выводим дату
    hour_cron = team_info.split()[2].split(":")[0] # выводим часы
    minute_cron = team_info.split()[2].split(":")[1] # выводим минуты
    
    return int(day_cron), int(hour_cron), int(minute_cron)
    
def get_breaking_news(show_new):
    data, news = send_news(show_new=show_new)
    # 00:18 Лукаку забил 300-й гол в карьере
    # https://www.sports.ru/football/1093950768-lukaku-zabil-300-j-gol-v-karere.html
    day = data.split()[0]
    hours = news[0].split(' ')[0].split(':')[0]
    minutes = news[0].split(' ')[0].split(':')[1]
    return int(day), int(hours), int(minutes)
