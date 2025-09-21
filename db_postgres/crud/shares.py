from sqlalchemy.future import select
from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import Share


async def add_share_status_master(user_id: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(
            select(Share).where(Share.master_id == user_id)
        )
        record = result.scalars().first()
        if not record:
            new_record = Share(master_id = user_id)  
            db.add(new_record)
            await db.commit()
            await db.refresh(new_record)
            return new_record
        return record
    
async def add_share_status_slave(user_id: int, master_id: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(
            select(Share).where(Share.master_id == master_id)
        )
        slave = result.scalars().first()
        if slave.master_id != user_id:
            slave.slave_id = user_id
            await db.commit()
            return slave
        
async def status_share_search(user_id: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(
            select(Share).where((Share.slave_id == user_id)))
        expense = result.scalars().first()
        return expense
    
async def master_slave(user_id: int):
        master = await status_share_search(user_id=user_id)
        if master:
                user_id = master.master_id
        return user_id
    
async def search_slave(user_id: int):
        async with AsyncDatabaseSession() as db:
            result = await db.execute(
                select(Share).where((Share.master_id == user_id)))
            expense = result.scalars().first()
            return expense