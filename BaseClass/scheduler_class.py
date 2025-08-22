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
                          trigger=CronTrigger(minute=20))
        LogCLassAll().info("Start scheduler Bot")
        self.scheduler.start()
        
class SchedulerTest(SchedulerStart):
    def __init__(self):
        super().__init__()
        self.time_test = 10
        self.scheduler.add_job(test_scheduler, "interval", seconds=self.time_test)
        self.scheduler.start()
        LogCLassAll().info("Start scheduler test")
        
        
def test_scheduler():
    LogCLassAll().debug('Test scheduler passed')