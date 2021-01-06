from utils.show_seria_a import show_matches, show_link_matches, show_table
from utils.show_news import show_link_news, show_news
from prettytable import PrettyTable

def send_information_seria_a(): # выводит анонс предстоящих матчей
    tmp_list = []
    data, time_list, home_team_list, guest_team_list = show_matches()
    link_list = show_link_matches()
    for time, home_teams, guest_team, link in zip(time_list, home_team_list, guest_team_list, link_list):
        s  = ''
        s += '{}: {} - {}\n{}\n'.format(time.strip(), home_teams.strip(), guest_team.strip(), link.strip())
        tmp_list.append(s)
    return data, tmp_list

def send_table_seria_a():
    x = PrettyTable()
    position_list, team_list, M_list, W_list, N_list, L_list, SG_list, LG_list, P_list = show_table()
    x.add_column("№", [x.strip() for x in position_list])
    x.add_column("К", [x.strip() for x in team_list])
    x.add_column("И", [x.strip() for x in M_list])
    x.add_column("В", [x.strip() for x in W_list])
    x.add_column("Н", [x.strip() for x in N_list])
    x.add_column("П", [x.strip() for x in L_list])
    x.add_column("З", [x.strip() for x in SG_list])
    x.add_column("Пр", [x.strip() for x in LG_list])
    x.add_column("О", [x.strip() for x in P_list])
    return x

def send_news():
    tmp_list = []
    links_list = show_link_news()
    data, news_list = show_news()
    for news, links in zip(news_list, links_list):
        s = ''
        s += '{}\n{}\n'.format(news, links)
        tmp_list.append(s)
    return data, tmp_list