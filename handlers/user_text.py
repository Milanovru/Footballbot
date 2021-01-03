from config import dp
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from utils import show_matches, show_link_matches
from buttons import football_matches, Seria_a
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text='seria_a')
async def send_football(call: CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup(reply_markup=Seria_a) # пресылает другую клавиатуру в том же сообщении

@dp.callback_query_handler(text='anons_matches')
async def send_seria_a(call: CallbackQuery):
    data, time_list, home_team_list, guest_team_list = show_matches()
    link_list = show_link_matches()
    #await message.answer('\n'.join(link_list)) # вывод одним сообщением 
    await call.answer('Ближайший тур Seria A')
    await call.message.answer('Расписание матчей на ближайший тур {}:'.format(data))
    for time, home, guest, link in zip(time_list, home_team_list, guest_team_list, link_list):
            await call.message.answer('{}: {} - {} {}'.format(time, home, guest, link), disable_web_page_preview=True)
    
        
    
    