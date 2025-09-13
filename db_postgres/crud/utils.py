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
            difference = exp_val - plan_val
            comparison.append({
                "category": cat,
                "amount_expenses": exp_val,
                "amount_money": plan_val,
                "difference": difference
            })

        return comparison
