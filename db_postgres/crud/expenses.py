from sqlalchemy.future import select
from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import Expense

async def add_expense(user_id: int, category: str, amount_expenses: float):
    async with AsyncDatabaseSession() as db:
        exp = Expense(user_id=user_id, category=category, amount_expenses=amount_expenses)
        db.add(exp)
        await db.commit()
        await db.refresh(exp)
        return exp

async def get_expenses(user_id: int):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(Expense).where(Expense.user_id == user_id))
        return result.scalars().all()

async def delete_expense(user_id: int, category: str):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(Expense).where(Expense.user_id==user_id, Expense.category==category))
        exp = result.scalars().first()
        if exp:
            await db.delete(exp)
            await db.commit()
        return exp
    
async def update_expenses(user_id: int, category: str, 
                          new_category: str = None, amount_expenses: float = None):
    async with AsyncDatabaseSession() as db:
        result = await db.execute(select(Expense).where((Expense.user_id == user_id) &
                                                        (Expense.category == category)))
        expense = result.scalars().first()
        print('Found expense:', expense)
        if not expense:
            print('Expense not found')
            return None
        print('start, new_category:', new_category, 'amount_expenses:', amount_expenses)
        # Обновляем поля
        if new_category is not None:
            expense.category = new_category
        if amount_expenses is not None:
            expense.amount_expenses = amount_expenses
        await db.commit()
        await db.refresh(expense)
        return expense
    
async def add_to_expenses(user_id: int, category: str, amount_to_add: float):
    async with AsyncDatabaseSession() as db:
        # Находим запись
        result = await db.execute(
            select(Expense).where(
                (Expense.user_id == user_id) & (Expense.category == category)
            )
        )
        expense = result.scalars().first()
        if not expense:
            return None  # запись не найдена

        # Прибавляем к текущему значению
        expense.amount_expenses -= amount_to_add

        await db.commit()
        await db.refresh(expense)
        return expense
    
async def category_exists(user_id: int, category: str) -> bool:
    async with AsyncDatabaseSession() as db:
        result = await db.execute(
            select(Expense).where(
                (Expense.user_id == user_id) & (Expense.category == category)
            )
        )
        expense = result.scalars().first()
        return expense is not None
    
async def update_expenses_amount(user_id: int, category: str, new_amount: float):
     async with AsyncDatabaseSession() as db:
        result = await db.execute(select(Expense).where(Expense.user_id==user_id, 
                                                             Expense.category==category))
        amount = result.scalars().first()
        new_amount = amount.amount_expenses - new_amount
        amount.amount_expenses = new_amount
        await db.commit()
        await db.refresh(amount)
        return amount