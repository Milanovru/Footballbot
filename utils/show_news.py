from utils.sports_ru_parse import show_new

def show_news():
    data = show_new.b.text # дата
    tmp_list = []
    for news in show_new.find_all('p', class_='one_news'):
        s = ''
        s += news.find('span').text + ' ' + news.find('a').text # время и новость
        tmp_list.append(s) 
    return data, tmp_list
    
def show_link_news():
    link_list = []
    for i in show_new.find_all('a'):
        if not i.get('href').endswith('comments'):
            link_list.append(i.get('href'))
    return mod_link_news(link_list)

def mod_link_news(list_news):
    tmp_list = []
    https = 'https://www.sports.ru'
    for link in list_news:
        if link.startswith('https'):
            tmp_list.append(link)
        else:
            tmp_list.append(https+link)
    return tmp_list