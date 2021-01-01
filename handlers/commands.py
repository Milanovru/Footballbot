from config import dp
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Приветики, {}!".format(message.from_user.full_name))