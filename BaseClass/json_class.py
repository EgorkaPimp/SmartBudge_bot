from db_postgres.crud.utils import get_category_comparison
from db_postgres.crud.every_waste import get_record
import json
import datetime
from collections import defaultdict

class JsonWork:
    def __init__(self, user_id, plan, waste):
        self.user_id = user_id
        self.plan = plan
        self.waste = waste

    @classmethod
    async def create(cls, user_id: int):
        plan = await get_category_comparison(user_id=user_id)
        waste = await get_record(user_id=user_id)
        return cls(user_id, plan, waste)
    
    async def to_json(self) -> dict:
        """Собираем данные в структуру JSON"""
        categories_data = []
        
        # Группируем расходы по категориям
        grouped_expenses = defaultdict(list)
        for w in self.waste:
            for category, values in w.items():
                amount, date, note = values
                grouped_expenses[category].append({
                    "date": str(date),
                    "amount": amount,
                    "note": note if note is not None else ""
                })
                
        # Формируем категории из плана
        for p in self.plan:
            name = p["category"]
            planned = p["plan"]
            spent = p["spent"]
            expenses = grouped_expenses.get(name, [])

            categories_data.append({
                "name": name,
                "planned": planned,
                "spent": spent,
                "expenses": expenses
            })

        return {
            "user_id": self.user_id,
            "budget": {
                "categories": categories_data
            },
            "report": ""  # Можно добавить отчёт позже
        }
        
    async def save(self, filename: str):
        time = datetime.datetime.now().strftime("%Y-%m-%d")
        data = await self.to_json()
        with open(f"json/{filename}_{time}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)