from sqlalchemy.future import select
from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import PlanSpending

async def add_plan_spending(user_id: int, category: str, amount_money: int):
    async with AsyncDatabaseSession() as db:
        amount = PlanSpending(user_id=user_id, category=category, amount_money=amount_money)
        db.add(amount)
        await db.commit()
        await db.refresh(amount)
        return amount

async def get_plan_spending(user_id: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(PlanSpending).where(PlanSpending.user_id == user_id))
        return result.scalars().all()

async def delete_plan_spending(user_id: int, category: str):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(PlanSpending).where(PlanSpending.user_id==user_id, 
                                                             PlanSpending.category==category))
        amount = result.scalars().first()
        if amount:
            await db.delete(amount)
            await db.commit()
        return amount