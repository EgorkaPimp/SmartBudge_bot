from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import Wishes

async def add_wish(user_id: int, comment: str):
    async with AsyncDatabaseSession() as db:
        wish = Wishes(user_id=user_id, comment=comment)
        db.add(wish)
        await db.commit()
        return wish
