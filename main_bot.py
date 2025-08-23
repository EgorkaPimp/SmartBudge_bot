import asyncio
from datetime import datetime
from BaseClass.log_class import LogCLassAll
from BaseClass.start_class import StartBot
from BaseClass.scheduler_class import SchedulerStartBot
from BaseClass.db_class import CreateDB


from app import *
    
async def main():
    LogCLassAll().info("Start logging")
    CreateDB()
    bot = StartBot()
    SchedulerStartBot()
    await bot.run()
    
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        LogCLassAll().error(f"script interrupted: {datetime.now()}")
    except Exception as e:
        LogCLassAll().error(f"Bug: \n {e}")