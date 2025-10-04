from sqlalchemy.future import select
from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import EveryWaste

async def add_record(user_id: int, category: str, expense: float, data: str):
    async with AsyncDatabaseSession() as db:
        record = EveryWaste(user_id=user_id, category=category, expense=expense, data_time=data)
        db.add(record)
        await db.commit()
        await db.refresh(record)
        return record
    
async def update_record(user_id: int, category: str, 
                          new_category: str):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(EveryWaste).where((EveryWaste.user_id == user_id) &
                                                        (EveryWaste.category == category)))
        all_record = result.scalars().all()
        if not all_record:
            return None
        for record in all_record:
            record.category = new_category
        await db.commit()
        return all_record
   
async def delete_record(user_id: int, category: str):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(EveryWaste).where(EveryWaste.user_id==user_id, 
                                                           EveryWaste.category==category))
        record_all = result.scalars().all()
        if record_all:
            for record in record_all:
                await db.delete(record)
                await db.commit()
        return record_all  
    
async def get_record(user_id: int):
       async with AsyncDatabaseSession() as db:
        result = await db.execute(select(EveryWaste).where(EveryWaste.user_id==user_id))
        record_all = result.scalars().all()
        waste = []
        if record_all:
            for record in record_all:
                map = {}
                map[record.category] = [record.expense, record.data_time, record.comment]
                waste.append(map)
        return waste 
    
async def delete_update(user_id: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(EveryWaste).where(EveryWaste.user_id==user_id))
        record_all = result.scalars().all()
        if record_all:
            for record in record_all:
                await db.delete(record)
                await db.commit()