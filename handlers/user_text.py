from config import dp, admins
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from utils import send_information_seria_a, send_table_seria_a, send_news
from utils.show_seria_a import show_matches, show_link_matches, show_table
from utils.sports_ru_parse import show_new
from utils.for_sheduler.from_cron import test_cron
from buttons import football_matches, Seria_a, out_keyboard, full_news
from aiogram.types import Message, CallbackQuery
from utils.data_base.db_api import Database


db = Database()

@dp.callback_query_handler(text='cancel')
@dp.callback_query_handler(text='seria_a')
async def send_football(call: CallbackQuery):
    await call.answer('Меню Seria A')
    await call.message.edit_reply_markup(reply_markup=Seria_a) # пресылает другую клавиатуру в том же сообщении


@dp.callback_query_handler(text='anons_matches')
async def send_seria_a(call: CallbackQuery):
    await call.answer('Ближайший тур Seria A')
    info_list = send_information_seria_a(show_matches, show_link_matches)
    #await message.answer('\n'.join(link_list)) # вывод одним сообщением 
    await call.message.answer('Расписание матчей на ближайший тур:\n\n' + '\n'.join(info_list),disable_web_page_preview=True, reply_markup=out_keyboard)


@dp.callback_query_handler(text='full')
async def send_seria_a(call: CallbackQuery):  
    await call.answer('Просмотр новостей')
    await call.message.answer('https://www.sports.ru/seria-a/news/', reply_markup=out_keyboard)


@dp.callback_query_handler(text='cancel')      
@dp.callback_query_handler(text='show_news')
async def send_seria_a(call: CallbackQuery):  
    await call.answer('Просмотр новостей')
    date, news = send_news(show_new)
    await call.message.answer(date + '\n\n' + '\n'.join(news[:10]), reply_markup=full_news, disable_web_page_preview=True) # выводит последние 3 новости


@dp.callback_query_handler(text='table')
async def send_seria_a(call: CallbackQuery):
    await call.answer('Таблица Seria A')  
    await call.message.answer(send_table_seria_a(show_table), reply_markup=out_keyboard)
    

@dp.callback_query_handler(text='subscript')
async def send_seria_a(call: CallbackQuery):
    await call.answer('Оформление подписки')
    id = call.message.from_user.id
    user_name = call.message.from_user.full_name
    try:
        check = db.insert_user(id, user_name)
        await call.message.answer(check)
    except:
        await call.message.answer(check)

@dp.callback_query_handler(text='unsubscript')
async def send_seria_a(call: CallbackQuery):
    await call.answer('Удаление подписки')
    id = call.message.from_user.id
    try:
        check = db.delete_user(id)
        await call.message.answer(check)
    except:
        await call.message.answer(check)

@dp.message_handler(text='test')
async def test(message: types.Message):
    #test_cron(show_matches, show_link_matches)
    #await message.answer(message.from_user.id)
    pass


async def send_message(dp):  # это обработчик для шедулера
    await dp.bot.send_message(admins[0], 'это сообщение по таймингу, Милан играет через 2 часа')
