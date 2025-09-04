from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from BaseClass.log_class import LogCLassAll
from db.search import SearchDB
from aiogram import types
from BaseClass.start_class import InstanceBot

class SchedulerStart:
    def __init__(self):
        self.scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
        

class SchedulerStartBot(SchedulerStart):
    def __init__(self):
        super().__init__()
        db = SearchDB()
        self.list_default_scheduler = db.search_default_scheduler()
        
        self.scheduler.add_job(func=test_scheduler,
                          trigger=CronTrigger(hour=self.list_default_scheduler["hour"],
                                              minute=self.list_default_scheduler["minute"]))
        LogCLassAll().info("Start scheduler Bot")
        self.scheduler.start()
        
        
# class SchedulerStartBot(SchedulerStart):
#     def __init__(self):
#         super().__init__()
#         db = SearchDB()
#         self.list_default_scheduler = db.search_default_scheduler()
#         self.scheduler.add_job(test_scheduler, "interval",
#                                seconds=10)
#         self.scheduler.start()
#         LogCLassAll().info("Start scheduler test")
        
        
async def test_scheduler():
    LogCLassAll().debug('Test scheduler passed')
    db = SearchDB()
    list_user = db.search_user_all()
    for i in list_user:
        await scheduler_message_day(i[0])
        
async def scheduler_message_day(chat: int):
    await InstanceBot.bot.send_message(chat_id=chat,
                                    text='Хочу просто напомнить о себе')
    