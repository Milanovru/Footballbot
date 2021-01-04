from config import dp, bot
from aiogram import types
from buttons import football_matches
from aiogram.types import Message, CallbackQuery

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Приветики, {}. Для просмотра списка матчей введи /show!".format(message.from_user.full_name))

# этот хендлер задает дефолтный список команд
@dp.message_handler(commands="set_commands", state="*")
async def cmd_set_commands(message: types.Message):
    commands = [types.BotCommand(command="/show", description="Меню")]
    await bot.set_my_commands(commands)

@dp.message_handler(commands=['show'])
async def start_command(message: types.Message):
    await message.answer('Вот, что я могу тебе показать', reply_markup=football_matches)
