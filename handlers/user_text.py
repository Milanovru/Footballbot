from config import dp
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from utils import show_table, send_information_seria_a
from buttons import football_matches, Seria_a
from aiogram.types import Message, CallbackQuery


@dp.callback_query_handler(text='seria_a')
async def send_football(call: CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup(reply_markup=Seria_a) # пресылает другую клавиатуру в том же сообщении

@dp.callback_query_handler(text='anons_matches')
async def send_seria_a(call: CallbackQuery):
    data, info_list = send_information_seria_a()
    #await message.answer('\n'.join(link_list)) # вывод одним сообщением 
    await call.answer('Ближайший тур Seria A')
    await call.message.answer('Расписание матчей на ближайший тур {}:\n'.format(data)+ '\n'.join(info_list),disable_web_page_preview=True)
       
@dp.callback_query_handler(text='show_commands')
async def send_seria_a(call: CallbackQuery):  
    await call.answer('В разработке')
    await call.message.answer('В разработке')

@dp.callback_query_handler(text='table')
async def send_seria_a(call: CallbackQuery):  
    position_list, team_list = show_table()
    await call.answer('Таблица Seria A')
    for position, team in zip(position_list, team_list):
        await call.message.answer('{}:{}'.format(position.strip(), team.strip()))
