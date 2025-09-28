from sqlalchemy.future import select
from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import EveryWaste

async def add_record(user_id: int, category: str, expense: float, data: str):
    async with AsyncDatabaseSession() as db:
        print(data)
        record = EveryWaste(user_id=user_id, category=category, expense=expense, data_time=data)
        db.add(record)
        await db.commit()
        await db.refresh(record)
        return record