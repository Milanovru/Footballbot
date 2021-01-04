from config import dp
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from utils import send_information_seria_a, send_table_seria_a
from buttons import football_matches, Seria_a, out_keyboard
from aiogram.types import Message, CallbackQuery

@dp.callback_query_handler(text='cancel')
@dp.callback_query_handler(text='seria_a')
async def send_football(call: CallbackQuery):
    await call.answer('Меню Seria A')
    await call.message.edit_reply_markup(reply_markup=Seria_a) # пресылает другую клавиатуру в том же сообщении

@dp.callback_query_handler(text='anons_matches')
async def send_seria_a(call: CallbackQuery):
    await call.answer('Ближайший тур Seria A')
    data, info_list = send_information_seria_a()
    #await message.answer('\n'.join(link_list)) # вывод одним сообщением 
    await call.message.answer('Расписание матчей на ближайший тур {}:\n'.format(data)+ '\n'.join(info_list),disable_web_page_preview=True, reply_markup=out_keyboard)
       
@dp.callback_query_handler(text='show_commands')
async def send_seria_a(call: CallbackQuery):  
    await call.answer('В разработке',)
    await call.message.answer('В разработке')

@dp.callback_query_handler(text='table')
async def send_seria_a(call: CallbackQuery):
    await call.answer('Таблица Seria A')  
    await call.message.answer(send_table_seria_a(), reply_markup=out_keyboard)
    