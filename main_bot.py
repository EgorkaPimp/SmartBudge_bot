import asyncio
from datetime import datetime
from BaseClass.log_class import LogCLassAll
from BaseClass.start_class import StartBot
from BaseClass.scheduler_class import SchedulerStartBot
from db_postgres.db_base import init_models
from db_postgres.crud.scheduler_default import add_scheduler_default

from app import *  # noqa: F403
    
async def main():
    LogCLassAll().info("Start logging")
    await init_models()
    await add_scheduler_default()
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