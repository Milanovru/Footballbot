from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from conf_data import BOT_TOKEN

bot = Bot(token= BOT_TOKEN, parse_mode= types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage= storage)