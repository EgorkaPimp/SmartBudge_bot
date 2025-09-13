from db_postgres.crud.users import add_user, get_user, update_user_role, delete_user
from db_postgres.crud.expenses import add_expense, get_expenses, delete_expense, update_expenses, category_exists
from db_postgres.crud.plan_spending import add_plan_spending, get_plan_spending, delete_plan_spending
from db_postgres.crud.utils import get_category_comparison
import time
import asyncio


async def users(user_id: int):
    await add_user(user_id=user_id, username="egor", role=1)
    print('add')


    # Получить
    user = await get_user(user_id)
    print(user.role)


    # Обновить роль
    await update_user_role(user_id, new_role=0)
    print('update')

    
async def expenses(user_id: int):
    await add_expense(user_id, 'test', 10000)
    await add_expense(user_id, 'test2', 20000)
    await add_expense(user_id, 'test3', 30000)
    await add_expense(user_id, 'test4', 40000)
    await add_expense(user_id, 'test5', 500)
    print('add all category')
    
    
    expenses = await get_expenses(user_id)
    for exp in expenses:
        print(exp.category, exp.amount_expenses)
    

    await delete_expense(user_id, 'test')
    print('del category')
    
    

async def plan_spending(user_id: int):
    await add_plan_spending(user_id, 'test2', 1000)
    await add_plan_spending(user_id, 'test3', 1000)
    await add_plan_spending(user_id, 'test4', 3000)
    await add_plan_spending(user_id, 'test5', 3000)
    print('add all category')
    
    
    spending = await get_plan_spending(user_id)
    for spen in spending:
        print(spen.category, spen.amount_money)
    
    
    await delete_plan_spending(user_id, 'test3')
    print('del test3')

async def main():
    user_id = 12345
    
    await users(user_id)
    
    await expenses(user_id)
    
    # await plan_spending(user_id)
    
    # result = await get_category_comparison(user_id)
    
    # x = await update_expenses(user_id=user_id, 
    #                           category='new_test',
    #                           new_category='new_test1')
    # print(x.category)
    
    # x = await update_expenses(user_id=user_id, 
    #                           category='new_test1',
    #                           amount_expenses=100)
    # print(x.amount_expenses)
    
    # # # for i in result:
    # # #     print(i)
    
    exists = await category_exists(user_id=12345, category='test')
    if exists:
        print("Категория существует")
    else:
        print("Категория отсутствует")
    
    # Удалить
    await delete_user(user_id)
    print('del')
    
    
asyncio.run(main())