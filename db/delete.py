from BaseClass.log_class import LogCLassAll
from BaseClass.db_class import InitDB

class DeleteDB(InitDB):
    def __init__(self):
        super().__init__()
        
    async def delete_category(self, user_id: int, category: str):
        LogCLassAll().debug(f'Delete category user: {user_id}')
        self.cursor.execute("DELETE FROM plan WHERE user_id = ? AND category = ?",
                            (user_id, category.lower()))
        self.cursor.execute("DELETE FROM reverse_budget WHERE user_id = ? AND category = ?",
                            (user_id, category.lower()))
        self.conn.commit()
        
        