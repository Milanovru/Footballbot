from utils.sports_ru_parse import match
from utils.sports_ru_parse import table

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

def show_link_matches(): 
    link_matches = []
    for items in match:
        link_match = items.find_all('a')
        for link in link_match:
            link_matches.append(link.get('href')) # ссылки на матч и команды
    return mod_show_link_matches(link_matches)

def mod_show_link_matches(link_matches): # фильтрует ссылки на ТОЛЬКО матчей
    tmp_list = []
    https = 'https://www.sports.ru'
    for link in link_matches:
        if '/match/' in link:
            if link.startswith('https'):
                tmp_list.append(link)
            else:
                tmp_list.append(https+link)
    return tmp_list

def show_table():
    position_list = []
    team_list = []
    M_list = []
    W_list = []
    N_list = []
    L_list = []
    SG_list = []
    LG_list = []
    P_list = []
    for items in table:
        info = items.find_all('td')
        position_list.append(info[0].text) # позиция
        team_list.append(info[1].text) # команда
        M_list.append(info[2].text) # кол-во матчей
        W_list.append(info[3].text) #  кол-во побед
        N_list.append(info[4].text) # кол-во ничьей
        L_list.append(info[5].text) # кол-во поражений
        SG_list.append(info[6].text) # кол-во забитых мячей
        LG_list.append(info[7].text) # кол-во пропущенных мячей
        P_list.append(info[8].text) # кол-во очкой    
    return position_list, team_list, M_list, W_list, N_list, L_list, SG_list, LG_list, P_list
    #print(info[0].text, info[1].text, info[2].text, info[3].text, info[4].text, info[5].text, info[6].text, info[7].text, info[8].text)