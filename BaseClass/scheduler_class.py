from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from BaseClass.log_class import LogCLassAll

class SchedulerStart:
    def __init__(self):
        self.scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
        

class SchedulerStartBot(SchedulerStart):
    def __init__(self):
        super().__init__()
        
        self.scheduler.add_job(func=test_scheduler,
                          trigger=CronTrigger(hour=22,
                                              minute=30))
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
        
    