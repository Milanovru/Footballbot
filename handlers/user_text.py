from config import dp
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from utils.sports_ru_parse import show_matches

@dp.message_handler(text='матчи')
async def matches(message: types.Message):
    await message.answer('В разработке')