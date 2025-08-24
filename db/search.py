from BaseClass.log_class import LogCLassAll
from BaseClass.db_class import InitDB

class SearchDB(InitDB):
    def __init__(self):
        super().__init__()
        
    def search_default_scheduler(self):
        self.cursor.execute("SELECT * FROM scheduler_default WHERE state = ?",
                       (1,))
        rows = self.cursor.fetchall()
        result_list = [{"day": row[1], "hour": row[2], "minute": row[3]} for row in rows]
        LogCLassAll().debug(f"Values ​​from the base planner are obtained {result_list}")
        return result_list[0]
    
    def search_user(self, user_id: int):
        self.cursor.execute("SELECT 1 FROM type_budget WHERE user_id = ?",
                       (user_id,))
        if self.cursor.fetchone():
            LogCLassAll().debug("User with data id exists")
            return True
        else:
            LogCLassAll().debug(f"New user {user_id}")
            return False
        
    def search_type_budget(self, user_id: int):
        self.cursor.execute("SELECT * FROM type_budget WHERE user_id = ?",
                       (user_id,))
        rows = self.cursor.fetchall()
        result_list = [{"reverse_budget": row[2], "financial_diary": row[3]} for row in rows]
        LogCLassAll().debug(f"Search type list {result_list[0]}")
        return result_list[0]
    
    async def view_categories(self, user_id: int):
        self.cursor.execute("SELECT * FROM reverse_budget "
                            "WHERE user_id = ?",
                            (user_id,))
        tables = {}
        for i in self.cursor.fetchall():
            tables[i[2]] = i[3]
        LogCLassAll().debug(f"Search category {tables}")
        return tables
    
    async def search_category_double(self, user_id: int, category: str):
        LogCLassAll().debug(f'Values ​​passed for search {category}')
        self.cursor.execute("SELECT 1 FROM reverse_budget "
                            "WHERE user_id = ? AND category = ? ",
                            (user_id, category,))
        if self.cursor.fetchone() is None:
            LogCLassAll().debug(f"search double category user:{user_id} category:{category}")
            return False
        else:
            return True
        
    async def search_category_table(self, user_id: int):
        self.cursor.execute("SELECT category FROM reverse_budget "
                            "WHERE user_id = ?",
                            (user_id,))
        all_category = self.cursor.fetchall()
        return all_category