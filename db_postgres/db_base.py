from db_postgres.db import engine, Base
import db_postgres.models #noqa

async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all) #Включить для очистки базы
        await conn.run_sync(Base.metadata.create_all)
