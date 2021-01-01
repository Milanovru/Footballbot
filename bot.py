     
if __name__ == "__main__":
    from aiogram import executor
    from config import dp
    from handlers import dp
    
executor.start_polling(dp)
