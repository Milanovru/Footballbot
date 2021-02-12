from aiogram import executor
from config import dp, scheduler
from handlers import dp
from handlers.user_text import send_message
from utils.for_sheduler.from_cron import test_cron
from utils.show_seria_a import show_matches, show_link_matches


def shedule_jobs():
  day_cron, hour_cron, minute_cron = test_cron(show_matches, show_link_matches)
  scheduler.add_job(send_message, "cron", day = day_cron,
                   hour=hour_cron - 2, minute=minute_cron, args=(dp,))
                   
    
if __name__ == "__main__":

  async def on_startup(dp):
    shedule_jobs()

scheduler.start()

executor.start_polling(dp, on_startup=on_startup)
