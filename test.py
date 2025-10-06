from db_postgres.crud.users import add_user
import asyncio

async def test():
    await add_user(6681145468, 'test11')
    
asyncio.run(test())