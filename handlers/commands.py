from config import dp, bot, admins
from aiogram import types
from buttons import *
from aiogram.types import Message, CallbackQuery
from handlers.user_text import db

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет, <b>{}</b>.\nФутбольное меню -  /menu;\nПодписки на матчи -  /subscriptions.\n\nДля дальнейшей навигаии используй кнопки или введи '/' для отображения подсказок".format(message.from_user.full_name))
    

# этот хендлер задает дефолтный список команд
@dp.message_handler(commands="set_commands", state="*", user_id=admins[0])
async def cmd_set_commands(message: types.Message):
    commands = [types.BotCommand(command="/menu", description="Просмотр футбольного меню"),
                types.BotCommand(command="/subscriptions", description="Подписки на анонсы матчей интересующей команды")
    ]
    await bot.set_my_commands(commands)
    await message.answer('Изменения внесены')

@dp.message_handler(commands=['menu'])
async def start_command(message: types.Message):
    await message.answer('Выбирай лигу', reply_markup=football_matches)

@dp.message_handler(commands=['create_db'], user_id=admins[0])
async def create_db(message: types.Message):
    db.create_table()
    await message.answer('база данных создана успешно!')

@dp.message_handler(commands=['subscriptions'])
async def start_command(message: types.Message):
    await message.answer('Что хочешь сделать?', reply_markup=subscriptions)
