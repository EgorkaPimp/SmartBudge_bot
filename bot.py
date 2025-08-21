import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

"""Импорт внутри проекта"""
from db.create_db import init_db, base_category_update, reminder_day
from token_file import read_file
from handlers import register_handlers
from collback import add_fin_callbacks

my_token = read_file()
logging.basicConfig(filename='bot.log', level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(name)s - %(message)s')



def setup_scheduler(bot: Bot):
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(
        base_category_update,
        trigger=CronTrigger(day=14, hour=14, minute=8),
        args=[bot],
        id="daily_update"
    )

    scheduler.add_job(
        reminder_day,
        trigger=CronTrigger(hour=22, minute=45),
        args=[bot],
        id="reminder"
    )

    scheduler.start()
    logging.info("Планировщик запущен")


async def on_startup(dp: Dispatcher):
    setup_scheduler(dp.bot)


async def main():
    init_db()
    bot = Bot(token=my_token)
    dp = Dispatcher()

    add_fin_callbacks(dp)
    await register_handlers(dp)

    setup_scheduler(bot)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"Script interrupted: {datetime.now()}")
