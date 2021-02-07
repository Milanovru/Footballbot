from aiogram import executor
from config import dp
from handlers import dp
from config import scheduler
from handlers.user_text import send_message


def shedule_jobs(): 
    scheduler.add_job(send_message, "interval", seconds=5, args=(dp,))
    
if __name__ == "__main__":

  async def on_startup(dp):
    shedule_jobs()

scheduler.start()
executor.start_polling(dp, on_startup=on_startup)
