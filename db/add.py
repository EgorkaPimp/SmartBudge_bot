from BaseClass.log_class import LogCLassAll
from BaseClass.db_class import InitDB

class AddDB(InitDB):
    def __init__(self):
        super().__init__()
    
    def add_category_db(self, user_id: int, category: str, sum_money: int):
        self.cursor.execute("INSERT INTO plan "
                            "(user_id, category, sum_money)"
                            "VALUES (?, ?, ?)",
                            (user_id, category, sum_money))
        self.conn.commit()
        LogCLassAll().info(f"Add new category {category} for user: {user_id} with sum {sum_money} ")
        
    def add_user_type_budget(self, user_id: int, type_budget: 'str'):
        if type_budget == 'reverse':
            self.cursor.execute("INSERT INTO type_budget "
                            "(user_id, reverse_budget, financial_diary)"
                            "VALUES (?, ?, ?)",
                            (user_id, 1, 0))
            LogCLassAll().info(f"Add user {user_id} with func reverse budget")
        elif type_budget == 'diary':
            self.cursor.execute("INSERT INTO type_budget "
                            "(user_id, reverse_budget, financial_diary)"
                            "VALUES (?, ?, ?)",
                            (user_id, 0, 1))
            LogCLassAll().info(f"Add user {user_id} with func financial diary")
        else:
            LogCLassAll().error("Wrong type")   
        self.conn.commit()