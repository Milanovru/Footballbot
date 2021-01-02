
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

football_matches = InlineKeyboardMarkup(row_width=2) # клавиатура
seria_a = InlineKeyboardButton(text='Seria A 🇮🇹', callback_data='seria_a')
football_matches.insert(seria_a)

