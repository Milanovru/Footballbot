from config import dp
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from utils.sports_ru_parse import show_matches

@dp.message_handler(text='матчи')
async def matches(message: types.Message):
    data, time_list, home_team_list, guest_team_list = show_matches()
    await message.answer('Расписание матчей на ближайший тур {}'.format(data))
    for time, home, guest in zip(time_list, home_team_list, guest_team_list):
        await message.answer('{}: {} - {}'.format(time, home, guest))
        
    