
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

football_matches = InlineKeyboardMarkup(row_width=2) # клавиатура Серии А
seria_a = InlineKeyboardButton(text='Seria A 🇮🇹', callback_data='seria_a')
football_matches.insert(seria_a)

Seria_a = InlineKeyboardMarkup(row_width=2)
show_commands = InlineKeyboardButton(text='Обзор команд Seria A', callback_data='show_commands')
Seria_a.add(show_commands)
anons_matches = InlineKeyboardButton(text='Анонс предстоящих матчей', callback_data='anons_matches')
Seria_a.add(anons_matches)
