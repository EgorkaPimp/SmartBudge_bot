from sqlalchemy.future import select
from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import Reminders

async def update_reminders_status(user_id: int, new_status: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(Reminders).where(Reminders.user_id == user_id))
        reminder = result.scalars().first()
        if reminder:
            reminder.status = new_status
            await db.commit()
        return reminder