from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from BaseClass.log_class import LogCLassAll
from BaseClass.db_class import SearchDB

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
        
        
# class SchedulerTest(SchedulerStart):
#     def __init__(self):
#         super().__init__()
#         db = SearchDB()
#         self.list_default_scheduler = db.search_default_scheduler()
#         self.scheduler.add_job(test_scheduler, "interval",
#                                seconds=self.list_default_scheduler["minute"])
#         self.scheduler.start()
#         LogCLassAll().info("Start scheduler test")
        
        
def test_scheduler():
    LogCLassAll().debug('Test scheduler passed')