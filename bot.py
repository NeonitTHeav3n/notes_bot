import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router
import database as db



async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    db.create_table()
    print("Бот запущен...")
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())


