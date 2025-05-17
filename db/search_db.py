import sqlite3
from io import text_encoding


async def view_categories():
    with sqlite3.connect('db/home.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM plan")
        test = cursor.fetchall()
        tables = {}
        for i in test:
            tables[i[1]] = i[2]
        return tables


def search_cat():
    with sqlite3.connect('db/home.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT category FROM plan')
    cat = cursor.fetchall()
    return cat

def search_sum(category):
    with sqlite3.connect('db/home.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT sum_money FROM plan WHERE category = ?',
                       (category.lower(),))
    sum_money = cursor.fetchall()
    return (sum_money[0])[0]

def rewrite_sum(category, new_sum):
    with sqlite3.connect('db/home.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE plan SET sum_money = ? WHERE category = ?',
                       (new_sum, category.lower()))

