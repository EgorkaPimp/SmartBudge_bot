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
        self.conn.commit()
    
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