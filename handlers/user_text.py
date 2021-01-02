from config import dp
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from utils.sports_ru_parse import show_matches
from buttons import football_matches
from aiogram.types import Message, CallbackQuery

@dp.callback_query_handler(text='seria_a')
async def matches(call: CallbackQuery):
    data, time_list, home_team_list, guest_team_list, link_match = show_matches()
    await call.answer('Ближайший тур Seria A')
    await call.message.answer('Расписание матчей на ближайший тур {}:'.format(data))
    for time, home, guest in zip(time_list, home_team_list, guest_team_list):
        await call.message.answer('{}: {} - {}'.format(time, home, guest))
        