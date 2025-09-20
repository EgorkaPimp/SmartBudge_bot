from sqlalchemy.future import select
from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import SchedulerDefault

async def add_scheduler_default():
    async with AsyncDatabaseSession() as db:
        # Проверяем, есть ли запись с id = 1
        result = await db.execute(
            select(SchedulerDefault).where(SchedulerDefault.id == 1)
        )
        record = result.scalars().first()

        if not record:
            # Если нет — создаём
            new_record = SchedulerDefault(id=1, day=1, hour=22, minute=45)  
            db.add(new_record)
            await db.commit()
            await db.refresh(new_record)
            return new_record
        return record