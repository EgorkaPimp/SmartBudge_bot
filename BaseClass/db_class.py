import sqlite3
from BaseClass.log_class import LogCLassAll

class InitDB:
    def __init__(self):
        self.conn = sqlite3.connect('db/pecuniary.db')
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.conn.cursor()
