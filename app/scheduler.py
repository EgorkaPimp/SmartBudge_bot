from BaseClass.log_class import LogCLassAll
from db_postgres.crud.status_scheduler import search_user
from BaseClass.start_class import InstanceBot
from db_postgres.crud.shares import master_slave
from db_postgres.crud.utils import get_category_comparison
from app.show_table import create_table
from db_postgres.crud.utils import sync_expenses_with_plans


async def daily_reminder():
        LogCLassAll().debug("Scheduler daily_reminder start")
        users = await search_user(notification=True)
        for user in users:
            await InstanceBot.bot.send_message(chat_id=user.user_id,
                                               text="Я просто решил напомнить о себе")
            
async def update():
        LogCLassAll().debug("Scheduler update start")
        users = await search_user(update=True)
        for user in users:
            user_id = await master_slave(user.user_id)
            plan = await get_category_comparison(user_id=user_id)
            full_table = await create_table(plan)
                   
            await InstanceBot.bot.send_message(chat_id=user.user_id,
                                               text="Вот так выглядит твой месяц:\n" + full_table,
                                               parse_mode="MarkdownV2")
            if user.user_id == user_id:
                await sync_expenses_with_plans(user.user_id)

        