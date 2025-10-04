from db_postgres.db import AsyncDatabaseSession
from db_postgres.models import MonthlyReport

async def add_report(user_id: int, path_to_json: str):
    async with AsyncDatabaseSession() as db:
        report = MonthlyReport(user_id=user_id, path_to_json=path_to_json)
        db.add(report)
        await db.commit()
        return report
