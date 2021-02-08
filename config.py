from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler


load_dotenv()

loop = asyncio.get_event_loop()

bot = Bot(token=os.getenv('BOT_TOKEN'), parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

scheduler = AsyncIOScheduler()

dp = Dispatcher(bot, storage=storage)

admins = [1027622714]
