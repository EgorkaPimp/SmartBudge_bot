from sqlalchemy.future import select
from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import StatusScheduler

async def add_status_scheduler(user_id: int, status: int = 1):
    async with AsyncDatabaseSession() as db:
        amount = StatusScheduler(user_id=user_id, 
                                 status_notification=status,
                                 status_update=status)
        db.add(amount)
        await db.commit()
        await db.refresh(amount)
        return amount
    
async def update_status_scheduler(user_id: int, new_status: int, type_status: str):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(
            select(StatusScheduler).where(StatusScheduler.user_id == user_id)
        )
        status = result.scalars().first()
        if status:
            setattr(status, type_status, new_status)  # <-- вот так
            await db.commit()
            await db.refresh(status)  # обновим объект из базы
        return status
    
async def search_status(user_id: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(
            select(StatusScheduler).where(StatusScheduler.user_id == user_id)
        )
        record = result.scalars().first()
        return record
    
async def search_user(notification: bool = False, update: bool = False):
    async with AsyncDatabaseSession() as db:
        if notification is True:
            result = await db.execute(
                select(StatusScheduler).where(StatusScheduler.status_notification == 1)
            )
            record = result.scalars().all()
            return record
        elif update is True:
            result = await db.execute(
                select(StatusScheduler).where(StatusScheduler.status_update == 1)
            )
            record = result.scalars().all()
            return record