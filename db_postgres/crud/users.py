from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import User
from sqlalchemy.future import select

async def add_user(user_id: int, username: str, role: int = 1):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(
            select(User).where(User.id == user_id)
        )
        record = result.scalars().first()

        if not record:
            user = User(id=user_id, username=username, role=role)
            db.add(user)
            await db.commit()
            await db.refresh(user)
            return user


async def get_user(user_id: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalars().first()


async def update_user_role(user_id: int, new_role: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if user:
            user.role = new_role
            await db.commit()
        return user


async def delete_user(user_id: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if user:
            await db.delete(user)
            await db.commit()
        return user
