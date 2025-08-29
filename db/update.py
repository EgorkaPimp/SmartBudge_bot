from BaseClass.log_class import LogCLassAll
from BaseClass.db_class import InitDB

class UpdateDB(InitDB):
    def __init__(self):
        super().__init__()
        
    async def update_sum_reverse_budget(self, user_id: int, category: str, new_sum: int):
        LogCLassAll().debug(f'Update sum_money user: {user_id}')
        self.cursor.execute('UPDATE reverse_budget SET sum_money = ?' 
                            'WHERE user_id = ? AND category = ?',
                            (new_sum, user_id, category.lower(),))
        self.conn.commit()
        
    async def update_name_category(self, user_id: int, category: str, new_name: str):
        LogCLassAll().debug(f'Update name category user: {user_id}')
        self.cursor.execute('UPDATE reverse_budget SET category = ?' 
                            'WHERE user_id = ? AND category = ?',
                            (new_name, user_id, category.lower(),))
        self.cursor.execute('UPDATE plan SET category = ?' 
                            'WHERE user_id = ? AND category = ?',
                            (new_name, user_id, category.lower(),))
        self.conn.commit()
        
    async def update_sum_category(self, user_id: int, category: str, new_sum: str):
        LogCLassAll().debug(f'Update sum category user: {user_id}')
        self.cursor.execute('UPDATE plan SET sum_money = ?' 
                            'WHERE user_id = ? AND category = ?',
                            (new_sum, user_id, category.lower(),))
        self.conn.commit()