import sqlite3
from BaseClass.log_class import LogCLassAll

class InitDB:
    def __init__(self):
        self.conn = sqlite3.connect('db/pecuniary.db')
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()

class CreateDB(InitDB):
    def __init__(self):
        super().__init__()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scheduler_default (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                day TEXT INTEGER,
                hour INTEGER,
                minute INTEGER,
                state INTEGER
            )
        ''')
        self.fill_scheduler_default()
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS plan (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                category TEXT,
                sum_money INTEGER 
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                category TEXT,
                sum_money INTEGER 
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS type_budget (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                reverse_budget INTEGER,
                financial_diary INTEGER 
            )
        ''')
        self.conn.commit()
        LogCLassAll().info("DataBase correct started")
    
    def fill_scheduler_default(self):
        self.cursor.execute("SELECT 1 FROM scheduler_default WHERE state = ?",
                       (1,))
        if self.cursor.fetchone():
            LogCLassAll().debug("The basic values of the planner are filled")
        else:
            self.cursor.execute("INSERT INTO scheduler_default "
                                "(day, hour, minute, state)"
                                "VALUES (?, ?, ?, ?)",
                                (1, 22, 45, 1))
        
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