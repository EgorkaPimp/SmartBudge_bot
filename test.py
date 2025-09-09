from BaseClass.db_class import InitDB
import random
class AddDB(InitDB):
    def __init__(self):
        super().__init__()
        
    def add(self, user_id):
        self.cursor.execute("""
            SELECT 
                r.category   AS Категория,
                r.sum_money  AS Сумма,
                p.sum_money  AS План,
                (p.sum_money - r.sum_money) AS Осталось
            FROM reverse_budget r
            JOIN plan p 
                ON r.category = p.category 
               AND r.user_id = p.user_id
            WHERE r.user_id = ?;
        """, (user_id,))
        
        return self.cursor.fetchall()

x = AddDB().add(933194755)
print(x[0])
for a, b, c, d in x:
    print (1, a)
    print (2, b)
    print (3, c)
    print (4, d)
    
for i in x:
    print(i)
    print(i[2])