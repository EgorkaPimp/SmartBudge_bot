from BaseClass.db_class import InitDB
import random
class AddDB(InitDB):
    def __init__(self):
        super().__init__()
        
    def add(self, user_id):
        self.cursor.execute("INSERT INTO type_budget "
                            "(user_id, reverse_budget, financial_diary)"
                            "VALUES (?, ?, ?)",
                            (user_id, 1, 0))
        self.conn.commit()
        

for i in range(100):
    AddDB().add(random.randint(1000, 60000000))