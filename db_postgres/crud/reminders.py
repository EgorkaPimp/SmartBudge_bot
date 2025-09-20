from sqlalchemy.future import select
from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import Reminders

async def add_reminders(user_id: int, status: int = 1):
    async with AsyncDatabaseSession() as db:
        remind = Reminders(user_id=user_id, status=status)
        db.add(remind)
        await db.commit()
        await db.refresh(remind)
        return remind
        

async def update_reminders_status(user_id: int, new_status: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(Reminders).where(Reminders.user_id == user_id))
        reminder = result.scalars().first()
        if reminder:
            reminder.status = new_status
            await db.commit()
        return reminder
    
async def status_search(user_id: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(
            select(Reminders).where((Reminders.user_id == user_id)))
        expense = result.scalars().first()
        return expense