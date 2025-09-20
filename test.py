from db_postgres.crud.shares import status_share_search
import asyncio

async def test():
    x = await status_share_search(933194755)
    y = await status_share_search(875300228)
    print(x)
    print(y.master_id)
    
asyncio.run(test())
print(123)