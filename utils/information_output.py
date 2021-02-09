from utils.show_news import show_link_news, show_news
from utils.sports_ru_parse import match, table
from prettytable import PrettyTable


def send_information_seria_a(show_matches, show_link_matches): # выводит анонс предстоящих матчей
    tmp_list = []
    data_list, time_list, home_team_list, guest_team_list = show_matches(match)
    link_list = show_link_matches(match)
    for data, time, home_teams, guest_team, link in zip(data_list, time_list, home_team_list, guest_team_list, link_list):
        s  = ''
        s += '{} {}: {} - {}\n{}\n'.format(data.strip(), time.strip(), home_teams.strip(), guest_team.strip(), link.strip())
        tmp_list.append(s)
    return tmp_list


def send_table_seria_a(show_table):
    x = PrettyTable()
    position_list, team_list, M_list, W_list, N_list, L_list, SG_list, LG_list, P_list = show_table(table)
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


def send_news(show_new):
    tmp_list = []
    links_list = show_link_news(show_new)
    data, news_list = show_news(show_new)
    for news, links in zip(news_list, links_list):
        s = ''
        s += '{}\n{}\n'.format(news, links)
        tmp_list.append(s)
    return data, tmp_list
    
