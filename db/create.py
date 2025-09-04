from BaseClass.log_class import LogCLassAll
from BaseClass.db_class import InitDB

class CreateDB(InitDB):
    def __init__(self):
        super().__init__()
        
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS type_budget (
                user_id INTEGER PRIMARY KEY,
                reverse_budget INTEGER,
                financial_diary INTEGER 
            )
        ''')
        
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
                user_id INTEGER,
                category TEXT,
                sum_money INTEGER,
                FOREIGN KEY (user_id) REFERENCES type_budget(user_id) ON DELETE CASCADE
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reverse_budget (
                user_id INTEGER,
                category TEXT,
                sum_money INTEGER,
                FOREIGN KEY (user_id) REFERENCES type_budget(user_id) ON DELETE CASCADE
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scheduler_user (
                user_id INTEGER,
                day TEXT INTEGER,
                hour INTEGER,
                minute INTEGER,
                state INTEGER,
                FOREIGN KEY (user_id) REFERENCES type_budget(user_id) ON DELETE CASCADE
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
        