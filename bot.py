from aiogram import executor
from config import dp, scheduler
from handlers import dp
from handlers.user_text import send_match, send_new
from utils.for_sheduler.from_cron import get_started_match, get_breaking_news
from utils.show_seria_a import show_matches, show_link_matches
from utils.sports_ru_parse import show_new


def started_match():
  day_cron, hour_cron, minute_cron = get_started_match(
      show_matches, show_link_matches)
  try:
    scheduler.add_job(send_match, "cron", day= int(day_cron),
                      hour= int(hour_cron), minute= int(minute_cron), args=(dp,))
  except:
    pass

def breaking_news():
  day_cron, hour_cron, minute_cron = get_breaking_news(show_new)
  scheduler.add_job(send_new, "cron", day=day_cron,
                    hour=hour_cron, minute=minute_cron, args=(dp,), jitter=120)
  

if __name__ == "__main__":

  async def on_startup(dp):
    started_match()
    breaking_news()

scheduler.start()

executor.start_polling(dp, on_startup=on_startup)
