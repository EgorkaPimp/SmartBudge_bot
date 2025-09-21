from sqlalchemy import select
from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import Expense, PlanSpending

async def get_category_comparison(user_id: int):
    async with AsyncDatabaseSession() as db:
        # Получаем все расходы
        expenses_result = await db.execute(
            select(Expense).where(Expense.user_id == user_id)
        )
        expenses = {e.category: e.amount_expenses for e in expenses_result.scalars()}

        # Получаем все планы
        plans_result = await db.execute(
            select(PlanSpending).where(PlanSpending.user_id == user_id)
        )
        plans = {p.category: p.amount_money for p in plans_result.scalars()}

        # Формируем итог
        comparison = []
        all_categories = set(expenses.keys()) | set(plans.keys())
        for cat in all_categories:
            exp_val = expenses.get(cat, 0)
            plan_val = plans.get(cat, 0)
            difference = plan_val - exp_val
            comparison.append({
                "category": cat,
                "spent": exp_val,
                "plan": plan_val,
                "remaining": difference
            })

        return comparison

async def sync_expenses_with_plans(user_id: int):
    async with AsyncDatabaseSession() as db:
        # Получаем все планы
        plans_result = await db.execute(
            select(PlanSpending).where(PlanSpending.user_id == user_id)
        )
        plans = plans_result.scalars().all()

        for plan in plans:
            # Ищем соответствующий Expense
            expense_result = await db.execute(
                select(Expense).where(
                    Expense.user_id == user_id,
                    Expense.category == plan.category
                )
            )
            expense = expense_result.scalars().first()

            if expense:
                # Обновляем существующий
                expense.amount_expenses = plan.amount_money
            else:
                # (опционально) создаём новый
                new_expense = Expense(
                    user_id=user_id,
                    category=plan.category,
                    amount_expenses=plan.amount_money
                )
                db.add(new_expense)

        await db.commit()