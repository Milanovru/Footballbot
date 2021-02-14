from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


football_matches = InlineKeyboardMarkup(row_width=2) # клавиатура Серии А
seria_a = InlineKeyboardButton(text='Seria A 🇮🇹', callback_data='seria_a')
football_matches.insert(seria_a)

list_leage = InlineKeyboardButton(
    text='К списку лиг', callback_data='leage_list')
    
Seria_a = InlineKeyboardMarkup(row_width=2)
show_commands = InlineKeyboardButton(text='Последние новости Seria A', callback_data='show_news')
Seria_a.add(show_commands)
anons_matches = InlineKeyboardButton(
    text='Анонс матчей Seria A', callback_data='anons_matches')
Seria_a.add(anons_matches)
table_seria_a = InlineKeyboardButton(
    text='Турнирная таблица Seria A', callback_data='table')
Seria_a.add(table_seria_a)
Seria_a.add(list_leage)



out_keyboard = InlineKeyboardMarkup()
cancel= InlineKeyboardButton(text='Назад в меню', callback_data='cancel')
out_keyboard.add(cancel)

full_news = InlineKeyboardMarkup()
full = InlineKeyboardButton(text='Все новости', callback_data='full')
full_news.add(full)
full_news.add(cancel)

subscriptions = InlineKeyboardMarkup()
subs = InlineKeyboardButton(text='Подписаться', callback_data='subscript')
unsubs = InlineKeyboardButton(text='Отписаться', callback_data='unsubscript')
subscriptions.add(subs, unsubs)
