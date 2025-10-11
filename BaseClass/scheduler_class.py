from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from app.scheduler import daily_reminder, update

class SchedulerStart:
    def __init__(self):
        self.scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
        
        
class SchedulerStartBot(SchedulerStart):
    def __init__(self):
        super().__init__()
        self.scheduler.add_job(func=daily_reminder,
                               trigger=CronTrigger(hour=22,
                                           minute=30))
        # self.scheduler.add_job(daily_reminder, "interval", seconds=10)
        self.scheduler.add_job(func=update,
                               trigger=CronTrigger(day=1,
                                                   hour=10,))
        self.scheduler.start()
           